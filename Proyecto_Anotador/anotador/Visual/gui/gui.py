from PySide2.QtCore import SIGNAL
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QMainWindow, QStackedWidget, QWidget, QDialog, QMessageBox

from Proyecto_Anotador.anotador.Mundo.errores import ExisteSeccion, NoExisteNota, NoExisteNotaDestacada, ExisteLibro, \
    NoExistePagina, NotaNoEncontrada, FechaNoEncontrada
from Proyecto_Anotador.anotador.Visual.ui_Dialogo_Crear_nota import Ui_Dialogo_Crear_Nota
from Proyecto_Anotador.anotador.Visual.ui_Dialogo_Modificar_Libro import Ui_Dialogo_Modificar_Libro
from Proyecto_Anotador.anotador.Visual.ui_Dialogo_Nombrar_Libro import Ui_Dialog_Nombrar_Libro
from Proyecto_Anotador.anotador.Visual.ui_Ventana_Nota import Ui_WNota
from Proyecto_Anotador.anotador.Visual.ui_Ventana_Seccion import Ui_WidgetPaginas
from Proyecto_Anotador.anotador.Visual.ui_Ventana_libro import Ui_FormSecciones
from Proyecto_Anotador.anotador.Visual.ui_Ventana_pagina import Ui_WNotas
from Proyecto_Anotador.anotador.Visual.ui_Widget_Buscador_Etiqueta import Ui_WBuscador
from Proyecto_Anotador.anotador.Visual.ui_Widget_Notas_Destacadas import Ui_WNotas_Destacadas
from Proyecto_Anotador.anotador.Visual.ui_Widgetprincipal import Ui_WidgetPrincipal


class Ventana(QMainWindow):
    ARCHIVO="Datos.Anotador"
    def __init__(self,anotador,parent=None):
        QMainWindow.__init__(self,parent)
        self.anotador=anotador
        self.anotador.load(Ventana.ARCHIVO)
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.start_screen =principal(self)
        self.central_widget.addWidget(self.start_screen)
        self.secciones_screen = WidgetLibro(self)
        self.paginas_screen= WidgetSeccion(self)
        self.notas_screen=WidgetPagina(self)
        self.nota_actual_screen=WidgetNota(self)
        self.buscador_screen=WidgetBuscador(self)
        self.notas_destacadas_screen=WidgetNotas_Destacadas(self)
        self.central_widget.addWidget(self.buscador_screen)
        self.central_widget.addWidget(self.start_screen)
        self.central_widget.addWidget(self.secciones_screen)
        self.central_widget.addWidget(self.paginas_screen)
        self.central_widget.addWidget(self.nota_actual_screen)
        self.central_widget.addWidget(self.notas_screen)
        self.central_widget.addWidget( self.informe_screen)
        self.central_widget.addWidget(self.notas_destacadas_screen)
        self.central_widget.setCurrentWidget(self.start_screen)
        self.show()
        self.closeEvent=self.cerrar_ventana
    def cerrar_ventana(self,event):
        self.anotador.save(Ventana.ARCHIVO)
    def actualizar_secciones_pantalla(self,libro):
        self.central_widget.removeWidget( self.secciones_screen)
        self.secciones_screen= WidgetLibro(self, libro)
        self.secciones_screen.actualizar_listasecciones()
        self.central_widget.addWidget(self.secciones_screen)
    def actualizar_paginas_pantalla(self,seccion):
        self.central_widget.removeWidget(self.paginas_screen)
        self.paginas_screen = WidgetSeccion(self, seccion)
        self.paginas_screen.actualizar_listapaginas()
        self.central_widget.addWidget(self.paginas_screen)
    def actualizar_notas_pantalla(self,pagina):
        self.notas_screen=WidgetPagina(self, pagina)
        self.notas_screen.actualizar_listanotas()
        self.central_widget.addWidget(self.notas_screen)
    def actualizar_nota_actual(self,nota):
        self.central_widget.removeWidget(self.nota_actual_screen)
        self.nota_actual_screen = WidgetNota(self, nota)
        self.nota_actual_screen.actualizar_listaetiquetas()
        if nota.contenido!="":
            self.nota_actual_screen.ui.plainTextEditContenido.setPlainText(nota.contenido)
        if self.nota_actual_screen.nota.destacado:
            self.nota_actual_screen.ui.pushButtonDestacar.setText("Desmarcar")
        self.central_widget.addWidget(self.nota_actual_screen)

