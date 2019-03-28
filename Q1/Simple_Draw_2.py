import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from Bright_drawing import Simple_drawing_window


class Simple_drawing_window2(Simple_drawing_window):
    def __init__(self):
        super().__init__()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 0, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawPie(50, 150, 100, 100, 0, 180 * 16)
        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()


def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window2()
    w.show()

    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())