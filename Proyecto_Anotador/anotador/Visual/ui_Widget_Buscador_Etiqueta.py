# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Widget_Buscador_Etiquetarvjqzf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WBuscador(object):
    def setupUi(self, WBuscador):
        if not WBuscador.objectName():
            WBuscador.setObjectName(u"WBuscador")
        WBuscador.resize(531, 390)
        self.verticalLayout = QVBoxLayout(WBuscador)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(WBuscador)
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
        self.frame_16.setStyleSheet(u"background-color: rgb(102, 101, 86);\n"
"background-color: rgb(0, 0, 0);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 4)
        self.frame_3 = QFrame(self.frame_16)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 252, 212);\n"
"background-color: rgb(74, 139, 218);\n"
"")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(74, 139, 218);")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButtonBuscarEtiqueta = QPushButton(self.frame_6)
        self.pushButtonBuscarEtiqueta.setObjectName(u"pushButtonBuscarEtiqueta")
        self.pushButtonBuscarEtiqueta.setStyleSheet(u"background-color: rgb(204, 204, 204);")

        self.gridLayout.addWidget(self.pushButtonBuscarEtiqueta, 0, 2, 1, 1)

        self.labelBusquedaetiqueta = QLabel(self.frame_6)
        self.labelBusquedaetiqueta.setObjectName(u"labelBusquedaetiqueta")

        self.gridLayout.addWidget(self.labelBusquedaetiqueta, 0, 0, 1, 1)

        self.lineEditEtiqueta = QLineEdit(self.frame_6)
        self.lineEditEtiqueta.setObjectName(u"lineEditEtiqueta")
        self.lineEditEtiqueta.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEditEtiqueta, 0, 1, 1, 1)

        self.labelbusquedafecha = QLabel(self.frame_6)
        self.labelbusquedafecha.setObjectName(u"labelbusquedafecha")

        self.gridLayout.addWidget(self.labelbusquedafecha, 1, 0, 1, 1)

        self.pushButtonBuscarFecha = QPushButton(self.frame_6)
        self.pushButtonBuscarFecha.setObjectName(u"pushButtonBuscarFecha")
        self.pushButtonBuscarFecha.setStyleSheet(u"background-color: rgb(204, 204, 204);")

        self.gridLayout.addWidget(self.pushButtonBuscarFecha, 1, 2, 1, 1)

        self.dateEdit = QDateEdit(self.frame_6)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"background-color: rgb(74, 139, 218);\n"
"selection-background-color: rgb(0, 170, 255);")
        self.dateEdit.setDateTime(QDateTime(QDate(2021, 1, 2), QTime(0, 0, 0)))
        self.dateEdit.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setDate(QDate(2021, 1, 2))

        self.gridLayout.addWidget(self.dateEdit, 1, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_6)

        self.listViewNotas = QListView(self.frame_5)
        self.listViewNotas.setObjectName(u"listViewNotas")
        self.listViewNotas.setStyleSheet(u"font: 12pt \"Lucida Handwriting\";")
        self.listViewNotas.setFrameShape(QFrame.NoFrame)
        self.listViewNotas.setFrameShadow(QFrame.Sunken)
        self.listViewNotas.setLineWidth(1)
        self.listViewNotas.setViewMode(QListView.IconMode)
        self.listViewNotas.setItemAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.listViewNotas)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_16)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 252, 212);")
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
        self.pushButton_Ver_Nota = QPushButton(self.frame_9)
        self.pushButton_Ver_Nota.setObjectName(u"pushButton_Ver_Nota")
        self.pushButton_Ver_Nota.setEnabled(False)
        self.pushButton_Ver_Nota.setStyleSheet(u"background-color: rgb(204, 204, 204);")

        self.verticalLayout_11.addWidget(self.pushButton_Ver_Nota)

        self.pushButton_Informe_Etiqueta_2 = QPushButton(self.frame_9)
        self.pushButton_Informe_Etiqueta_2.setObjectName(u"pushButton_Informe_Etiqueta_2")
        self.pushButton_Informe_Etiqueta_2.setEnabled(True)
        self.pushButton_Informe_Etiqueta_2.setStyleSheet(u"background-color: rgb(204, 204, 204);")

        self.verticalLayout_11.addWidget(self.pushButton_Informe_Etiqueta_2)

        self.pushButton_Notas_Destacadas_2 = QPushButton(self.frame_9)
        self.pushButton_Notas_Destacadas_2.setObjectName(u"pushButton_Notas_Destacadas_2")
        self.pushButton_Notas_Destacadas_2.setEnabled(True)
        self.pushButton_Notas_Destacadas_2.setStyleSheet(u"background-color: rgb(204, 204, 204);")

        self.verticalLayout_11.addWidget(self.pushButton_Notas_Destacadas_2)

        self.pushButton_Home = QPushButton(self.frame_9)
        self.pushButton_Home.setObjectName(u"pushButton_Home")
        self.pushButton_Home.setEnabled(True)
        self.pushButton_Home.setStyleSheet(u"background-color: rgb(204, 204, 204);")

        self.verticalLayout_11.addWidget(self.pushButton_Home)


        self.horizontalLayout_2.addWidget(self.frame_9)


        self.horizontalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_16)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(WBuscador)

        QMetaObject.connectSlotsByName(WBuscador)
    # setupUi

    def retranslateUi(self, WBuscador):
        WBuscador.setWindowTitle(QCoreApplication.translate("WBuscador", u"Form", None))
        self.pushButtonBuscarEtiqueta.setText(QCoreApplication.translate("WBuscador", u"Buscar", None))
        self.labelBusquedaetiqueta.setText(QCoreApplication.translate("WBuscador", u"Busqueda por etiqueta", None))
        self.lineEditEtiqueta.setPlaceholderText(QCoreApplication.translate("WBuscador", u"Ingrese etiqueta a buscar", None))
        self.labelbusquedafecha.setText(QCoreApplication.translate("WBuscador", u"Busqueda por fecha", None))
        self.pushButtonBuscarFecha.setText(QCoreApplication.translate("WBuscador", u"Buscar", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("WBuscador", u"dd/MM/yyyy", None))
        self.pushButton_Ver_Nota.setText(QCoreApplication.translate("WBuscador", u"Ver nota", None))
        self.pushButton_Informe_Etiqueta_2.setText(QCoreApplication.translate("WBuscador", u"Informe etiqueta", None))
        self.pushButton_Notas_Destacadas_2.setText(QCoreApplication.translate("WBuscador", u"Notas destacadas", None))
        self.pushButton_Home.setText(QCoreApplication.translate("WBuscador", u"Home", None))
    # retranslateUi

