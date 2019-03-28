import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from A_simple_paint_program import Ui_PaintProgram

class PaintProgram(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)

        self.ui = Ui_PaintProgram()
        self.ui.setupUi(self)
       
    def mousePressEvent(self, event):
        print("eee")
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([
            QPoint(70,100),QPoint(100,110),
            QPoint(130,100),QPoint(100,150)
        ])

        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(50,150,100,100,0,180*16)
        p.drawPolygon(
            [QPoint(50,200),QPoint(150,200),QPoint(100,400),]
        )
        p.end()


def main():
    a = QApplication(sys.argv)
    w = PaintProgram()
    w.show()
    return a.exec_()


if __name__ == "__main__":
    sys.exit(main())