class WidgetLibro(QWidget):
    def __init__(self,parent,libro=None):
        QWidget.__init__(self,parent)
        self.ui=Ui_FormSecciones()
        self.ui.setupUi(self)
        self._configurar()
        self.libro=libro
    def _configurar(self):
        self.ui.listViewSecciones_2.setModel(QStandardItemModel())
        self.connect(self.ui.pushButtonRegresar_2, SIGNAL("clicked()"), self.cambiar_ventana_anterior)
        self.ui.pushButtonCrear_Seccion_2.clicked.connect(self.abrirdialogocrear)
        self.ui.listViewSecciones_2.selectionModel().selectionChanged.connect(self.selecionar_seccion)
        self.ui.pushButton_Borrar_seccion_2.clicked.connect(self.borrarseccion)
        self.ui.pushButton_Modificar_seccion_2.clicked.connect(self.abrir_dialogo_modificar)
        self.ui.pushButton_Archivar_seccion_2.clicked.connect(self.borrarseccion)
        self.connect(self.ui.pushButton_Ver_seccion_2, SIGNAL("clicked()"), self.cambiar_ventanta)
    def actualizar_listasecciones(self):
        self.ui.listViewSecciones_2.model().clear()
        secciones=self.libro.secciones.values()
        for seccion in secciones:
            item = QStandardItem(str(seccion))
            item.setEditable(False)
            item.seccion = seccion
            self.ui.listViewSecciones_2.model().appendRow(item)
    def abrirdialogocrear(self):
        dialogo = DialogoCrear(self)
        resp = dialogo.exec_()
        if resp == QDialog.Accepted:
            titulo = dialogo.ui.lineEditTitulo.text()
            try:
                self.libro.agregar_seccion(titulo)
                self.ingresar_listasecciones(self.libro.secciones[titulo])
            except ExisteSeccion:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error Seccion con titulo {titulo} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
    def ingresar_listasecciones(self, seccion):
        item = QStandardItem(str(seccion))
        item.setEditable(False)
        item.seccion=seccion
        self.ui.listViewSecciones_2.model().appendRow(item)
    def cambiar_ventana_anterior(self):
        self.parent().setCurrentWidget(
            self.parent().parent().start_screen)
    def actualizarSelecion(self):
        indice = self.ui.listViewSecciones_2.selectedIndexes()[0]
        seccion = self.ui.listViewSecciones_2.model().itemFromIndex(indice).seccion
        self.parent().parent().actualizar_paginas_pantalla(seccion)
    def cambiar_ventanta(self):
        self.actualizarSelecion()
        self.parent().setCurrentWidget(self.parent().parent().paginas_screen)
    def abrir_dialogo_modificar(self):
        indice = self.ui.listViewSecciones_2.selectedIndexes()[0]
        titulo= self.ui.listViewSecciones_2.model().itemFromIndex(indice).seccion.nombre
        dialog=DialogoModificar(titulo)
        resp=dialog.exec_()
        new=dialog.ui.lineEditTituloNuevo.text()
        if resp==QDialog.Accepted:
            try:
                self.libro.modificar_seccion(titulo,new)
                self.actualizar_listasecciones()
            except ExisteSeccion:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error seccion con titulo {new} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
    def borrarseccion(self):
        indice=self.ui.listViewSecciones_2.selectedIndexes()[0]
        titulo=self.ui.listViewSecciones_2.model().itemFromIndex(indice).seccion.nombre
        self.libro.borrar_seccion(titulo)
        self.actualizar_listasecciones()
        if len(self.libro.secciones)==0:
            self.actualizar_botones_secciones(False)
    def selecionar_seccion(self,selected, deselected):
        indices=selected.indexes()
        if len(indices)>0:
            self.actualizar_botones_secciones(True)
        else:
            self.actualizar_botones_secciones(False)

    def actualizar_botones_secciones(self, boolean:bool):
        self.ui.pushButton_Archivar_seccion_2.setEnabled(boolean)
        self.ui.pushButton_Ver_seccion_2.setEnabled(boolean)
        self.ui.pushButton_Borrar_seccion_2.setEnabled(boolean)
        self.ui.pushButton_Modificar_seccion_2.setEnabled(boolean)
