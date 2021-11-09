import os
import pickle
import time

from errores import ExisteLibro, NotaNoEncontrada, NoExisteNotaDestacada, FechaNoEncontrada, ExisteSeccion, NoExistePagina, NoExisteNota, NoExisteNombreEtiqueta


class Anotador:

    def __init__(self):
        self.libros = {}

    def guardar(self,archivo):
        with open(archivo, "wb") as f:
            pickle.dump(self,f)

    def cargar(self,archivo):
        try:
            with open(archivo, "rb") as f:
                if os.path.exists(archivo) and os.path.getsize(archivo)> 0:
                    dato = pickle.load(f)
                    self.libros = dato.libros
                else:
                    return
        except FileNotFoundError:
            with open(archivo, "x") as f:
                return


    def libro_existe(self, nombre):
        llave = self.libros.keys()
        valor = nombre in llave
        if valor is False:
            raise ExisteLibro()

    def agregar_libro(self, nombre: str):
        self.libro_existe(nombre)
        self.libros[nombre] = Libro(nombre)

    def borrar_libro(self, nombre):
        self.libros.pop(nombre)

    def modificar_libro(self, nombre, nuevo_nombre, fecha, nueva_fecha):
            self.libro_existe(nuevo_nombre)
            viejo_nombre = self.libros.pop(nombre)
            viejo_nombre.nombre = nuevo_nombre
            self.libros[nuevo_nombre] = viejo_nombre
            fecha_vieja = self.libros.pop(fecha)
            fecha_vieja.fecha = nueva_fecha
            self.libros[nuevo_nombre].fecha = nueva_fecha
    def buscar_nota_por_etiqueta(self, etiqueta):
            lista_notas_etiqueta = []
            libros = self.libros
            for llave_libro in libros.keys():
                libro = libros[llave_libro]
                secciones = libro.secciones
                for llave_seccion in secciones.keys():
                    seccion = secciones[llave_seccion]
                    paginas = seccion.paginas
                    for llave_pagina in paginas.keys():
                        pagina = paginas[llave_pagina]
                        notas = pagina.notas
                        for llave_nota in notas.keys():
                            nota = notas[llave_nota]
                            if len(nota.etiquetas) != 0:
                                etiquetas = nota.etiquetas
                                if etiqueta in etiquetas:
                                    lista_notas_etiqueta.append(
                                        (nota, [libro, seccion, pagina]))
            if len(lista_notas_etiqueta) == 0:
                raise NotaNoEncontrada()
            return lista_notas_etiqueta

    def agregar_a_destacadas(self):
            lista_notas_destacadas = []
            libros = self.libros
            for llave_libro in libros.keys():
                libro = libros[llave_libro]
                secciones = libro.secciones
                for llave_seccion in secciones.keys():
                    seccion = secciones[llave_seccion]
                    paginas = seccion.paginas
                    for llave_pagina in paginas.keys():
                        pagina = paginas[llave_pagina]
                        notas = pagina.notas
                        for llave_nota in notas.keys():
                            nota = notas[llave_nota]
                            if nota.destacado:
                                lista_notas_destacadas.append((nota, [libro, seccion, pagina]))
            if len(lista_notas_destacadas) == 0:
                raise NoExisteNotaDestacada()
            return lista_notas_destacadas


    def busqueda_por_fecha(self, fecha):
            lista_notas_fecha = []
            libros = self.libros
            for llave_libro in libros.keys():
                libro = libros[llave_libro]
                secciones = libro.secciones
                for llave_seccion in secciones.keys():
                    seccion = secciones[llave_seccion]
                    paginas = seccion.paginas
                    for llave_pagina in paginas.keys():
                        pagina = paginas[llave_pagina]
                        notas = pagina.notas
                        for llave_nota in notas.keys():
                            nota = notas[llave_nota]
                            if fecha == nota.fecha_creacion:
                                lista_notas_fecha.append(
                                    (nota, [libro, seccion, pagina]))
            if len(lista_notas_fecha) == 0:
                raise FechaNoEncontrada()
            return lista_notas_fecha

