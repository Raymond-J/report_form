# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 450))
        MainWindow.setMaximumSize(QtCore.QSize(800, 450))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("border-style:none;")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 421, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_0 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("方正本墨悦亦体 简")
        font.setPointSize(16)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_0.setStyleSheet("QPushButton {color:white;border-style:none;}\n"
"QPushButton:hover { background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(91, 91, 91, 255), stop:1 rgba(255, 255, 255, 255)) }\n"
"QPushButton:checked{background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(91, 91, 91, 255), stop:1 rgba(255, 255, 255, 255)); }")
        self.pushButton_0.setCheckable(True)
        self.pushButton_0.setAutoExclusive(True)
        self.pushButton_0.setObjectName("pushButton_0")
        self.horizontalLayout.addWidget(self.pushButton_0)
        self.pushButton_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("方正本墨悦亦体 简")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1.setStyleSheet("QPushButton {color:white;border-style:none;}\n"
"QPushButton:hover { background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(91, 91, 91, 255), stop:1 rgba(255, 255, 255, 255)) }\n"
"QPushButton:checked{background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(91, 91, 91, 255), stop:1 rgba(255, 255, 255, 255)); }")
        self.pushButton_1.setCheckable(True)
        self.pushButton_1.setAutoExclusive(True)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("方正本墨悦亦体 简")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {color:white;border-style:none;}\n"
"QPushButton:hover { background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(91, 91, 91, 255), stop:1 rgba(255, 255, 255, 255)) }\n"
"QPushButton:checked{background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(91, 91, 91, 255), stop:1 rgba(255, 255, 255, 255)); }")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("方正本墨悦亦体 简")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {color:white;border-style:none;}\n"
"QPushButton:hover { background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(91, 91, 91, 255), stop:1 rgba(255, 255, 255, 255)) }\n"
"QPushButton:checked{background-color:qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(91, 91, 91, 255), stop:1 rgba(255, 255, 255, 255)); }")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 0, 800, 41))
        self.line_2.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(91, 91, 91, 255));")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 40, 801, 411))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("方正本墨悦亦体 简")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("border-image:url(E:/三维表/qq2.png)")
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.label = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label.setGeometry(QtCore.QRect(50, 220, 141, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MJNgai PRC Medium")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"boeder-style:none;\n"
"background-color: transparent;\n"
"border-image:none")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label_2.setGeometry(QtCore.QRect(230, 220, 151, 91))
        font = QtGui.QFont()
        font.setFamily("MJNgai PRC Medium")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"boeder-style:none;\n"
"background-color: transparent;\n"
"border-image:none")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label_3.setGeometry(QtCore.QRect(430, 220, 121, 91))
        font = QtGui.QFont()
        font.setFamily("MJNgai PRC Medium")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"boeder-style:none;\n"
"background-color: transparent;\n"
"border-image:none")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_02 = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.pushButton_02.setGeometry(QtCore.QRect(250, 80, 100, 100))
        self.pushButton_02.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_02.setStyleSheet("border-image:url(E:/三维表/2.png)")
        self.pushButton_02.setText("")
        self.pushButton_02.setCheckable(True)
        self.pushButton_02.setAutoExclusive(True)
        self.pushButton_02.setFlat(True)
        self.pushButton_02.setObjectName("pushButton_02")
        self.pushButton_01 = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.pushButton_01.setGeometry(QtCore.QRect(70, 80, 100, 100))
        self.pushButton_01.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_01.setStyleSheet("border-image:url(E:/三维表/1.png)")
        self.pushButton_01.setText("")
        self.pushButton_01.setCheckable(True)
        self.pushButton_01.setAutoExclusive(True)
        self.pushButton_01.setObjectName("pushButton_01")
        self.pushButton_03 = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.pushButton_03.setGeometry(QtCore.QRect(440, 80, 100, 100))
        self.pushButton_03.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_03.setStyleSheet("border-image:url(E:/三维表/3.png)")
        self.pushButton_03.setText("")
        self.pushButton_03.setCheckable(True)
        self.pushButton_03.setAutoExclusive(False)
        self.pushButton_03.setObjectName("pushButton_03")
        self.label_4 = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label_4.setGeometry(QtCore.QRect(610, 220, 121, 91))
        font = QtGui.QFont()
        font.setFamily("MJNgai PRC Medium")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"boeder-style:none;\n"
