# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Widget_Notas_DestacadasWphrpa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WNotas_Destacadas(object):
    def setupUi(self, WNotas_Destacadas):
        if not WNotas_Destacadas.objectName():
            WNotas_Destacadas.setObjectName(u"WNotas_Destacadas")
        WNotas_Destacadas.resize(547, 422)
        self.verticalLayout = QVBoxLayout(WNotas_Destacadas)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(WNotas_Destacadas)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
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
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 252, 212);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(74, 139, 218);\n"
"")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 40))
        self.frame_8.setStyleSheet(u"background-color: rgb(74, 139, 218);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(6, 7, 5, 4)
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout_12.addWidget(self.label)


        self.verticalLayout_9.addWidget(self.frame_8)

        self.pushButtonBuscar = QPushButton(self.frame_5)
        self.pushButtonBuscar.setObjectName(u"pushButtonBuscar")
        self.pushButtonBuscar.setStyleSheet(u"background-color: rgb(204, 204, 204);")

        self.verticalLayout_9.addWidget(self.pushButtonBuscar)

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
        self.frame_9.setStyleSheet(u"background-color: rgb(74, 139, 218);")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButton_Ver_Nota = QPushButton(self.frame_9)
        self.pushButton_Ver_Nota.setObjectName(u"pushButton_Ver_Nota")
        self.pushButton_Ver_Nota.setEnabled(False)
        self.pushButton_Ver_Nota.setStyleSheet(u"background-color: rgb(204, 204, 204);")

        self.verticalLayout_11.addWidget(self.pushButton_Ver_Nota)

        self.pushButton_Buscar_Nota = QPushButton(self.frame_9)
        self.pushButton_Buscar_Nota.setObjectName(u"pushButton_Buscar_Nota")
        self.pushButton_Buscar_Nota.setEnabled(True)
        self.pushButton_Buscar_Nota.setStyleSheet(u"background-color: rgb(204, 204, 204);")

        self.verticalLayout_11.addWidget(self.pushButton_Buscar_Nota)

        self.pushButton_Informe_Etiqueta = QPushButton(self.frame_9)
        self.pushButton_Informe_Etiqueta.setObjectName(u"pushButton_Informe_Etiqueta")
        self.pushButton_Informe_Etiqueta.setEnabled(True)
        self.pushButton_Informe_Etiqueta.setStyleSheet(u"background-color: rgb(204, 204, 204);")

        self.verticalLayout_11.addWidget(self.pushButton_Informe_Etiqueta)

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


        self.retranslateUi(WNotas_Destacadas)

        QMetaObject.connectSlotsByName(WNotas_Destacadas)
    # setupUi

    def retranslateUi(self, WNotas_Destacadas):
        WNotas_Destacadas.setWindowTitle(QCoreApplication.translate("WNotas_Destacadas", u"Form", None))
        self.label.setText(QCoreApplication.translate("WNotas_Destacadas", u"NOTAS DESTACADAS", None))
        self.pushButtonBuscar.setText(QCoreApplication.translate("WNotas_Destacadas", u"Buscar", None))
        self.pushButton_Ver_Nota.setText(QCoreApplication.translate("WNotas_Destacadas", u"Ver nota", None))
        self.pushButton_Buscar_Nota.setText(QCoreApplication.translate("WNotas_Destacadas", u"Buscar nota", None))
        self.pushButton_Informe_Etiqueta.setText(QCoreApplication.translate("WNotas_Destacadas", u"informe etiqueta", None))
        self.pushButton_Home.setText(QCoreApplication.translate("WNotas_Destacadas", u"Home", None))
    # retranslateUi

