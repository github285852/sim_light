# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys

from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6 import QtCore,QtGui
from PySide6.QtGui import QColor

from light_max import LightMax

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.

import time

if __name__ == '__main__':
    print_hi('PyCharm')
    app = QApplication(sys.argv)
    # myw = QMainWindow()
    # LightMax(myw)
    # myw.show()
    lightMax = LightMax()
    lightMax.initUI()
    lightMax.show()
    sys.exit(app.exec())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