"background-color: transparent;\n"
"border-image:none")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_04 = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.pushButton_04.setGeometry(QtCore.QRect(620, 80, 100, 100))
        self.pushButton_04.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_04.setStyleSheet("border-image:url(E:/三维表/4.png)")
        self.pushButton_04.setText("")
        self.pushButton_04.setCheckable(True)
        self.pushButton_04.setAutoExclusive(True)
        self.pushButton_04.setFlat(True)
        self.pushButton_04.setObjectName("pushButton_04")
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.page = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.page.setObjectName("page")
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(80, 40, 351, 71))
        self.label_11.setStyleSheet("border-image:url(E:/三维表/STWG2/2.png);\n"
"background-color: transparent")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(80, 130, 411, 71))
        self.label_12.setStyleSheet("border-image:url(E:/三维表/STWG2/3.png);\n"
"background-color: transparent")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setGeometry(QtCore.QRect(80, 220, 461, 71))
        self.label_13.setStyleSheet("border-image:url(E:/三维表/STWG2/1.png);\n"
"background-color: transparent")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setGeometry(QtCore.QRect(80, 310, 561, 71))
        self.label_14.setStyleSheet("border-image:url(E:/三维表/STWG2/4.png);\n"
"background-color: transparent")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_11.setGeometry(QtCore.QRect(252, 49, 151, 41))
        font = QtGui.QFont()
        font.setFamily("方正本墨悦亦体 简")
        font.setPointSize(18)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("background-color: transparent;\n"
"border-image:none")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_14.setGeometry(QtCore.QRect(250, 140, 211, 41))
        font = QtGui.QFont()
        font.setFamily("方正本墨悦亦体 简")
        font.setPointSize(18)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setStyleSheet("background-color: transparent;\n"
"border-image:none")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_15.setGeometry(QtCore.QRect(250, 230, 261, 41))
        font = QtGui.QFont()
        font.setFamily("方正本墨悦亦体 简")
        font.setPointSize(18)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setStyleSheet("background-color: transparent;\n"
"border-image:none")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_16.setGeometry(QtCore.QRect(250, 320, 361, 41))
        font = QtGui.QFont()
        font.setFamily("方正本墨悦亦体 简")
        font.setPointSize(18)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setStyleSheet("background-color: transparent;\n"
"border-image:none")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(620, 230, 81, 81))
        self.label_5.setStyleSheet("border-image:url(E:/三维表/STWG2/5.png);\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(670, 290, 121, 21))
        font = QtGui.QFont()
        font.setFamily("方正静蕾简体")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("\n"
"border-image:none;\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.listWidget = QtWidgets.QListWidget(self.page)
        self.listWidget.setGeometry(QtCore.QRect(540, 160, 241, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("\n"
"QListWidget{background-color: rgb(255, 255, 255, 40%);border-image:none}\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.page_2)
        self.listWidget_2.setGeometry(QtCore.QRect(510, 50, 261, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("QListWidget:Item{padding-bottom:-10px}\n"
"QListWidget{background-color: rgb(255, 255, 255, 40%);border-image:none;}\n"
"\n"
"")
        self.listWidget_2.setGridSize(QtCore.QSize(0, 50))
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(510, 360, 261, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.pushButton_21 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setStyleSheet("QPushButton {background-color: rgb(255, 255, 255, 70%);\n"
"image:url(E:/三维表/STWG3/B21.png);border-image:none;}\n"
"QPushButton:hover { border-image:none;background-color: rgb(255, 255, 255, 40%);}\n"
"")
        self.pushButton_21.setText("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_21.addWidget(self.pushButton_21)
        self.pushButton_22 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_22.setStyleSheet("QPushButton {background-color: rgb(255, 255, 255, 70%);\n"
"image:url(E:/三维表/STWG3/B22.png);border-image:none;}\n"
"QPushButton:hover { border-image:none;background-color: rgb(255, 255, 255, 40%);}\n"
"")
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout_21.addWidget(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_23.setStyleSheet("QPushButton {background-color: rgb(255, 255, 255, 70%);\n"
"image:url(E:/三维表/STWG3/B23.png);border-image:none;}\n"
"QPushButton:hover { border-image:none;background-color: rgb(255, 255, 255, 40%);}\n"
"")
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout_21.addWidget(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy)
        self.pushButton_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_24.setStyleSheet("QPushButton {background-color: rgb(255, 255, 255, 70%);\n"
"image:url(E:/三维表/STWG3/B24.png);border-image:none;}\n"
"QPushButton:hover { border-image:none;background-color: rgb(255, 255, 255, 40%);}\n"
"")
        self.pushButton_24.setText("")
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_21.addWidget(self.pushButton_24)
        self.label_21 = QtWidgets.QLabel(self.page_2)
        self.label_21.setGeometry(QtCore.QRect(30, 30, 451, 51))
        self.label_21.setStyleSheet("border-image:url(E:/三维表/STWG3/L21.png);\n"
"background-color: transparent")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.page_2)
        self.label_22.setGeometry(QtCore.QRect(30, 100, 261, 51))
        self.label_22.setStyleSheet("border-image:url(E:/三维表/STWG3/L22.png);\n"
"background-color: transparent")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_21.setGeometry(QtCore.QRect(140, 38, 311, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setStyleSheet("background-color: transparent;\n"
"border-image:none")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.listWidget_3 = QtWidgets.QListWidget(self.page_2)
        self.listWidget_3.setGeometry(QtCore.QRect(134, 70, 331, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.listWidget_3.setFont(font)
        self.listWidget_3.setStyleSheet("\n"
"QListWidget{background-color: rgb(255, 255, 255);border-image:none;}\n"
"\n"
"")
        self.listWidget_3.setObjectName("listWidget_3")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(510, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("方正本墨悦亦体 简")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255, 70%);\n"
"border-image:none;\n"
"background-repeat: no-repeat;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_25 = QtWidgets.QLabel(self.page_2)
        self.label_25.setGeometry(QtCore.QRect(270, 170, 221, 51))
        self.label_25.setStyleSheet("border-image:url(E:/三维表/STWG3/L25.png);\n"
"background-color: transparent")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.page_2)
        self.label_26.setGeometry(QtCore.QRect(30, 240, 221, 51))
        self.label_26.setStyleSheet("border-image:url(E:/三维表/STWG3/L26.png);\n"
"background-color: transparent")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.label_24 = QtWidgets.QLabel(self.page_2)
        self.label_24.setGeometry(QtCore.QRect(30, 170, 221, 51))
        self.label_24.setStyleSheet("border-image:url(E:/三维表/STWG3/L24.png);\n"
"background-color: transparent")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.label_23 = QtWidgets.QLabel(self.page_2)
        self.label_23.setGeometry(QtCore.QRect(310, 100, 181, 51))
        self.label_23.setStyleSheet("border-image:url(E:/三维表/STWG3/L23.png);\n"
"background-color: transparent")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_27 = QtWidgets.QLabel(self.page_2)
        self.label_27.setGeometry(QtCore.QRect(270, 240, 221, 51))
        self.label_27.setStyleSheet("border-image:url(E:/三维表/STWG3/L27.png);\n"
"background-color: transparent")
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_23.setGeometry(QtCore.QRect(430, 110, 41, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setStyleSheet("background-color: transparent;\n"
"border-image:none")
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_24.setGeometry(QtCore.QRect(190, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_24.setFont(font)
        self.lineEdit_24.setStyleSheet("background-color: transparent;\n"
"border-image:none")
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_25.setGeometry(QtCore.QRect(430, 180, 41, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_25.setFont(font)
        self.lineEdit_25.setStyleSheet("background-color: transparent;\n"
"border-image:none")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_26.setGeometry(QtCore.QRect(190, 250, 41, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_26.setFont(font)
        self.lineEdit_26.setStyleSheet("background-color: transparent;\n"
"border-image:none")
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_27.setGeometry(QtCore.QRect(430, 250, 31, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_27.setFont(font)
        self.lineEdit_27.setStyleSheet("background-color: transparent;\n"
"border-image:none")
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.pushButton_25 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_25.setGeometry(QtCore.QRect(110, 320, 120, 49))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy)
        self.pushButton_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_25.setStyleSheet("QPushButton{border-image:url(E:/三维表/STWG3/B25.png);}")
        self.pushButton_25.setText("")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_26.setGeometry(QtCore.QRect(300, 320, 121, 49))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy)
        self.pushButton_26.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_26.setStyleSheet("QPushButton{border-image:url(E:/三维表/STWG3/B26.png);}\n"
"QPushButton:checked{border-image:url(E:/三位表/STWG3/B26_P.png); }")
        self.pushButton_26.setText("")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_27.setGeometry(QtCore.QRect(40, 320, 120, 49))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy)
        self.pushButton_27.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_27.setStyleSheet("border-image:url(E:/三维表/STWG3/B27.png);")
        self.pushButton_27.setText("")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_28.setGeometry(QtCore.QRect(200, 320, 121, 49))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy)
        self.pushButton_28.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_28.setStyleSheet("border-image:url(E:/三维表/STWG3/B28.png);")
        self.pushButton_28.setText("")
        self.pushButton_28.setObjectName("pushButton_28")
        self.lineEdit_22 = QtWidgets.QDateEdit(self.page_2)
        self.lineEdit_22.setGeometry(QtCore.QRect(140, 110, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setStyleSheet("QDateEdit{background-color: transparent;border-image:none}\n"
"")
        self.lineEdit_22.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.pushButton_29 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_29.setGeometry(QtCore.QRect(360, 320, 121, 51))
        self.pushButton_29.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_29.setStyleSheet("border-image:url(E:/三维表/STWG3/B29.png);")
        self.pushButton_29.setText("")
        self.pushButton_29.setObjectName("pushButton_29")
        self.listWidget_2.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.lineEdit_21.raise_()
        self.label_8.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_24.raise_()
        self.label_23.raise_()
        self.label_27.raise_()
        self.lineEdit_23.raise_()
        self.lineEdit_24.raise_()
        self.lineEdit_25.raise_()
        self.lineEdit_26.raise_()
        self.lineEdit_27.raise_()
        self.pushButton_25.raise_()
        self.pushButton_26.raise_()
        self.pushButton_27.raise_()
        self.pushButton_28.raise_()
        self.lineEdit_22.raise_()
        self.listWidget_3.raise_()
        self.pushButton_29.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.line_2.raise_()
        self.horizontalLayoutWidget.raise_()
        self.stackedWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_0.setText(_translate("MainWindow", "首  页"))
        self.pushButton_1.setText(_translate("MainWindow", "基本信息"))
        self.pushButton_2.setText(_translate("MainWindow", "检查情况"))
        self.pushButton_3.setText(_translate("MainWindow", "表单管理"))
        self.label.setText(_translate("MainWindow", "基本信息的录入\n"
"填报时间\n"
"填报到位的名称\n"
"填报时间等"))
        self.label_2.setText(_translate("MainWindow", "检查情况的录入\n"
"被查企业名称\n"
"检查的时间人次\n"
"隐患数量等"))
        self.label_3.setText(_translate("MainWindow", "表单文件管理\n"
"打开保存表单\n"
"整合导入导出\n"
"生成工作表等"))
        self.label_4.setText(_translate("MainWindow", "帮助文档\n"
"介绍使用方法\n"
"emmmm……\n"
"和吐槽方式"))
        self.label_6.setText(_translate("MainWindow", "我就是怕你填错了"))
        self.label_8.setText(_translate("MainWindow", "检查单位名单"))
        self.lineEdit_27.setText(_translate("MainWindow", "否"))

