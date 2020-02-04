from PyQt5.QtWidgets import QApplication

import myMainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = myMainWindow.myMainWindow()
    mainwindow.show()

    sys.exit(app.exec_())