class Libro:

    def __init__(self,nombre: str):
        self.fecha = time.strftime("%d/%m/%Y", time.localtime())
        self.nombre: str = nombre
        self.secciones= {}

        def __str__(self):
            return (f"{self.nombre}/{self.fecha}")

    def revisar_agregar_seccion(self, nombre: str):
        self.recorrer_secciones(nombre)
        self.secciones[nombre] = Seccion(nombre)

    def borrar_seccion(self, nombre):
        self.secciones.pop(nombre)

    def modificar_seccion(self, nombre, nuevo_nombre):
        self.recorrer_secciones(nuevo_nombre)
        viejo_nombre = self.secciones.pop(nombre)
        viejo_nombre.nombre = nuevo_nombre
        self.secciones[nuevo_nombre] = viejo_nombre

    def recorrer_secciones(self, nombre: str):
        llaves = self.secciones.keys()
        valor = nombre in llaves
        if valor is False:
            raise ExisteSeccion()

class Seccion:

    def __init__(self, nombre: str):
        self.fecha: str = time.strftime("%d/%m/%Y", time.localtime())
        self.nombre: str = nombre
        self.paginas = {}

    def __str__(self):
        return (f"{self.nombre}/{self.fecha}")

    def recorrer_pagina(self, nombre: str):
        llaves = self.paginas.keys()
        valor = nombre in llaves
        if valor:
            raise NoExistePagina()

    def modificar_pagina(self, nombre: str, nuevo_nombre):
        self.recorrer_pagina(nuevo_nombre)
        viejo_nombre = self.paginas.pop(nombre)
        viejo_nombre.nombre = nuevo_nombre
        self.paginas[nuevo_nombre] = viejo_nombre

    def borrar_pagina(self, nombre):
        self.paginas.pop(nombre)

    def agregar_pagina(self, nombre: str):
        self.recorrer_pagina(nombre)
        self.paginas[nombre] = Pagina(nombre)
class Pagina:

    def __init__(self, nombre: str):
        self.fecha: str = time.strftime("%d/%m/%Y", time.localtime())
        self.nombre: str = nombre
        self.notas={}
        self.notas_destacadas=[]

    def __str__(self):
        return (f"{self.nombre}/{self.fecha}")

    def revisar_nota(self, nombre: str):
            llaves = self.notas.keys()
            valor = nombre in llaves
            if valor:
                raise NoExisteNota()

    def agregar_nota(self, nombre: str, etiqueta=""):
            self.revisar_nota(nombre)
            self.notas[nombre] = Nota(nombre, etiqueta)

    def modificar_nota(self, nombre: str, nuevo_nombre):
            self.revisar_nota(nuevo_nombre)
            viejo_nombre = self.notas.pop(nombre)
            viejo_nombre.nombre = nuevo_nombre
            self.notas[nuevo_nombre] = viejo_nombre

    def borrar_nota(self, nombre):
            self.notas.pop(nombre)

class Nota:

    def __init__(self, nombre: str, etiqueta:""):
        self.fecha: str = time.strftime("%d/%m/%Y", time.localtime())
        self.nombre: str = nombre
        self.etiqueta = etiqueta
        self.contenido = ""

        self.etiquetas = []
        if etiqueta != "":
            self.etiquetas.append(etiqueta)

    def __str__(self):
        if self.notas_destacadas:
            return (f"* {self.nombre}/{self.fecha}")
        return (f"*{self.nombre}/{self.fecha}")

    def agregar_etiqueta(self, etiqueta: str):
        self.buscar_nombre_etiqueta(etiqueta)
        self.etiquetas.append(etiqueta)

    def elimininar_etiqueta(self, etiqueta: str):
        self.buscar_nombre_etiqueta(etiqueta)
        indice = self.etiquetas.index(etiqueta)
        self.etiquetas.pop(indice)

    def buscar_nombre_etiqueta(self, etiqueta):
        valor = etiqueta in self.etiquetas
        if valor is False:
            raise NoExisteNombreEtiqueta




