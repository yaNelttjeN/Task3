import random

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import sys
from PyQt5 import uic, QtWidgets, QtCore


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.squares = 3
        self.offset = 130
        self.max_dim = 120
        self.min_dim = 30
        self.flag = False
        self.pushButton.clicked.connect(self.draw)

    def setup_ui(self):
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(455, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Нарисовать"))

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            for i in range(self.squares):
                self.paint_circle(painter, i)
        self.flag = False

    def paint_circle(self, painter: QPainter, time):
        painter.setPen(QColor(*random_color()))
        x, y = 60 + (time * self.offset), 60
        w = h = int(random.randint(self.min_dim, self.max_dim) // 2)
        painter.drawEllipse(x, y, w, h)


def random_color():
    return tuple([random.randint(0, 255) for _ in range(3)])


def except_hook(a, b, c):
    sys.__excepthook__(a, b, c)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    f = Window()
    f.show()
    sys.exit(app.exec_())



