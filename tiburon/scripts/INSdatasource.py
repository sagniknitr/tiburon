# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Jun  6 15:50:16 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(804, 635)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 211, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 150, 761, 421))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Automatic = QtGui.QWidget()
        self.Automatic.setObjectName(_fromUtf8("Automatic"))
        self.label_2 = QtGui.QLabel(self.Automatic)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 67, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.Automatic)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 91, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.Automatic)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 67, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.Automatic)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 67, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.Automatic)
        self.label_6.setGeometry(QtCore.QRect(10, 180, 67, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.Pressure = QtGui.QLabel(self.Automatic)
        self.Pressure.setGeometry(QtCore.QRect(110, 30, 67, 17))
        self.Pressure.setObjectName(_fromUtf8("Pressure"))
        self.Temperature = QtGui.QLabel(self.Automatic)
        self.Temperature.setGeometry(QtCore.QRect(110, 70, 67, 17))
        self.Temperature.setObjectName(_fromUtf8("Temperature"))
        self.Yaw = QtGui.QLabel(self.Automatic)
        self.Yaw.setGeometry(QtCore.QRect(110, 110, 67, 17))
        self.Yaw.setObjectName(_fromUtf8("Yaw"))
        self.Pitch = QtGui.QLabel(self.Automatic)
        self.Pitch.setGeometry(QtCore.QRect(110, 150, 67, 17))
        self.Pitch.setObjectName(_fromUtf8("Pitch"))
        self.Roll = QtGui.QLabel(self.Automatic)
        self.Roll.setGeometry(QtCore.QRect(110, 180, 67, 17))
        self.Roll.setObjectName(_fromUtf8("Roll"))
        self.label_12 = QtGui.QLabel(self.Automatic)
        self.label_12.setGeometry(QtCore.QRect(200, 10, 91, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.Quaterniondata = QtGui.QTextEdit(self.Automatic)
        self.Quaterniondata.setGeometry(QtCore.QRect(200, 30, 241, 121))
        self.Quaterniondata.setReadOnly(True)
        self.Quaterniondata.setObjectName(_fromUtf8("Quaterniondata"))
        self.label_13 = QtGui.QLabel(self.Automatic)
        self.label_13.setGeometry(QtCore.QRect(490, 10, 131, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.Accelerationdata = QtGui.QTextEdit(self.Automatic)
        self.Accelerationdata.setGeometry(QtCore.QRect(490, 30, 251, 121))
        self.Accelerationdata.setReadOnly(True)
        self.Accelerationdata.setObjectName(_fromUtf8("Accelerationdata"))
        self.label_14 = QtGui.QLabel(self.Automatic)
        self.label_14.setGeometry(QtCore.QRect(200, 220, 81, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.Gyrodata = QtGui.QTextEdit(self.Automatic)
        self.Gyrodata.setGeometry(QtCore.QRect(200, 240, 241, 121))
        self.Gyrodata.setReadOnly(True)
        self.Gyrodata.setObjectName(_fromUtf8("Gyrodata"))
        self.label_15 = QtGui.QLabel(self.Automatic)
        self.label_15.setGeometry(QtCore.QRect(500, 220, 151, 17))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.Magnetometerdata = QtGui.QTextEdit(self.Automatic)
        self.Magnetometerdata.setGeometry(QtCore.QRect(490, 240, 251, 121))
        self.Magnetometerdata.setReadOnly(True)
        self.Magnetometerdata.setObjectName(_fromUtf8("Magnetometerdata"))
        self.tabWidget.addTab(self.Automatic, _fromUtf8(""))
        self.Manual = QtGui.QWidget()
        self.Manual.setObjectName(_fromUtf8("Manual"))
        self.label_16 = QtGui.QLabel(self.Manual)
        self.label_16.setGeometry(QtCore.QRect(30, 10, 151, 31))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.Pressureandtemp = QtGui.QPushButton(self.Manual)
        self.Pressureandtemp.setGeometry(QtCore.QRect(20, 40, 191, 27))
        self.Pressureandtemp.setObjectName(_fromUtf8("Pressureandtemp"))
        self.YPRbtn = QtGui.QPushButton(self.Manual)
        self.YPRbtn.setGeometry(QtCore.QRect(260, 40, 99, 27))
        self.YPRbtn.setObjectName(_fromUtf8("YPRbtn"))
        self.Quatbtn = QtGui.QPushButton(self.Manual)
        self.Quatbtn.setGeometry(QtCore.QRect(500, 40, 99, 27))
        self.Quatbtn.setObjectName(_fromUtf8("Quatbtn"))
        self.Accelbtn = QtGui.QPushButton(self.Manual)
        self.Accelbtn.setGeometry(QtCore.QRect(30, 220, 99, 27))
        self.Accelbtn.setObjectName(_fromUtf8("Accelbtn"))
        self.Gyrobtn = QtGui.QPushButton(self.Manual)
        self.Gyrobtn.setGeometry(QtCore.QRect(260, 220, 99, 27))
        self.Gyrobtn.setObjectName(_fromUtf8("Gyrobtn"))
        self.magnetobtn = QtGui.QPushButton(self.Manual)
        self.magnetobtn.setGeometry(QtCore.QRect(510, 220, 121, 27))
        self.magnetobtn.setObjectName(_fromUtf8("magnetobtn"))
        self.Pressuretempbox = QtGui.QTextEdit(self.Manual)
        self.Pressuretempbox.setGeometry(QtCore.QRect(20, 80, 191, 121))
        self.Pressuretempbox.setObjectName(_fromUtf8("Pressuretempbox"))
        self.Yprdatabox = QtGui.QTextEdit(self.Manual)
        self.Yprdatabox.setGeometry(QtCore.QRect(270, 80, 181, 121))
        self.Yprdatabox.setObjectName(_fromUtf8("Yprdatabox"))
        self.Quatdatabox = QtGui.QTextEdit(self.Manual)
        self.Quatdatabox.setGeometry(QtCore.QRect(500, 80, 211, 121))
        self.Quatdatabox.setObjectName(_fromUtf8("Quatdatabox"))
        self.Acceldatabox = QtGui.QTextEdit(self.Manual)
        self.Acceldatabox.setGeometry(QtCore.QRect(20, 260, 191, 121))
        self.Acceldatabox.setObjectName(_fromUtf8("Acceldatabox"))
        self.gyrodatabox = QtGui.QTextEdit(self.Manual)
        self.gyrodatabox.setGeometry(QtCore.QRect(270, 260, 181, 121))
        self.gyrodatabox.setObjectName(_fromUtf8("gyrodatabox"))
        self.Magnetodatabox = QtGui.QTextEdit(self.Manual)
        self.Magnetodatabox.setGeometry(QtCore.QRect(500, 260, 211, 121))
        self.Magnetodatabox.setObjectName(_fromUtf8("Magnetodatabox"))
        self.tabWidget.addTab(self.Manual, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_17 = QtGui.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(20, 20, 111, 21))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(110, 80, 67, 17))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(110, 120, 67, 17))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(110, 160, 67, 17))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.lineEdit = QtGui.QLineEdit(self.tab_3)
        self.lineEdit.setGeometry(QtCore.QRect(160, 70, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 110, 113, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 150, 113, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.label_7 = QtGui.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(270, 10, 81, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(540, 10, 81, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.textEdit = QtGui.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(270, 30, 171, 131))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralWidget)
        self.textEdit_2.setGeometry(QtCore.QRect(540, 30, 181, 131))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 804, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "NITR AUV INS PANEL", None))
        self.label_2.setText(_translate("MainWindow", "Pressure:", None))
        self.label_3.setText(_translate("MainWindow", "Temperature:", None))
        self.label_4.setText(_translate("MainWindow", "Yaw:", None))
        self.label_5.setText(_translate("MainWindow", "Pitch:", None))
        self.label_6.setText(_translate("MainWindow", "roll:", None))
        self.Pressure.setText(_translate("MainWindow", "NA", None))
        self.Temperature.setText(_translate("MainWindow", "NA", None))
        self.Yaw.setText(_translate("MainWindow", "NA", None))
        self.Pitch.setText(_translate("MainWindow", "NA", None))
        self.Roll.setText(_translate("MainWindow", "NA", None))
        self.label_12.setText(_translate("MainWindow", "Quaternion:", None))
        self.label_13.setText(_translate("MainWindow", "acceleration data:", None))
        self.label_14.setText(_translate("MainWindow", "Gyro data:", None))
        self.label_15.setText(_translate("MainWindow", "Magnetometer data:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Automatic), _translate("MainWindow", "Tab 1", None))
        self.label_16.setText(_translate("MainWindow", "GET DATA", None))
        self.Pressureandtemp.setText(_translate("MainWindow", "Pressure and Temperature", None))
        self.YPRbtn.setText(_translate("MainWindow", "YPR", None))
        self.Quatbtn.setText(_translate("MainWindow", "Quaternion", None))
        self.Accelbtn.setText(_translate("MainWindow", "Accel_Data", None))
        self.Gyrobtn.setText(_translate("MainWindow", "Gyro_Data", None))
        self.magnetobtn.setText(_translate("MainWindow", "Magneto_Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Manual), _translate("MainWindow", "Tab 2", None))
        self.label_17.setText(_translate("MainWindow", "Set Parameters", None))
        self.label_18.setText(_translate("MainWindow", "Yaw", None))
        self.label_19.setText(_translate("MainWindow", "Pitch", None))
        self.label_20.setText(_translate("MainWindow", "Roll", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page", None))
        self.label_7.setText(_translate("MainWindow", "errorboard", None))
        self.label_8.setText(_translate("MainWindow", "Infoboard", None))

