from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QToolTip, QMessageBox, QDesktopWidget
import helloworld
import sys


class myMainWindow(QtWidgets.QMainWindow, helloworld.Ui_Form):
    def __init__(self, parent=None):
        super(myMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('hello')
        self.setWindowIcon(QIcon('res/hello.png'))
        self.setGeometry(300, 300, 300, 220)
        self.center()
        # 信号槽绑定
        self.pushButton.clicked.connect(self.showLabel)

    def showLabel(self):
        self.label.setText("waht")
        print("what")

    def center(self):
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #重写了closeEvent 事件
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()