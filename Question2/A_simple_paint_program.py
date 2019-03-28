# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'A_simple_paint_program.ui',
# licensing of 'A_simple_paint_program.ui' applies.
#
# Created: Thu Mar 28 13:53:16 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_PaintProgram(object):
    def setupUi(self, PaintProgram):
        PaintProgram.setObjectName("PaintProgram")
        PaintProgram.resize(364, 304)
        self.bt_clear = QtWidgets.QPushButton(PaintProgram)
        self.bt_clear.setGeometry(QtCore.QRect(80, 270, 181, 21))
        self.bt_clear.setObjectName("bt_clear")
        self.label = QtWidgets.QLabel(PaintProgram)
        self.label.setGeometry(QtCore.QRect(60, 240, 211, 21))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(PaintProgram)
        self.frame.setGeometry(QtCore.QRect(10, 10, 341, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.retranslateUi(PaintProgram)
        QtCore.QMetaObject.connectSlotsByName(PaintProgram)

    def retranslateUi(self, PaintProgram):
        PaintProgram.setWindowTitle(QtWidgets.QApplication.translate("PaintProgram", "Form", None, -1))
        self.bt_clear.setText(QtWidgets.QApplication.translate("PaintProgram", "Clear", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("PaintProgram", "Drag the mouse to draw", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PaintProgram = QtWidgets.QWidget()
    ui = Ui_PaintProgram()
    ui.setupUi(PaintProgram)
    PaintProgram.show()
    sys.exit(app.exec_())

