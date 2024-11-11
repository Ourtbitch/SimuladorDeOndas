# main.py
from PyQt5 import QtWidgets
import sys
from simulador_ui import SimuladorOndaInterfaz

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SimuladorOndaInterfaz()
    window.show()
    sys.exit(app.exec_())