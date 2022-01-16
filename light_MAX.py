# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'light_MAX.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(659, 536)
        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(70, 80, 426, 426))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.led_1 = QPushButton(self.gridLayoutWidget)
        self.led_1.setObjectName(u"led_1")
        self.led_1.setStyleSheet(u"border: 2px solid #8f8f91;\n"
"/*\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                            stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"*/\n"
"/*background-color:rgb(255, 89, 255);*/\n"
"width:80px;\n"
"height:80px;\n"
"\n"
"border: 2px solid rgb(170, 255, 0);\n"
"border-radius: 40px;\n"
"text-align: center;\n"
"")

        self.gridLayout.addWidget(self.led_1, 0, 0, 1, 1)

        self.led_4 = QPushButton(self.gridLayoutWidget)
        self.led_4.setObjectName(u"led_4")
        self.led_4.setStyleSheet(u"border: 2px solid #8f8f91;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                            stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"width:80px;\n"
"height:80px;\n"
"\n"
"border: 0px solid #e4007e;\n"
"border-radius: 40px;\n"
"text-align: center;\n"
"")

        self.gridLayout.addWidget(self.led_4, 2, 0, 1, 1)

        self.led_5 = QPushButton(self.gridLayoutWidget)
        self.led_5.setObjectName(u"led_5")
        self.led_5.setStyleSheet(u"border: 2px solid #8f8f91;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                            stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"width:80px;\n"
"height:80px;\n"
"\n"
"border: 0px solid #e4007e;\n"
"border-radius: 40px;\n"
"text-align: center;\n"
"")

        self.gridLayout.addWidget(self.led_5, 2, 2, 1, 1)

        self.led_7 = QPushButton(self.gridLayoutWidget)
        self.led_7.setObjectName(u"led_7")
        self.led_7.setStyleSheet(u"border: 2px solid #8f8f91;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                            stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"width:80px;\n"
"height:80px;\n"
"\n"
"border: 0px solid #e4007e;\n"
"border-radius: 40px;\n"
"text-align: center;\n"
"")

        self.gridLayout.addWidget(self.led_7, 4, 0, 1, 1)

        self.led_2 = QPushButton(self.gridLayoutWidget)
        self.led_2.setObjectName(u"led_2")
        self.led_2.setStyleSheet(u"border: 2px solid #8f8f91;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                            stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"width:80px;\n"
"height:80px;\n"
"\n"
"border: 0px solid #e4007e;\n"
"border-radius: 40px;\n"
"text-align: center;\n"
"")

        self.gridLayout.addWidget(self.led_2, 0, 2, 1, 1)

        self.led_9 = QPushButton(self.gridLayoutWidget)
        self.led_9.setObjectName(u"led_9")
        self.led_9.setStyleSheet(u"border: 2px solid #8f8f91;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                            stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"width:80px;\n"
"height:80px;\n"
"\n"
"border: 0px solid #e4007e;\n"
"border-radius: 40px;\n"
"text-align: center;\n"
"")

        self.gridLayout.addWidget(self.led_9, 4, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.led_6 = QPushButton(self.gridLayoutWidget)
        self.led_6.setObjectName(u"led_6")
        self.led_6.setStyleSheet(u"border: 2px solid #8f8f91;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                            stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"width:80px;\n"
"height:80px;\n"
"\n"
"border: 0px solid #e4007e;\n"
"border-radius: 40px;\n"
"text-align: center;\n"
"")

        self.gridLayout.addWidget(self.led_6, 2, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.led_8 = QPushButton(self.gridLayoutWidget)
        self.led_8.setObjectName(u"led_8")
        self.led_8.setStyleSheet(u"border: 2px solid #8f8f91;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                            stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"width:80px;\n"
"height:80px;\n"
"\n"
"border: 0px solid #e4007e;\n"
"border-radius: 40px;\n"
"text-align: center;\n"
"")

        self.gridLayout.addWidget(self.led_8, 4, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.led_3 = QLabel(self.gridLayoutWidget)
        self.led_3.setObjectName(u"led_3")
        self.led_3.setStyleSheet(u"border: 2px solid #8f8f91;\n"
"/*\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                            stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"*/\n"
"background-color:rgb(255, 89, 255);\n"
"width:80px;\n"
"height:80px;\n"
"\n"
"border: 2px solid rgb(170, 255, 0);\n"
"border-radius: 40px;\n"
"text-align: center;")

        self.gridLayout.addWidget(self.led_3, 0, 4, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.led_1.setText("")
        self.led_4.setText("")
        self.led_5.setText("")
        self.led_7.setText("")
        self.led_2.setText("")
        self.led_9.setText("")
        self.led_6.setText("")
        self.led_8.setText("")
        self.led_3.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi

