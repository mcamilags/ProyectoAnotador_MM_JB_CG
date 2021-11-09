# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana_libroTVYMyh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FormSecciones(object):
    def setupUi(self, FormSecciones):
        if not FormSecciones.objectName():
            FormSecciones.setObjectName(u"FormSecciones")
        FormSecciones.resize(523, 473)
        self.verticalLayout = QVBoxLayout(FormSecciones)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(FormSecciones)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(32, 42, 84);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 4)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(-1, 1, -1, -1)
        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 4)
        self.frame_3 = QFrame(self.frame_16)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(74, 139, 218);")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 40))
        self.frame_6.setStyleSheet(u"background-color: rgb(74, 139, 218);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(6, 7, 5, 4)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout_7.addWidget(self.label)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.listViewSecciones_2 = QListView(self.frame_5)
        self.listViewSecciones_2.setObjectName(u"listViewSecciones_2")
        self.listViewSecciones_2.setStyleSheet(u"font: 16pt \"Lucida Handwriting\";")
        self.listViewSecciones_2.setFrameShape(QFrame.NoFrame)
        self.listViewSecciones_2.setFlow(QListView.TopToBottom)
        self.listViewSecciones_2.setViewMode(QListView.IconMode)
        self.listViewSecciones_2.setItemAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.listViewSecciones_2)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_16)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMinimumSize(QSize(189, 0))
        self.frame_9.setStyleSheet(u"background-color: rgb(255, 252, 212);\n"
"background-color: rgb(74, 139, 218);")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButtonCrear_Seccion_2 = QPushButton(self.frame_9)
        self.pushButtonCrear_Seccion_2.setObjectName(u"pushButtonCrear_Seccion_2")
        self.pushButtonCrear_Seccion_2.setStyleSheet(u"background-color: rgb(204, 204, 204);")

        self.verticalLayout_11.addWidget(self.pushButtonCrear_Seccion_2)

        self.pushButton_Ver_seccion_2 = QPushButton(self.frame_9)
        self.pushButton_Ver_seccion_2.setObjectName(u"pushButton_Ver_seccion_2")
        self.pushButton_Ver_seccion_2.setEnabled(False)
        self.pushButton_Ver_seccion_2.setStyleSheet(u"background-color: rgb(204, 204, 204);")

        self.verticalLayout_11.addWidget(self.pushButton_Ver_seccion_2)

        self.pushButton_Modificar_seccion_2 = QPushButton(self.frame_9)
        self.pushButton_Modificar_seccion_2.setObjectName(u"pushButton_Modificar_seccion_2")
        self.pushButton_Modificar_seccion_2.setEnabled(False)
        self.pushButton_Modificar_seccion_2.setStyleSheet(u"background-color: rgb(204, 204, 204);")

        self.verticalLayout_11.addWidget(self.pushButton_Modificar_seccion_2)

        self.pushButton_Archivar_seccion_2 = QPushButton(self.frame_9)
        self.pushButton_Archivar_seccion_2.setObjectName(u"pushButton_Archivar_seccion_2")
        self.pushButton_Archivar_seccion_2.setEnabled(False)
        self.pushButton_Archivar_seccion_2.setStyleSheet(u"background-color: rgb(204, 204, 204);")

        self.verticalLayout_11.addWidget(self.pushButton_Archivar_seccion_2)

        self.pushButton_Borrar_seccion_2 = QPushButton(self.frame_9)
        self.pushButton_Borrar_seccion_2.setObjectName(u"pushButton_Borrar_seccion_2")
        self.pushButton_Borrar_seccion_2.setEnabled(False)
        self.pushButton_Borrar_seccion_2.setStyleSheet(u"background-color: rgb(204, 204, 204);")

        self.verticalLayout_11.addWidget(self.pushButton_Borrar_seccion_2)

        self.pushButtonRegresar_2 = QPushButton(self.frame_9)
        self.pushButtonRegresar_2.setObjectName(u"pushButtonRegresar_2")

        self.verticalLayout_11.addWidget(self.pushButtonRegresar_2)


        self.horizontalLayout_2.addWidget(self.frame_9)


        self.horizontalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_16)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(FormSecciones)

        QMetaObject.connectSlotsByName(FormSecciones)
    # setupUi

    def retranslateUi(self, FormSecciones):
        FormSecciones.setWindowTitle(QCoreApplication.translate("FormSecciones", u"Form", None))
        self.label.setText(QCoreApplication.translate("FormSecciones", u"LISTA DE SECCIONES", None))
        self.pushButtonCrear_Seccion_2.setText(QCoreApplication.translate("FormSecciones", u"Crear nueva seccion", None))
        self.pushButton_Ver_seccion_2.setText(QCoreApplication.translate("FormSecciones", u"Ver seccion", None))
        self.pushButton_Modificar_seccion_2.setText(QCoreApplication.translate("FormSecciones", u"Modificar seccion", None))
        self.pushButton_Archivar_seccion_2.setText(QCoreApplication.translate("FormSecciones", u"Archivar seccion", None))
        self.pushButton_Borrar_seccion_2.setText(QCoreApplication.translate("FormSecciones", u"Borrar seccion", None))
        self.pushButtonRegresar_2.setText(QCoreApplication.translate("FormSecciones", u"Home", None))
    # retranslateUi

