# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/FormEmployee.ui'
#
# Created: Thu Aug 15 22:21:00 2013
#      by: PyQt4 UI code generator 4.10
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

class Ui_FormEmployee(object):
    def setupUi(self, FormEmployee):
        FormEmployee.setObjectName(_fromUtf8("FormEmployee"))
        FormEmployee.resize(277, 158)
        font = QtGui.QFont()
        font.setPointSize(10)
        FormEmployee.setFont(font)
        self.verticalLayout_2 = QtGui.QVBoxLayout(FormEmployee)
        self.verticalLayout_2.setMargin(3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(FormEmployee)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setMinimumSize(QtCore.QSize(80, 0))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout.addWidget(self.label_9)
        self.lineEdit_Name = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Name.setMinimumSize(QtCore.QSize(120, 0))
        self.lineEdit_Name.setObjectName(_fromUtf8("lineEdit_Name"))
        self.horizontalLayout.addWidget(self.lineEdit_Name)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setMinimumSize(QtCore.QSize(80, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_Email = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Email.setMinimumSize(QtCore.QSize(120, 0))
        self.lineEdit_Email.setObjectName(_fromUtf8("lineEdit_Email"))
        self.horizontalLayout_3.addWidget(self.lineEdit_Email)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setMinimumSize(QtCore.QSize(80, 0))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEdit_Cellphone = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Cellphone.setMinimumSize(QtCore.QSize(120, 0))
        self.lineEdit_Cellphone.setObjectName(_fromUtf8("lineEdit_Cellphone"))
        self.horizontalLayout_2.addWidget(self.lineEdit_Cellphone)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_10 = QtGui.QLabel(FormEmployee)
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_4.addWidget(self.label_10)
        self.pushButton_Cancel = QtGui.QPushButton(FormEmployee)
        self.pushButton_Cancel.setObjectName(_fromUtf8("pushButton_Cancel"))
        self.horizontalLayout_4.addWidget(self.pushButton_Cancel)
        self.pushButton_Save = QtGui.QPushButton(FormEmployee)
        self.pushButton_Save.setObjectName(_fromUtf8("pushButton_Save"))
        self.horizontalLayout_4.addWidget(self.pushButton_Save)
        self.horizontalLayout_4.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(FormEmployee)
        QtCore.QMetaObject.connectSlotsByName(FormEmployee)

    def retranslateUi(self, FormEmployee):
        FormEmployee.setWindowTitle(_translate("FormEmployee", "FormEmployee", None))
        self.groupBox.setTitle(_translate("FormEmployee", "业务信息：", None))
        self.label_9.setText(_translate("FormEmployee", "姓名：", None))
        self.label_4.setText(_translate("FormEmployee", "邮件：", None))
        self.label_5.setText(_translate("FormEmployee", "电话：", None))
        self.pushButton_Cancel.setText(_translate("FormEmployee", "取 消 (&C)", None))
        self.pushButton_Save.setText(_translate("FormEmployee", "保 存 (&S)", None))

