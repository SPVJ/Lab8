from bill_drawing import Simple_drawing_window_v3
from Simple_drawing_window1 import Simple_drawing_window1
from Simple_Draw_2 import Simple_drawing_window2
import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

def main():
    app = QApplication()

    w = Simple_drawing_window1()
    w2 = Simple_drawing_window2()
    w3 = Simple_drawing_window_v3()

    w.show()
    w2.show()
    w3.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())