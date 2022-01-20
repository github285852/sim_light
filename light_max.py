from PySide6.QtCore import (QThread, Signal, QDateTime)
from ui_light_MAX import Ui_Dialog
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QColor

def set_led_color(widget,r,g,b):
    str_bgc = "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\nstop: 0 rgb(" + str(r) + "," + str(g) + "," + str(b) + "), stop: 1 #dadbde);\n"
    str_style = (
                             u"width:80px;\n"
                             "height:80px;\n"
                             "\n"
                             "border: 0px solid #000000;\n"
                             "border-radius: 40px;\n"
                             "")
    print(str_style+str_bgc)
    widget.setStyleSheet(str_style+str_bgc)

    # palette1 = widget.palette()
    # palette1.setColor(widget.backgroundRole(), 0xFF0000)
    # widget.setPalette(palette1)
    # widget.setText("Hello")
    #
    # widget.setAutoFillBackground(True)
    # self.led_1.set
    # self.led_1.setStyleSheet("background-color:purple")

class LightThread(QThread):
    #str 为字符串字典
    led_update = Signal(dict)#字典数据
    ledColor = {}

    def HsiOut(self,led,h,s,i):
        color = QColor(255, 255, 0)
        color.setHsvF(h, s, i)
        self.ledColor[led] = color
        self.led_update.emit(self.ledColor)

    def run(self):

        while True:
            self.HsiOut("led_1",0,1,0.9)
            self.sleep(1)

            self.HsiOut("led_2",0,1,0.8)
            self.sleep(1)

            self.HsiOut("led_3",0,1,0.7)
            self.sleep(1)

            self.HsiOut("led_4",0,1,0.6)
            self.sleep(1)

            self.HsiOut("led_5",0,1,0.5)
            self.sleep(1)

            self.HsiOut("led_6", 0, 1, 0.4)
            self.sleep(1)

            self.HsiOut("led_7",0,1,0.3)
            self.sleep(1)

            self.HsiOut("led_8",0,1,0.2)
            self.sleep(1)


class LightMax(QMainWindow):
    ui = Ui_Dialog()
    light = LightThread()

    def initUI(self):
        self.ui.setupUi(self)#不能放入 __init__ 这个实例还没初始化完成
        self.light.led_update.connect(self.LedHandle)

    def LedHandle(self,data):
        for key,vaule in data.items():
            self.setLedColor(key,vaule)
        # print(data)

    def showEvent(self,event):
        print("showEvent")
        self.light.start()

    def setLedColor(self,led="led_1",color=QColor(255,0,0)):
        r = color.red()  #强制转换
        g = color.green()
        b = color.blue()
        str_bgc = "background-color: rgb(" + str(r) + "," + str(g) + "," + str(b) + ");\n"
        # str_bgc = "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\nstop: 0 rgb(" + str(r) + "," + str(g) + "," + str(b) + "), stop: 1 #dadbde);\n"
        str_style = (

            )
        led_widget = eval("self.ui."+led)
        led_widget.setStyleSheet(str_style + str_bgc)

        # palette1 = led_widget.palette()
        # palette1.setColor(led_widget.backgroundRole(),color)
        # led_widget.setPalette(palette1)
        # led_widget.setAutoFillBackground(True)