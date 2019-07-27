# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(497, 307)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: #34495e\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    background-color: #34495e\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.output = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Semibold [ADBO]")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.output.setFont(font)
        self.output.setStyleSheet("QLabel{\n"
"    color: #fff\n"
"}")
        self.output.setText("")
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setObjectName("output")
        self.gridLayout_2.addWidget(self.output, 2, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Semibold [ADBO]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    color: #fff\n"
"}")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Semibold [ADBO]")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setStyleSheet("QLineEdit{\n"
"    background: #fff; \n"
"}")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.password)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Semibold [ADBO]")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"    color: #fff\n"
"}")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.ip_address = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Semibold [ADBO]")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ip_address.setFont(font)
        self.ip_address.setStyleSheet("QLineEdit{\n"
"    background: #fff; \n"
"}")
        self.ip_address.setObjectName("ip_address")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ip_address)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.restrict = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Semibold [ADBO]")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.restrict.setFont(font)
        self.restrict.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.restrict.setStyleSheet("QPushButton{\n"
"    /*background-color: #e67e22;*/\n"
"    background-color: #3498db;\n"
"    color: #fff;\n"
"    padding-top: 4px;\n"
"    padding-right: 6px;\n"
"      padding-bottom: 4px;\n"
"      padding-left: 6px;\n"
"    border: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover { \n"
"  /*background-color: #bf6516;*/\n"
"  background-color: #217dbb;\n"
"}\n"
"\n"
"QPushButton:pressed { \n"
"  background-color: #196090;\n"
"}")
        self.restrict.setObjectName("restrict")
        self.horizontalLayout.addWidget(self.restrict)
        self.enable = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Semibold [ADBO]")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.enable.setFont(font)
        self.enable.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enable.setStyleSheet("QPushButton{\n"
"    background-color: #2ecc71;\n"
"    color: #fff;\n"
"    padding-top: 4px;\n"
"    padding-right: 6px;\n"
"      padding-bottom: 4px;\n"
"      padding-left: 6px;\n"
"    border: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover { \n"
"  background-color: #25a25a;\n"
"}\n"
"\n"
"QPushButton:pressed { \n"
"  background-color: #1b7943;\n"
"}")
        self.enable.setObjectName("enable")
        self.horizontalLayout.addWidget(self.enable)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Contraseña de super usuario"))
        self.label_2.setText(_translate("MainWindow", "Dirección IP a restringir"))
        self.restrict.setText(_translate("MainWindow", "Restringir"))
        self.enable.setText(_translate("MainWindow", "Habilitar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

