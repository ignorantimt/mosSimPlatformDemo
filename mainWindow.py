# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1520, 960)
        MainWindow.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout_3.addWidget(self.listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout.addWidget(self.label_title)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget.addWidget(self.page)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.widget_1 = QVideoWidget(self.page_1)
        self.widget_1.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_1.setObjectName("widget_1")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.widget_2 = QtWidgets.QWidget(self.page_2)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setObjectName("widget_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.widget_3 = QVideoWidget(self.page_3)
        self.widget_3.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_3.setObjectName("widget_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.widget_4 = QtWebEngineWidgets.QWebEngineView(self.page_4)
        self.widget_4.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_4.setObjectName("widget_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.widget_5 = QtWebEngineWidgets.QWebEngineView(self.page_5)
        self.widget_5.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_5.setObjectName("widget_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.widget_6 = QtWidgets.QWidget(self.page_6)
        self.widget_6.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_6.setObjectName("widget_6")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.widget_7 = QtWidgets.QWidget(self.page_7)
        self.widget_7.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_7.setObjectName("widget_7")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.widget_8 = QtWidgets.QWidget(self.page_8)
        self.widget_8.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_8.setObjectName("widget_8")
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.widget_9 = QVideoWidget(self.page_9)
        self.widget_9.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_9.setObjectName("widget_9")
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.widget_10 = QtWidgets.QWidget(self.page_10)
        self.widget_10.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_10.setObjectName("widget_10")
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.widget_11 = QtWidgets.QWidget(self.page_11)
        self.widget_11.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_11.setObjectName("widget_11")
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.widget_12 = QtWidgets.QWidget(self.page_12)
        self.widget_12.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_12.setObjectName("widget_12")
        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.widget_13 = QtWidgets.QWidget(self.page_13)
        self.widget_13.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_13.setObjectName("widget_13")
        self.stackedWidget.addWidget(self.page_13)
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setObjectName("page_14")
        self.widget_14 = QtWidgets.QWidget(self.page_14)
        self.widget_14.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_14.setObjectName("widget_14")
        self.stackedWidget.addWidget(self.page_14)
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.widget_15 = QtWidgets.QWidget(self.page_15)
        self.widget_15.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_15.setObjectName("widget_15")
        self.stackedWidget.addWidget(self.page_15)
        self.page_16 = QtWidgets.QWidget()
        self.page_16.setObjectName("page_16")
        self.widget_16 = QtWidgets.QWidget(self.page_16)
        self.widget_16.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_16.setObjectName("widget_16")
        self.stackedWidget.addWidget(self.page_16)
        self.page_17 = QtWidgets.QWidget()
        self.page_17.setObjectName("page_17")
        self.widget_17 = QtWidgets.QWidget(self.page_17)
        self.widget_17.setGeometry(QtCore.QRect(10, 10, 961, 541))
        self.widget_17.setObjectName("widget_17")
        self.stackedWidget.addWidget(self.page_17)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.label_descr = QtWidgets.QLabel(self.centralwidget)
        self.label_descr.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.label_descr.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_descr.setWordWrap(True)
        self.label_descr.setObjectName("label_descr")
        self.verticalLayout.addWidget(self.label_descr)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1520, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "介绍"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "实验1：仿人足球机器人初探"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "实验2：Python编程实验"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "实验3：Ubuntu操作实验"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "实验4：ROS操作实验"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "实验5：Webots机器人动力学模型搭建实验"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "实验6：计算机视觉实验"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "实验7：手眼协同——位姿转换实验"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "实验8：机器人自主定位实验"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "实验9：机器人运动控制实验"))
        item = self.listWidget.item(10)
        item.setText(_translate("MainWindow", "实验10：机器人智能决策实验"))
        item = self.listWidget.item(11)
        item.setText(_translate("MainWindow", "实验11：仿人机器人仿真步行实验"))
        item = self.listWidget.item(12)
        item.setText(_translate("MainWindow", "实验12：搭建足球机器人仿真平台"))
        item = self.listWidget.item(13)
        item.setText(_translate("MainWindow", "实验13：仿人机器人步行速度控制实验"))
        item = self.listWidget.item(14)
        item.setText(_translate("MainWindow", "实验14：仿人机器人头部运动实验"))
        item = self.listWidget.item(15)
        item.setText(_translate("MainWindow", "实验15：仿人机器人足球识别实验"))
        item = self.listWidget.item(16)
        item.setText(_translate("MainWindow", "综合实验1：机器人点球实验"))
        item = self.listWidget.item(17)
        item.setText(_translate("MainWindow", "综合实验2：多机器人自主对战实验"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_title.setText(_translate("MainWindow", "介绍"))
        self.label_descr.setText(_translate("MainWindow", "TextLabel"))
        self.menu.setTitle(_translate("MainWindow", "仿人足球机器人课程"))
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())