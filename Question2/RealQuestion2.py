import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from A_simple_paint_program import Ui_PaintProgram

class PaintProgram(QMainWindow):
    def __init__(self):
        super().__init__(self,None)

        self.ui = Ui_PaintProgram()
        self.ui.setupUi(self)

    
    def dragEnterEvent(self, event):
        pencil = QPaint()
        pencil.begin(self)

        pencil.setPen(QColor(0,0,0))
        pencil.setBrush(QColor(0,0,0))

        pencil.drawEllipse(event.pos().x(),event.pos().y(),2,2)

        pencil.show()


def main():
    a = QApplication(sys.argv)
    w = PaintProgram()
    w.show()
    return a.exec_()


if __name__ == "__main__":
    sys.exit(main())