class DialogoModificar(QDialog):
    def __init__(self, titulo, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Dialogo_Modificar_Libro()
        self.ui.setupUi(self)
        self.ui.lineEditTitulo.setText(titulo)
    def accept(self) -> None:
        if self.ui.lineEditTituloNuevo.text() != "":
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
class   DialogoCrear(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui =Ui_Dialog_Nombrar_Libro()
        self.ui.setupUi(self)
    def accept(self) -> None:
        if self.ui.lineEditTitulo.text() != "":
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
class DialogoCrear_nota(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui =Ui_Dialogo_Crear_Nota()
        self.ui.setupUi(self)
    def accept(self) -> None:
        if self.ui.lineEditTitulo.text() != "" and self.ui.lineEditEtiqueta.text()!="":
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validación")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios.")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
class WidgetNota(QWidget):
    def __init__(self,parent,nota=None):
        QWidget.__init__(self,parent)
        self.ui = Ui_WNota()
        self.ui.setupUi(self)
        self._configurar()
        self.nota = nota

    def _configurar(self):
        self.ui.listViewEtiquetas.setModel(QStandardItemModel())
        self.connect(self.ui.pushButtonRegresar, SIGNAL("clicked()"), self.cambiar_ventana_anterior)
        self.ui.pushButtonagregarEtiqueta.clicked.connect(self.abrirdialogocrear)
        self.ui.listViewEtiquetas.selectionModel().selectionChanged.connect(self.selecionar_etiqueta)
        self.ui.pushButtonEliminarEtiqueta.clicked.connect(self.borraretiqueta)
        self.ui.pushButtonGuardar.clicked.connect(self.guardar)
        self.ui.pushButtonDestacar.clicked.connect(self.destacado)
        self.ui.plainTextEditContenido.textChanged.connect(self.habilitar_guardado)
    def habilitar_guardado(self):
        self.ui.pushButtonGuardar.setEnabled(True)
    def destacado(self):
        if self.ui.pushButtonDestacar.text()== "Destacar":
            self.ui.pushButtonDestacar.setText("Desmarcar")
            self.nota.destacar_nota(True)
        else:
            self.ui.pushButtonDestacar.setText("Destacar")
            self.nota.destacar_nota(False)
        self.parent().parent().notas_screen.actualizar_listanotas()
    def guardar(self):
        texto=self.ui.plainTextEditContenido.toPlainText()
        self.nota.contenido=texto
        self.ui.pushButtonGuardar.setEnabled(False)
    def actualizar_listaetiquetas(self):
        self.ui.listViewEtiquetas.model().clear()
        etiquetas = self.nota.etiquetas
        for etiqueta in etiquetas:
            item = QStandardItem(str(etiqueta))
            item.setEditable(False)
            item.etiqueta = etiqueta
            self.ui.listViewEtiquetas.model().appendRow(item)

    def abrirdialogocrear(self):
        dialogo = DialogoCrear(self)
        resp = dialogo.exec_()
        if resp == QDialog.Accepted:
            nombre = dialogo.ui.lineEditTitulo.text()
            try:
                self.nota.agregar_etiqueta(nombre)
                self.ingresar_listaetiquetas(nombre)
            except NoExisteNota:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error Etiqueta con titulo {nombre} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def ingresar_listaetiquetas(self, etiqueta):
        item = QStandardItem(str(etiqueta))
        item.setEditable(False)
        item.etiqueta = etiqueta
        self.ui.listViewEtiquetas.model().appendRow(item)

    def cambiar_ventana_anterior(self):
        self.parent().setCurrentWidget(
            self.parent().parent().notas_screen)
    def borraretiqueta(self):
        indice = self.ui.listViewEtiquetas.selectedIndexes()[0]
        nombre = self.ui.listViewEtiquetas.model().itemFromIndex(indice).etiqueta
        self.nota.eliminiar_etiqueta(nombre)
        self.actualizar_listaetiquetas()
    def selecionar_etiqueta(self, selected, deselected):
        indices = selected.indexes()
        if len(indices) > 0:
            if len(self.nota.etiquetas)!=1:
                self.actualizar_boton_etiqueta(True)
            else:
                self.actualizar_boton_etiqueta(False)
        else:
            self.actualizar_boton_etiqueta(False)

    def actualizar_boton_etiqueta(self, boolean: bool):
        self.ui.pushButtonEliminarEtiqueta.setEnabled(boolean)

class WidgetNotas_Destacadas(QWidget):
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.ui = Ui_WNotas_Destacadas()
        self.ui.setupUi(self)
        self._configurar()
        self.anotador = parent.anotador
    def _configurar(self):
        self.ui.listViewNotas.setModel(QStandardItemModel())
        self.ui.listViewNotas.selectionModel().selectionChanged.connect(self.selecionar)
        self.ui.pushButton_Ver_Nota.clicked.connect(self.ver_nota)
        self.ui.pushButton_Home.clicked.connect(self.cambiar_ventana_principal)
        self.ui.pushButtonBuscar.clicked.connect(self.buscar_destacados)
        self.ui.pushButton_Buscar_Nota.clicked.connect(self.cambiar_ventana_buscador)
        self.ui.pushButton_Informe_Etiqueta.clicked.connect(self.cambiar_ventana_informe)
    def cambiar_ventana_informe(self):
        self.parent().parent().informe_screen.ui.listViewNotas.model().clear()
        self.parent().parent().informe_screen.ui.lineEditEtiqueta.setText("")
        self.parent().parent().informe_screen.ui.label_cantidad_notas_valor.setText("")
        self.parent().setCurrentWidget(self.parent().parent().informe_screen)
    def cambiar_ventana_buscador(self):
        self.parent().parent().buscador_screen.ui.listViewNotas.model().clear()
        self.parent().parent().buscador_screen.ui.lineEditEtiqueta.setText("")
        self.parent().setCurrentWidget(self.parent().parent().buscador_screen)
    def buscar_destacados(self):
        try:
           lista_notas=self.anotador.agregar_a_destacadas()
        except NoExisteNotaDestacada:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("ERROR EXISTENCIAL")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(f"No fue encontrada ninguna nota destacada")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
        else:
            self.ui.listViewNotas.model().clear()
            for tupla in lista_notas:
                nota,lista_ruta=tupla
                display=f"{lista_ruta[0].nombre}/{lista_ruta[1].nombre}/{lista_ruta[2].nombre}/{str(nota)}"
                item = QStandardItem(display)
                item.setEditable(False)
                item.nota=nota
                item.ruta=lista_ruta
                self.ui.listViewNotas.model().appendRow(item)
    def cambiar_ventana_principal(self):
        self.parent().setCurrentWidget(
            self.parent().parent().start_screen)
    def ver_nota(self):
        self.actualizarSelecion()
        self.parent().setCurrentWidget(
            self.parent().parent().nota_actual_screen)
    def selecionar(self,selected,deselected):
        indices=selected.indexes()
        if len(indices) > 0:
            self.ui.pushButton_Ver_Nota.setEnabled(True)
        else:
            self.ui.pushButton_Ver_Nota.setEnabled(False)
    def actualizarSelecion(self):
        indice = self.ui.listViewNotas.selectedIndexes()[0]
        nota = self.ui.listViewNotas.model().itemFromIndex(indice).nota
        ruta=self.ui.listViewNotas.model().itemFromIndex(indice).ruta
        libro,seccion,pagina=ruta
        self.parent().parent().actualizar_secciones_pantalla(libro)
        self.parent().parent().actualizar_paginas_pantalla(seccion)
        self.parent().parent().actualizar_notas_pantalla(pagina)
        self.parent().parent().actualizar_nota_actual(nota)

class WidgetPagina(QWidget):
    def __init__(self,parent,pagina=None):
        QWidget.__init__(self,parent)
        self.ui =Ui_WNotas()
        self.ui.setupUi(self)
        self._configurar()
        self.pagina=pagina

    def _configurar(self):
        self.ui.listViewNotas_2.setModel(QStandardItemModel())
        self.connect(self.ui.pushButtonRegresar_2, SIGNAL("clicked()"), self.cambiar_vetana_anterior)
        self.ui.pushButtonCrear_Nota_2.clicked.connect(self.abrirdialogocrear)
        self.ui.listViewNotas_2.selectionModel().selectionChanged.connect(self.selecionar_nota)
        self.ui.pushButton_Borrar_Nota_2.clicked.connect(self.borrarnota)
        self.ui.pushButton_Modificar_Nota_2.clicked.connect(self.abrir_dialogo_modificar)
        self.ui.pushButton_Archivar_Nota_2.clicked.connect(self.borrarnota)
        self.connect(self.ui.pushButton_Ver_Nota_2, SIGNAL("clicked()"), self.cambiar_ventana)

    def actualizar_listanotas(self):
        self.ui.listViewNotas_2.model().clear()
        notas = self.pagina.notas.values()
        for nota in notas:
            item = QStandardItem(str(nota))
            item.setEditable(False)
            item.nota = nota
            self.ui.listViewNotas_2.model().appendRow(item)

    def abrirdialogocrear(self):
        dialogo =DialogoCrear_nota(self)
        resp = dialogo.exec_()
        if resp == QDialog.Accepted:
            titulo = dialogo.ui.lineEditTitulo.text()
            etiqueta=dialogo.ui.lineEditEtiqueta.text()
            try:
                self.pagina.agregar_nota(titulo)
                self.pagina.notas[titulo].agregar_etiqueta(etiqueta)
                self.ingresar_listanotas(self.pagina.notas[titulo])
                self.parent().parent().actualizar_nota_actual(self.pagina.notas[titulo])
                self.parent().setCurrentWidget(self.parent().parent().nota_actual_screen)
            except NoExisteNota:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error nota con titulo {titulo} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def ingresar_listanotas(self, nota):
        item = QStandardItem(str(nota))
        item.setEditable(False)
        item.nota =nota
        self.ui.listViewNotas_2.model().appendRow(item)

    def cambiar_vetana_anterior(self):
        self.parent().setCurrentWidget(
            self.parent().parent().paginas_screen)

    def actualizarSelecion(self):
        indice = self.ui.listViewNotas_2.selectedIndexes()[0]
        nota = self.ui.listViewNotas_2.model().itemFromIndex(indice).nota
        self.parent().parent().actualizar_nota_actual(nota)

    def cambiar_ventana(self):
        self.actualizarSelecion()
        self.parent().setCurrentWidget(self.parent().parent().nota_actual_screen)
    def abrir_dialogo_modificar(self):
        indice = self.ui.listViewNotas_2.selectedIndexes()[0]
        titulo = self.ui.listViewNotas_2.model().itemFromIndex(indice).nota.nombre
        dialog = DialogoModificar(titulo)
        resp = dialog.exec_()
        new = dialog.ui.lineEditTituloNuevo.text()
        if resp == QDialog.Accepted:
            try:
                self.pagina.modificar_nombre_nota(titulo, new)
                self.actualizar_listanotas()
            except NoExisteNota:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error Nota con titulo {new} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def borrarnota(self):
        indice = self.ui.listViewNotas_2.selectedIndexes()[0]
        titulo = self.ui.listViewNotas_2.model().itemFromIndex(indice).nota.nombre
        self.pagina.borrar_nota(titulo)
        self.actualizar_listanotas()
        if len(self.pagina.notas) == 0:
            self.actualizar_botones_notas(False)
    def selecionar_nota(self, selected, deselected):
        indices = selected.indexes()
        if len(indices) > 0:
            self.actualizar_botones_notas(True)
        else:
            self.actualizar_botones_notas(False)

    def actualizar_botones_notas(self, boolean: bool):
        self.ui.pushButton_Archivar_Nota_2.setEnabled(boolean)
        self.ui.pushButton_Ver_Nota_2.setEnabled(boolean)
        self.ui.pushButton_Borrar_Nota_2.setEnabled(boolean)
        self.ui.pushButton_Modificar_Nota_2.setEnabled(boolean)
class principal(QWidget):
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.ui =Ui_WidgetPrincipal()
        self.ui.setupUi(self)
        self.anotador = parent.anotador
        self._configurar()
    def _configurar(self):
        self.ui.pushButtonCrear_Libro.clicked.connect(self.abrir_dialogo_crearlibro)
        self.ui.listViewLibros.setModel(QStandardItemModel())
        self.actualizar_listalibros()
        self.ui.listViewLibros.selectionModel().selectionChanged.connect(self.selecionar_libro)
        self.ui.pushButton_Borrar_Libro.clicked.connect(self.borrarlibro)
        self.ui.pushButton_Modificar_Libro.clicked.connect(self.abrir_dialogo_modificarlibro)
        self.ui.pushButton_Archivar_Libro.clicked.connect(self.borrarlibro)
        self.connect(self.ui.pushButton_Ver_Libro, SIGNAL("clicked()"), self.cambiar_Ventana)
        self.connect(self.ui.pushButton_Buscar_Nota,SIGNAL("clicked()"),self.buscar)
        self.ui.pushButton_Informe_Etiqueta.clicked.connect(self.cambiar_ventana_informe)
        self.ui.pushButton_Notas_Destacadas.clicked.connect(self.cambiar_ventana_notas_destacadas)
    def cambiar_ventana_notas_destacadas(self):
        self.parent().parent().notas_destacadas_screen.ui.listViewNotas.model().clear()
        self.parent().setCurrentWidget(self.parent().parent().notas_destacadas_screen)
    def cambiar_ventana_informe(self):
        self.parent().parent().informe_screen.ui.listViewNotas.model().clear()
        self.parent().parent().informe_screen.ui.lineEditEtiqueta.setText("")
        self.parent().parent().informe_screen.ui.label_cantidad_notas_valor.setText("")
        self.parent().setCurrentWidget(self.parent().parent().informe_screen)
    def buscar(self):
        self.parent().parent().buscador_screen.ui.listViewNotas.model().clear()
        self.parent().parent().buscador_screen.ui.lineEditEtiqueta.setText("")
        self.parent().setCurrentWidget(self.parent().parent().buscador_screen)
    def actualizarSelecion(self):
        indice = self.ui.listViewLibros.selectedIndexes()[0]
        libro = self.ui.listViewLibros.model().itemFromIndex(indice).libro
        self.parent().parent().actualizar_secciones_pantalla(libro)
    def cambiar_Ventana(self):
        self.actualizarSelecion()
        self.parent().setCurrentWidget(self.parent().parent().secciones_screen)
    def abrir_dialogo_modificarlibro(self):
        indice = self.ui.listViewLibros.selectedIndexes()[0]
        titulo= self.ui.listViewLibros.model().itemFromIndex(indice).libro.nombre
        dialog=DialogoModificar(titulo)
        resp=dialog.exec_()
        new=dialog.ui.lineEditTituloNuevo.text()
        if resp==QDialog.Accepted:
            try:
                self.anotador.modificar_libro(titulo,new)
                self.actualizar_listalibros()
            except ExisteLibro:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error Libro con titulo {new} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def borrarlibro(self):
        indice=self.ui.listViewLibros.selectedIndexes()[0]
        titulo=self.ui.listViewLibros.model().itemFromIndex(indice).libro.nombre
        self.anotador.borrar_libro(titulo)
        self.actualizar_listalibros()
        if len(self.anotador.libros)==0:
            self.actualizar_botones_libro(False)
    def selecionar_libro(self,selected, deselected):
        indices=selected.indexes()
        if len(indices)>0:
            self.actualizar_botones_libro(True)
        else:
            self.actualizar_botones_libro(False)

    def actualizar_botones_libro(self, boolean:bool):
        self.ui.pushButton_Archivar_Libro.setEnabled(boolean)
        self.ui.pushButton_Ver_Libro.setEnabled(boolean)
        self.ui.pushButton_Borrar_Libro.setEnabled(boolean)
        self.ui.pushButton_Modificar_Libro.setEnabled(boolean)
    def actualizar_listalibros(self):
        self.ui.listViewLibros.model().clear()
        libros=self.anotador.libros.values()
        for libro in libros:
            item = QStandardItem(str(libro))
            item.setEditable(False)
            item.libro = libro
            self.ui.listViewLibros.model().appendRow(item)
    def ingresar_listalibros(self, libro):
        item = QStandardItem(str(libro))
        item.setEditable(False)
        item.libro=libro
        self.ui.listViewLibros.model().appendRow(item)

    def abrir_dialogo_crearlibro(self):
        dialogo =DialogoCrear(self)
        resp = dialogo.exec_()
        if resp==QDialog.Accepted:
            titulo=dialogo.ui.lineEditTitulo.text()
            try:
                self.anotador.agregar_libro(titulo)
                self.ingresar_listalibros(self.anotador.libros[titulo])
            except ExisteLibro:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error Libro con titulo {titulo} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
class WidgetSeccion(QWidget):
    def __init__(self,parent,seccion=None):
        QWidget.__init__(self,parent)
        self.ui =Ui_WidgetPaginas()
        self.ui.setupUi(self)
        self._configurar()
        self.seccion =seccion

    def _configurar(self):
        self.ui.listViewPaginas.setModel(QStandardItemModel())
        self.connect(self.ui.pushButtonRegresar, SIGNAL("clicked()"), self.cambiar_ventana_anterior)
        self.ui.pushButtonCrear_Pagina.clicked.connect(self.abrirdialogocrear)
        self.ui.listViewPaginas.selectionModel().selectionChanged.connect(self.selecionar_pagina)
        self.ui.pushButton_Borrar_Pagina.clicked.connect(self.borrarpagina)
        self.ui.pushButton_Modificar_Pagina.clicked.connect(self.abrir_dialogo_modificar)
        self.ui.pushButton_Archivar_Pagina.clicked.connect(self.borrarpagina)
        self.connect(self.ui.pushButton_Ver_Pagina, SIGNAL("clicked()"), self.cambiar_ventana)

    def actualizar_listapaginas(self):
        self.ui.listViewPaginas.model().clear()
        paginas = self.seccion.paginas.values()
        for pagina in paginas:
            item = QStandardItem(str(pagina))
            item.setEditable(False)
            item.pagina = pagina
            self.ui.listViewPaginas.model().appendRow(item)

    def abrirdialogocrear(self):
        dialogo = DialogoCrear(self)
        resp = dialogo.exec_()
        if resp == QDialog.Accepted:
            titulo = dialogo.ui.lineEditTitulo.text()
            try:
                self.seccion.agregar_pagina(titulo)
                self.ingresar_listapaginas(self.seccion.paginas[titulo])
            except NoExistePagina:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error pagina con titulo {titulo} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def ingresar_listapaginas(self, pagina):
        item = QStandardItem(str(pagina))
        item.setEditable(False)
        item.pagina =pagina
        self.ui.listViewPaginas.model().appendRow(item)

    def cambiar_ventana_anterior(self):
        self.parent().setCurrentWidget(
            self.parent().parent().secciones_screen)

    def actualizarSelecion(self):
        indice = self.ui.listViewPaginas.selectedIndexes()[0]
        pagina = self.ui.listViewPaginas.model().itemFromIndex(indice).pagina
        self.parent().parent().actualizar_notas_pantalla(pagina)

    def cambiar_ventana(self):
        self.actualizarSelecion()
        self.parent().setCurrentWidget(self.parent().parent().notas_screen)

    def abrir_dialogo_modificar(self):
        indice = self.ui.listViewPaginas.selectedIndexes()[0]
        titulo = self.ui.listViewPaginas.model().itemFromIndex(indice).pagina.nombre
        dialog = DialogoModificar(titulo)
        resp = dialog.exec_()
        new = dialog.ui.lineEditTituloNuevo.text()
        if resp == QDialog.Accepted:
            try:
                self.seccion.modificar_pagina(titulo, new)
                self.actualizar_listapaginas()
            except NoExistePagina:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ERROR EXISTENCIAL")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(f"Error pagina con titulo {new} ya existe")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()

    def borrarpagina(self):
        indice = self.ui.listViewPaginas.selectedIndexes()[0]
        titulo = self.ui.listViewPaginas.model().itemFromIndex(indice).pagina.nombre
        self.seccion.borrar_pagina(titulo)
        self.actualizar_listapaginas()
        if len(self.seccion.paginas) == 0:
            self.actualizar_botones_paginas(False)
    def selecionar_pagina(self, selected, deselected):
        indices = selected.indexes()
        if len(indices) > 0:
            self.actualizar_botones_paginas(True)
        else:
            self.actualizar_botones_paginas(False)

    def actualizar_botones_paginas(self, boolean: bool):
        self.ui.pushButton_Archivar_Pagina.setEnabled(boolean)
        self.ui.pushButton_Ver_Pagina.setEnabled(boolean)
        self.ui.pushButton_Borrar_Pagina.setEnabled(boolean)
        self.ui.pushButton_Modificar_Pagina.setEnabled(boolean)
class WidgetBuscador(QWidget):
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.ui = Ui_WBuscador()
        self.ui.setupUi(self)
        self._configurar()
        self.anotador = parent.anotador
    def _configurar(self):
        self.ui.listViewNotas.setModel(QStandardItemModel())
        self.ui.listViewNotas.selectionModel().selectionChanged.connect(self.selecionar)
        self.ui.pushButton_Ver_Nota.clicked.connect(self.ver_nota)
        self.ui.pushButton_Home.clicked.connect(self.cambiar_ventana_principal)
        self.ui.pushButtonBuscarFecha.clicked.connect(self.busqueda_porfecha)
        self.ui.pushButtonBuscarEtiqueta.clicked.connect(self.busqueda_poretiqueta)
        self.ui.pushButton_Informe_Etiqueta_2.clicked.connect(self.cambiar_ventana_informe)
        self.ui.pushButton_Notas_Destacadas_2.clicked.connect(self.cambiar_ventana_notas_destacadas)
    def cambiar_ventana_notas_destacadas(self):
        self.parent().parent().notas_destacadas_screen.ui.listViewNotas.model().clear()
        self.parent().setCurrentWidget(self.parent().parent().notas_destacadas_screen)
    def cambiar_ventana_informe(self):
        self.parent().parent().informe_screen.ui.listViewNotas.model().clear()
        self.parent().parent().informe_screen.ui.lineEditEtiqueta.setText("")
        self.parent().parent().informe_screen.ui.label_cantidad_notas_valor.setText("")
        self.parent().setCurrentWidget(self.parent().parent().informe_screen)
    def busqueda_poretiqueta(self):
        etiqueta=self.ui.lineEditEtiqueta.text()
        try:
            lista_notas=self.anotador.buscar_nota_por_etiqueta(etiqueta)
        except NotaNoEncontrada:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("ERROR EXISTENCIAL")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(f"No fue encontrada ninguna nota con la etiqueta: {etiqueta}")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
        else:
            self.ui.listViewNotas.model().clear()
            for tupla in lista_notas:
                nota,lista_ruta=tupla
                display=f"{lista_ruta[0].nombre}/{lista_ruta[1].nombre}/{lista_ruta[2].nombre}/{str(nota)}"
                item = QStandardItem(display)
                item.setEditable(False)
                item.nota =nota
                item.ruta=lista_ruta
                self.ui.listViewNotas.model().appendRow(item)
    def busqueda_porfecha(self):
        fecha = self.ui.dateEdit.text()
        try:
            lista_notas = self.anotador.busqueda_por_fecha(fecha)
        except FechaNoEncontrada:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("ERROR EXISTENCIAL")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText(f"No fue encontrada ninguna nota con la fecha: {fecha}")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
        else:
            self.ui.listViewNotas.model().clear()
            for tupla in lista_notas:
                nota, lista_ruta = tupla
                display = f"{lista_ruta[0].nombre}/{lista_ruta[1].nombre}/{lista_ruta[2].nombre}/{str(nota)}"
                item = QStandardItem(display)
                item.setEditable(False)
                item.nota = nota
                item.ruta = lista_ruta
                self.ui.listViewNotas.model().appendRow(item)
    def cambiar_ventana_principal(self):
        self.parent().setCurrentWidget(
            self.parent().parent().start_screen)
    def ver_nota(self):
        self.actualizarSelecion()
        self.parent().setCurrentWidget(
            self.parent().parent().nota_actual_screen)
    def selecionar(self,selected,deselected):
        indices=selected.indexes()
        if len(indices) > 0:
            self.ui.pushButton_Ver_Nota.setEnabled(True)
        else:
            self.ui.pushButton_Ver_Nota.setEnabled(False)
    def actualizarSeleccion(self):
        indice = self.ui.listViewNotas.selectedIndexes()[0]
        nota = self.ui.listViewNotas.model().itemFromIndex(indice).nota
        ruta=self.ui.listViewNotas.model().itemFromIndex(indice).ruta
        libro,seccion,pagina=ruta
        self.parent().parent().actualizar_secciones_pantalla(libro)
        self.parent().parent().actualizar_paginas_pantalla(seccion)
        self.parent().parent().actualizar_notas_pantalla(pagina)
        self.parent().parent().actualizar_nota_actual(nota)

