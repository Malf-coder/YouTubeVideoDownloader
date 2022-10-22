# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YouTubeVideo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("YouTubeVideos")
        MainWindow.setFixedSize(400, 370)
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(18, 18, 18);\n"
                                 "border-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 200, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-style:solid;\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-width: 3px;\n"
                                    "border-color: rgb(170, 0, 0);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 300, 381, 31))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(170, 0, 0);\n"
                                        "border-radius: 4px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 250, 381, 31))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(170, 0, 0);\n"
                                        "border-radius: 4px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setToolTipDuration(3)
        self.label.setStyleSheet("border-style:solid;\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "border-width: 3px;\n"
                                 "border-color: rgb(170, 0, 0);\n"
                                 "color: rgb(126, 126, 126);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTubeVideos"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "https://www.youtube.com"))
        self.pushButton_2.setText(_translate("MainWindow", "Далее"))
        self.pushButton_3.setText(_translate("MainWindow", "Выбрать папку для скачивания"))
        self.label.setText(_translate("MainWindow", "Ожидание"))


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(500, 170)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 80, 481, 22))
        self.comboBox.setStyleSheet("border-style:solid;\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-width: 3px;\n"
                                    "border-color: rgb(170, 0, 0);\n"
                                    "color: rgb(126, 126, 126);\n"
                                    "")
        self.comboBox.setObjectName("comboBox")
        self.dowloand_button = QtWidgets.QPushButton(self.centralwidget)
        self.dowloand_button.setGeometry(QtCore.QRect(10, 122, 481, 31))
        self.dowloand_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(170, 0, 0);\n"
                                           "border-radius: 4px;")
        self.dowloand_button.setObjectName("dowloand_button")
        self.dowloand_label = QtWidgets.QLabel(self.centralwidget)
        self.dowloand_label.setGeometry(QtCore.QRect(10, 15, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dowloand_label.setFont(font)
        self.dowloand_label.setStyleSheet("border-style:solid;\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "border-width: 3px;\n"
                                          "border-color: rgb(170, 0, 0);\n"
                                          "color: rgb(126, 126, 126);\n"
                                          "")
        self.dowloand_label.setObjectName("dowloand_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTubeVideos"))
        self.dowloand_button.setText(_translate("MainWindow", "Скачать"))
        self.dowloand_label.setText(_translate("MainWindow", "Выбирите качество видео"))
