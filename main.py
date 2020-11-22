import sys
import random
from PyQt5 import uic
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QColor, QPainter, QPolygon
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

SCREEN_SIZE = [400, 400]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.btn.clicked.connect(self.p)
        self.mouse_x = 0
        self.mouse_y = 0
        self.dopaint = False

    def p(self):
        self.mouse_y = random.randint(0, 400)
        self.mouse_x = random.randint(0, 400)
        self.dopaint = True
        self.repaint()

    def paintEvent(self, event):
        if self.dopaint:
            qp = QPainter()
            qp.begin(self)
            s = random.randint(20, 110)
            qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            qp.drawEllipse(self.mouse_x - s // 2, self.mouse_y - s // 2, s, s)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
