# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialogo_Crear_notaWZciXc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialogo_Crear_Nota(object):
    def setupUi(self, Dialogo_Crear_Nota):
        if not Dialogo_Crear_Nota.objectName():
            Dialogo_Crear_Nota.setObjectName(u"Dialogo_Crear_Nota")
        Dialogo_Crear_Nota.resize(540, 243)
        self.verticalLayout = QVBoxLayout(Dialogo_Crear_Nota)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialogo_Crear_Nota)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(32, 42, 84);\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 4)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(9, 1, 9, 9)
        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background-color: rgb(102, 101, 86);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_16)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Yu Gothic UI Semibold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 63 11pt \"Yu Gothic UI Semibold\";")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEditTitulo = QLineEdit(self.frame_6)
        self.lineEditTitulo.setObjectName(u"lineEditTitulo")

        self.gridLayout.addWidget(self.lineEditTitulo, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 12pt \"Lucida Handwriting\";\n"
"font: 63 11pt \"Yu Gothic UI Semibold\";")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEditEtiqueta = QLineEdit(self.frame_6)
        self.lineEditEtiqueta.setObjectName(u"lineEditEtiqueta")

        self.gridLayout.addWidget(self.lineEditEtiqueta, 1, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_6)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame_16)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(Dialogo_Crear_Nota)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialogo_Crear_Nota)
        self.buttonBox.accepted.connect(Dialogo_Crear_Nota.accept)
        self.buttonBox.rejected.connect(Dialogo_Crear_Nota.reject)

        QMetaObject.connectSlotsByName(Dialogo_Crear_Nota)
    # setupUi

    def retranslateUi(self, Dialogo_Crear_Nota):
        Dialogo_Crear_Nota.setWindowTitle(QCoreApplication.translate("Dialogo_Crear_Nota", u"A\u00f1adir ", None))
        self.label.setText(QCoreApplication.translate("Dialogo_Crear_Nota", u"Titulo: ", None))
        self.lineEditTitulo.setInputMask("")
        self.lineEditTitulo.setPlaceholderText(QCoreApplication.translate("Dialogo_Crear_Nota", u"Ingrese titulo", None))
        self.label_2.setText(QCoreApplication.translate("Dialogo_Crear_Nota", u"Etiqueta:", None))
        self.lineEditEtiqueta.setInputMask("")
        self.lineEditEtiqueta.setPlaceholderText(QCoreApplication.translate("Dialogo_Crear_Nota", u"Ingrese etiqueta ", None))
    # retranslateUi

