# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6 import QtCore,QtGui
from PySide6.QtGui import QColor

from light_MAX import Ui_Dialog

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def set_led_color(widget,r,g,b):
    str2 = ""
    str_style = (u"border: 2px solid #8f8f91;\n" 
                 "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                             "                            stop: 0 #f6f700, stop: 1 #dadbde);\n"
                             "width:80px;\n"
                             "height:80px;\n"
                             "\n"
                             "border: 0px solid #e4007e;\n"
                             "border-radius: 40px;\n"
                             "text-align: center;\n"
                             "")
    widget.setStyleSheet(str_style)

    # palette1 = widget.palette()
    # palette1.setColor(widget.backgroundRole(), 0xFF0000)
    # widget.setPalette(palette1)
    # widget.setText("Hello")
    #
    # widget.setAutoFillBackground(True)
    # self.led_1.set
    # self.led_1.setStyleSheet("background-color:purple")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    app = QApplication(sys.argv)
    myw = QMainWindow()
    dialog = Ui_Dialog()
    dialog.setupUi(myw)
    myw.show()
    set_led_color(dialog.led_3,0,255,0)
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

