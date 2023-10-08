import sys

from PyQt5 import QtGui, QtCore, uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore    import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )
        self.setGeometry(0, 0, 2256, 1530)
        self.label = QLabel(self)
        self.pixmap = QPixmap('crack3.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(2256, 1550)
        self.setCursor(Qt.BlankCursor) 
 


    # destroy window if pressed
    def mousePressEvent(self, event):
        QtWidgets.qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.setWindowOpacity(0.7)
    mywindow.show()
    app.exec_()