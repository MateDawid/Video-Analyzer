import sys
from PyQt5.QtWidgets import QApplication
from Menu import Menu


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Menu()
    main.setGeometry(100, 100, 300, 300)
    main.show()
    sys.exit(app.exec_())


