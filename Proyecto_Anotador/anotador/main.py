import sys

from PySide2.QtWidgets import QApplication

from Proyecto_Anotador.anotador.Mundo.mundo import Anotador
from Proyecto_Anotador.anotador.Visual.gui.gui import Ventana

if __name__ == "__main__":
    anotador=Anotador()
    app = QApplication(sys.argv)
    window = Ventana(anotador)
    window.setWindowTitle("Anotador")
    window.setMinimumSize(1000,600)
    sys.exit(app.exec_())