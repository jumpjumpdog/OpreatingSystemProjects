# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1budianti.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!



from PyQt4 import QtCore, QtGui
from TenpLayer import TempLayer
Temp_Layer = []

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

#创建ui
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lev3_1 = QtGui.QPushButton(self.centralwidget)
        self.lev3_1.setGeometry(QtCore.QRect(290, 330, 51, 31))
        self.lev3_1.setText(_fromUtf8(""))
        self.lev3_1.setObjectName(_fromUtf8("lev3_1"))
        self.lev4_1 = QtGui.QPushButton(self.centralwidget)
        self.lev4_1.setGeometry(QtCore.QRect(290, 290, 51, 31))
        self.lev4_1.setText(_fromUtf8(""))
        self.lev4_1.setObjectName(_fromUtf8("lev4_1"))
        self.up2 = QtGui.QPushButton(self.centralwidget)
        self.up2.setGeometry(QtCore.QRect(110, 370, 61, 31))
        self.up2.setObjectName(_fromUtf8("up2"))
        self.lev7_1 = QtGui.QPushButton(self.centralwidget)
        self.lev7_1.setGeometry(QtCore.QRect(290, 170, 51, 31))
        self.lev7_1.setText(_fromUtf8(""))
        self.lev7_1.setObjectName(_fromUtf8("lev7_1"))
        self.lev10_1 = QtGui.QPushButton(self.centralwidget)
        self.lev10_1.setGeometry(QtCore.QRect(290, 50, 51, 31))
        self.lev10_1.setText(_fromUtf8(""))
        self.lev10_1.setObjectName(_fromUtf8("lev10_1"))
        self.lev8_1 = QtGui.QPushButton(self.centralwidget)
        self.lev8_1.setGeometry(QtCore.QRect(290, 130, 51, 31))
        self.lev8_1.setText(_fromUtf8(""))
        self.lev8_1.setObjectName(_fromUtf8("lev8_1"))
        self.up1 = QtGui.QPushButton(self.centralwidget)
        self.up1.setGeometry(QtCore.QRect(110, 410, 61, 31))
        self.up1.setObjectName(_fromUtf8("up1"))
        self.down8 = QtGui.QPushButton(self.centralwidget)
        self.down8.setGeometry(QtCore.QRect(180, 130, 61, 31))
        self.down8.setObjectName(_fromUtf8("down8"))
        self.up6 = QtGui.QPushButton(self.centralwidget)
        self.up6.setGeometry(QtCore.QRect(110, 210, 61, 31))
        self.up6.setObjectName(_fromUtf8("up6"))
        self.up8 = QtGui.QPushButton(self.centralwidget)
        self.up8.setGeometry(QtCore.QRect(110, 130, 61, 31))
        self.up8.setObjectName(_fromUtf8("up8"))
        self.down4 = QtGui.QPushButton(self.centralwidget)
        self.down4.setGeometry(QtCore.QRect(180, 290, 61, 31))
        self.down4.setObjectName(_fromUtf8("down4"))
        self.up3 = QtGui.QPushButton(self.centralwidget)
        self.up3.setGeometry(QtCore.QRect(110, 330, 61, 31))
        self.up3.setObjectName(_fromUtf8("up3"))
        self.down10 = QtGui.QPushButton(self.centralwidget)
        self.down10.setGeometry(QtCore.QRect(180, 50, 61, 31))
        self.down10.setObjectName(_fromUtf8("down10"))
        self.lev9_1 = QtGui.QPushButton(self.centralwidget)
        self.lev9_1.setGeometry(QtCore.QRect(290, 90, 51, 31))
        self.lev9_1.setText(_fromUtf8(""))
        self.lev9_1.setObjectName(_fromUtf8("lev9_1"))
        self.lev5_1 = QtGui.QPushButton(self.centralwidget)
        self.lev5_1.setGeometry(QtCore.QRect(290, 250, 51, 31))
        self.lev5_1.setText(_fromUtf8(""))
        self.lev5_1.setObjectName(_fromUtf8("lev5_1"))
        self.down9 = QtGui.QPushButton(self.centralwidget)
        self.down9.setGeometry(QtCore.QRect(180, 90, 61, 31))
        self.down9.setObjectName(_fromUtf8("down9"))
        self.up9 = QtGui.QPushButton(self.centralwidget)
        self.up9.setGeometry(QtCore.QRect(110, 90, 61, 31))
        self.up9.setObjectName(_fromUtf8("up9"))
        self.up7 = QtGui.QPushButton(self.centralwidget)
        self.up7.setGeometry(QtCore.QRect(110, 170, 61, 31))
        self.up7.setObjectName(_fromUtf8("up7"))
        self.up4 = QtGui.QPushButton(self.centralwidget)
        self.up4.setGeometry(QtCore.QRect(110, 290, 61, 31))
        self.up4.setObjectName(_fromUtf8("up4"))
        self.down7 = QtGui.QPushButton(self.centralwidget)
        self.down7.setGeometry(QtCore.QRect(180, 170, 61, 31))
        self.down7.setObjectName(_fromUtf8("down7"))
        self.lev1_1 = QtGui.QPushButton(self.centralwidget)
        self.lev1_1.setGeometry(QtCore.QRect(290, 410, 51, 31))
        self.lev1_1.setText(_fromUtf8(""))
        self.lev1_1.setObjectName(_fromUtf8("lev1_1"))
        self.up5 = QtGui.QPushButton(self.centralwidget)
        self.up5.setGeometry(QtCore.QRect(110, 250, 61, 31))
        self.up5.setObjectName(_fromUtf8("up5"))
        self.lev6_1 = QtGui.QPushButton(self.centralwidget)
        self.lev6_1.setGeometry(QtCore.QRect(290, 210, 51, 31))
        self.lev6_1.setText(_fromUtf8(""))
        self.lev6_1.setObjectName(_fromUtf8("lev6_1"))
        self.down5 = QtGui.QPushButton(self.centralwidget)
        self.down5.setGeometry(QtCore.QRect(180, 250, 61, 31))
        self.down5.setObjectName(_fromUtf8("dwon5"))
        self.down6 = QtGui.QPushButton(self.centralwidget)
        self.down6.setGeometry(QtCore.QRect(180, 210, 61, 31))
        self.down6.setObjectName(_fromUtf8("down6"))
        self.down3 = QtGui.QPushButton(self.centralwidget)
        self.down3.setGeometry(QtCore.QRect(180, 330, 61, 31))
        self.down3.setObjectName(_fromUtf8("down3"))
        self.down2 = QtGui.QPushButton(self.centralwidget)
        self.down2.setGeometry(QtCore.QRect(180, 370, 61, 31))
        self.down2.setObjectName(_fromUtf8("down2"))
        self.lev2_1 = QtGui.QPushButton(self.centralwidget)
        self.lev2_1.setGeometry(QtCore.QRect(290, 370, 51, 31))
        self.lev2_1.setText(_fromUtf8(""))
        self.lev2_1.setObjectName(_fromUtf8("lev2_1"))
        self.lev10_2 = QtGui.QPushButton(self.centralwidget)
        self.lev10_2.setGeometry(QtCore.QRect(370, 50, 51, 31))
        self.lev10_2.setText(_fromUtf8(""))
        self.lev10_2.setObjectName(_fromUtf8("lev10_2"))
        self.lev9_2 = QtGui.QPushButton(self.centralwidget)
        self.lev9_2.setGeometry(QtCore.QRect(370, 90, 51, 31))
        self.lev9_2.setText(_fromUtf8(""))
        self.lev9_2.setObjectName(_fromUtf8("lev9_2"))
        self.lev8_2 = QtGui.QPushButton(self.centralwidget)
        self.lev8_2.setGeometry(QtCore.QRect(370, 130, 51, 31))
        self.lev8_2.setText(_fromUtf8(""))
        self.lev8_2.setObjectName(_fromUtf8("lev8_2"))
        self.lev7_2 = QtGui.QPushButton(self.centralwidget)
        self.lev7_2.setGeometry(QtCore.QRect(370, 170, 51, 31))
        self.lev7_2.setText(_fromUtf8(""))
        self.lev7_2.setObjectName(_fromUtf8("lev7_2"))
        self.lev6_2 = QtGui.QPushButton(self.centralwidget)
        self.lev6_2.setGeometry(QtCore.QRect(370, 210, 51, 31))
        self.lev6_2.setText(_fromUtf8(""))
        self.lev6_2.setObjectName(_fromUtf8("lev6_2"))
        self.lev5_2 = QtGui.QPushButton(self.centralwidget)
        self.lev5_2.setGeometry(QtCore.QRect(370, 250, 51, 31))
        self.lev5_2.setText(_fromUtf8(""))
        self.lev5_2.setObjectName(_fromUtf8("lev5_2"))
        self.lev4_2 = QtGui.QPushButton(self.centralwidget)
        self.lev4_2.setGeometry(QtCore.QRect(370, 290, 51, 31))
        self.lev4_2.setText(_fromUtf8(""))
        self.lev4_2.setObjectName(_fromUtf8("lev4_2"))
        self.lev3_2 = QtGui.QPushButton(self.centralwidget)
        self.lev3_2.setGeometry(QtCore.QRect(370, 330, 51, 31))
        self.lev3_2.setText(_fromUtf8(""))
        self.lev3_2.setObjectName(_fromUtf8("lev3_2"))
        self.lev2_2 = QtGui.QPushButton(self.centralwidget)
        self.lev2_2.setGeometry(QtCore.QRect(370, 370, 51, 31))
        self.lev2_2.setText(_fromUtf8(""))
        self.lev2_2.setObjectName(_fromUtf8("lev2_2"))
        self.lev1_2 = QtGui.QPushButton(self.centralwidget)
        self.lev1_2.setGeometry(QtCore.QRect(370, 410, 51, 31))
        self.lev1_2.setText(_fromUtf8(""))
        self.lev1_2.setObjectName(_fromUtf8("lev1_2"))
        self.lev10_3 = QtGui.QPushButton(self.centralwidget)
        self.lev10_3.setGeometry(QtCore.QRect(450, 50, 51, 31))
        self.lev10_3.setText(_fromUtf8(""))
        self.lev10_3.setObjectName(_fromUtf8("lev10_3"))
        self.lev9_3 = QtGui.QPushButton(self.centralwidget)
        self.lev9_3.setGeometry(QtCore.QRect(450, 90, 51, 31))
        self.lev9_3.setText(_fromUtf8(""))
        self.lev9_3.setObjectName(_fromUtf8("lev9_3"))
        self.lev8_3 = QtGui.QPushButton(self.centralwidget)
        self.lev8_3.setGeometry(QtCore.QRect(450, 130, 51, 31))
        self.lev8_3.setText(_fromUtf8(""))
        self.lev8_3.setObjectName(_fromUtf8("lev8_3"))
        self.lev7_3 = QtGui.QPushButton(self.centralwidget)
        self.lev7_3.setGeometry(QtCore.QRect(450, 170, 51, 31))
        self.lev7_3.setText(_fromUtf8(""))
        self.lev7_3.setObjectName(_fromUtf8("lev7_3"))
        self.lev6_3 = QtGui.QPushButton(self.centralwidget)
        self.lev6_3.setGeometry(QtCore.QRect(450, 210, 51, 31))
        self.lev6_3.setText(_fromUtf8(""))
        self.lev6_3.setObjectName(_fromUtf8("lev6_3"))
        self.lev5_3 = QtGui.QPushButton(self.centralwidget)
        self.lev5_3.setGeometry(QtCore.QRect(450, 250, 51, 31))
        self.lev5_3.setText(_fromUtf8(""))
        self.lev5_3.setObjectName(_fromUtf8("lev5_3"))
        self.lev4_3 = QtGui.QPushButton(self.centralwidget)
        self.lev4_3.setGeometry(QtCore.QRect(450, 290, 51, 31))
        self.lev4_3.setText(_fromUtf8(""))
        self.lev4_3.setObjectName(_fromUtf8("lev4_3"))
        self.lev3_3 = QtGui.QPushButton(self.centralwidget)
        self.lev3_3.setGeometry(QtCore.QRect(450, 330, 51, 31))
        self.lev3_3.setText(_fromUtf8(""))
        self.lev3_3.setObjectName(_fromUtf8("lev3_3"))
        self.lev2_3 = QtGui.QPushButton(self.centralwidget)
        self.lev2_3.setGeometry(QtCore.QRect(450, 370, 51, 31))
        self.lev2_3.setText(_fromUtf8(""))
        self.lev2_3.setObjectName(_fromUtf8("lev2_3"))
        self.lev1_3 = QtGui.QPushButton(self.centralwidget)
        self.lev1_3.setGeometry(QtCore.QRect(450, 410, 51, 31))
        self.lev1_3.setText(_fromUtf8(""))
        self.lev1_3.setObjectName(_fromUtf8("lev1_3"))
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.up2.setText(_translate("MainWindow", "up", None))
        self.up1.setText(_translate("MainWindow", "up", None))
        self.down8.setText(_translate("MainWindow", "down", None))
        self.up6.setText(_translate("MainWindow", "up", None))
        self.up8.setText(_translate("MainWindow", "up", None))
        self.down4.setText(_translate("MainWindow", "down", None))
        self.up3.setText(_translate("MainWindow", "up", None))
        self.down10.setText(_translate("MainWindow", "down", None))
        self.down9.setText(_translate("MainWindow", "down", None))
        self.up9.setText(_translate("MainWindow", "up", None))
        self.up7.setText(_translate("MainWindow", "up", None))
        self.up4.setText(_translate("MainWindow", "up", None))
        self.down7.setText(_translate("MainWindow", "down", None))
        self.up5.setText(_translate("MainWindow", "up", None))
        self.down5.setText(_translate("MainWindow", "down", None))
        self.down6.setText(_translate("MainWindow", "down", None))
        self.down3.setText(_translate("MainWindow", "down", None))
        self.down2.setText(_translate("MainWindow", "down", None))

