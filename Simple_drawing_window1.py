import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from Bright_drawing import Simple_drawing_window

class Simple_drawing_window1(Simple_drawing_window):
    def __init__(self):
        super().__init__()
    
    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([QPoint(50,200),QPoint(150,200),QPoint(100,0),])

       
        p.drawPolygon(
            [QPoint(50,200),QPoint(150,200),QPoint(100,400),]
        )
        p.drawPixmap(QRect(200,100,320,320),self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)

    w= Simple_drawing_window1()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())