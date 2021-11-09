# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialogo_Nombrar_LibroDdBepQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_Nombrar_Libro(object):
    def setupUi(self, Dialog_Nombrar_Libro):
        if not Dialog_Nombrar_Libro.objectName():
            Dialog_Nombrar_Libro.setObjectName(u"Dialog_Nombrar_Libro")
        Dialog_Nombrar_Libro.resize(413, 125)
        self.verticalLayout = QVBoxLayout(Dialog_Nombrar_Libro)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog_Nombrar_Libro)
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
        self.frame_16.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_16)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 252, 212);\n"
"border-color: rgb(255, 255, 255);")
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
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 191, 21))
        self.label.setStyleSheet(u"font: 25 12pt \"Yu Gothic UI Light\";")
        self.lineEditTitulo = QLineEdit(self.frame_6)
        self.lineEditTitulo.setObjectName(u"lineEditTitulo")
        self.lineEditTitulo.setGeometry(QRect(10, 50, 461, 19))

        self.horizontalLayout_3.addWidget(self.frame_6)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame_16)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStyleSheet(u"background-color: rgb(204, 204, 204);")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout_5.addWidget(self.buttonBox)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog_Nombrar_Libro)
        self.buttonBox.accepted.connect(Dialog_Nombrar_Libro.accept)
        self.buttonBox.rejected.connect(Dialog_Nombrar_Libro.reject)

        QMetaObject.connectSlotsByName(Dialog_Nombrar_Libro)
    # setupUi

    def retranslateUi(self, Dialog_Nombrar_Libro):
        Dialog_Nombrar_Libro.setWindowTitle(QCoreApplication.translate("Dialog_Nombrar_Libro", u"A\u00f1adir ", None))
        self.label.setText(QCoreApplication.translate("Dialog_Nombrar_Libro", u"Ingrese nombre nuevo libro", None))
        self.lineEditTitulo.setInputMask("")
        self.lineEditTitulo.setPlaceholderText(QCoreApplication.translate("Dialog_Nombrar_Libro", u"Titulo libro", None))
    # retranslateUi