#各个楼层的按钮的槽，当按钮被点击时，就会有一个当前等待乘客被添加到Temp_Layer
#Temp_Layer存储了乘客的楼层信息以及上行还是下行信息
class MyForm(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.up1, QtCore.SIGNAL('clicked()'), self.up1_clicked)
        QtCore.QObject.connect(self.ui.up2,QtCore.SIGNAL('clicked()'),self.up2_clicked)
        QtCore.QObject.connect(self.ui.up3, QtCore.SIGNAL('clicked()'), self.up3_clicked)
        QtCore.QObject.connect(self.ui.up4, QtCore.SIGNAL('clicked()'), self.up4_clicked)
        QtCore.QObject.connect(self.ui.up5, QtCore.SIGNAL('clicked()'), self.up5_clicked)
        QtCore.QObject.connect(self.ui.up6, QtCore.SIGNAL('clicked()'), self.up6_clicked)
        QtCore.QObject.connect(self.ui.up7, QtCore.SIGNAL('clicked()'), self.up7_clicked)
        QtCore.QObject.connect(self.ui.up8, QtCore.SIGNAL('clicked()'), self.up8_clicked)
        QtCore.QObject.connect(self.ui.up9, QtCore.SIGNAL('clicked()'), self.up9_clicked)

        QtCore.QObject.connect(self.ui.down2, QtCore.SIGNAL('clicked()'), self.down2_clicked)
        QtCore.QObject.connect(self.ui.down3, QtCore.SIGNAL('clicked()'), self.down3_clicked)
        QtCore.QObject.connect(self.ui.down4, QtCore.SIGNAL('clicked()'), self.down4_clicked)
        QtCore.QObject.connect(self.ui.down5, QtCore.SIGNAL('clicked()'), self.down5_clicked)
        QtCore.QObject.connect(self.ui.down6, QtCore.SIGNAL('clicked()'), self.down6_clicked)
        QtCore.QObject.connect(self.ui.down7, QtCore.SIGNAL('clicked()'), self.down7_clicked)
        QtCore.QObject.connect(self.ui.down8, QtCore.SIGNAL('clicked()'), self.down8_clicked)
        QtCore.QObject.connect(self.ui.down9, QtCore.SIGNAL('clicked()'), self.down9_clicked)
        QtCore.QObject.connect(self.ui.down10, QtCore.SIGNAL('clicked()'), self.down10_clicked)



    def up1_clicked(self):
        temp = TempLayer('up',1)
        Temp_Layer.append(temp)


    def up2_clicked(self):
        temp = TempLayer('up',2)
        Temp_Layer.append(temp)

    def up3_clicked(self):
        temp = TempLayer('up', 3)
        Temp_Layer.append(temp)


    def up4_clicked(self):
        temp = TempLayer('up', 4)
        Temp_Layer.append(temp)



    def up5_clicked(self):
        print "clicked"
        temp = TempLayer('up', 5)
        Temp_Layer.append(temp)

    def up6_clicked(self):
        temp = TempLayer('up', 6)
        Temp_Layer.append(temp)


    def up7_clicked(self):
        temp = TempLayer('up', 7)
        Temp_Layer.append(temp)


    def up8_clicked(self):
        temp = TempLayer('up', 8)
        Temp_Layer.append(temp)


    def up9_clicked(self):
        temp = TempLayer('up', 9)
        Temp_Layer.append(temp)


    def down2_clicked(self):
        temp = TempLayer('down', 2)
        Temp_Layer.append(temp)


    def down3_clicked(self):
        temp = TempLayer('down', 3)
        Temp_Layer.append(temp)



    def down4_clicked(self):
        temp = TempLayer('down', 4)
        Temp_Layer.append(temp)


    def down5_clicked(self):
        temp = TempLayer('down', 5)
        Temp_Layer.append(temp)


    def down6_clicked(self):
        temp = TempLayer('down', 6)
        Temp_Layer.append(temp)


    def down7_clicked(self):
        temp = TempLayer('down', 7)
        Temp_Layer.append(temp)


    def down8_clicked(self):
        temp = TempLayer('down', 8)
        Temp_Layer.append(temp)


    def down9_clicked(self):
        temp = TempLayer('down', 9)
        Temp_Layer.append(temp)


    def down10_clicked(self):
        temp = TempLayer('down', 10)
        Temp_Layer.append(temp)
