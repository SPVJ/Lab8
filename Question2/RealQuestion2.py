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
        self.x = []
        self.y = []
        self.ui.bt_clear.clicked.connect(self.clear)

    def clear(self):
        self.x = []
        self.y = []
        self.update()

 
    def mouseMoveEvent(self,event):
        self.x.append(event.pos().x())
        self.y.append(event.pos().y())
        self.update()

        
    def paintEvent(self,ev):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        for i in range(len(self.x)):
            p.drawEllipse(self.x[i],self.y[i],5,5)

        p.end()


def main():
    a = QApplication(sys.argv)
    w = PaintProgram()
    w.show()
    return a.exec_()


if __name__ == "__main__":
    sys.exit(main())

