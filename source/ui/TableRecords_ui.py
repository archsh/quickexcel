# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/TableRecords.ui'
#
# Created: Mon Jul 22 15:46:10 2013
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(791, 354)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setMargin(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_072_bookmark.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_Filter = QtGui.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_027_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Filter.setIcon(icon)
        self.pushButton_Filter.setObjectName(_fromUtf8("pushButton_Filter"))
        self.horizontalLayout.addWidget(self.pushButton_Filter)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView_Records = QtGui.QTableView(Form)
        self.tableView_Records.setObjectName(_fromUtf8("tableView_Records"))
        self.verticalLayout.addWidget(self.tableView_Records)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_LastPage = QtGui.QPushButton(Form)
        self.pushButton_LastPage.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_216_circle_arrow_left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_LastPage.setIcon(icon1)
        self.pushButton_LastPage.setObjectName(_fromUtf8("pushButton_LastPage"))
        self.horizontalLayout_2.addWidget(self.pushButton_LastPage)
        self.lineEdit_Page = QtGui.QLineEdit(Form)
        self.lineEdit_Page.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_Page.setObjectName(_fromUtf8("lineEdit_Page"))
        self.horizontalLayout_2.addWidget(self.lineEdit_Page)
        self.pushButton_NextPage = QtGui.QPushButton(Form)
        self.pushButton_NextPage.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_217_circle_arrow_right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_NextPage.setIcon(icon2)
        self.pushButton_NextPage.setObjectName(_fromUtf8("pushButton_NextPage"))
        self.horizontalLayout_2.addWidget(self.pushButton_NextPage)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton_Delete = QtGui.QPushButton(Form)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_191_circle_minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Delete.setIcon(icon3)
        self.pushButton_Delete.setObjectName(_fromUtf8("pushButton_Delete"))
        self.horizontalLayout_2.addWidget(self.pushButton_Delete)
        self.pushButton_Modify = QtGui.QPushButton(Form)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_193_circle_ok.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Modify.setIcon(icon4)
        self.pushButton_Modify.setObjectName(_fromUtf8("pushButton_Modify"))
        self.horizontalLayout_2.addWidget(self.pushButton_Modify)
        self.pushButton_New = QtGui.QPushButton(Form)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_190_circle_plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_New.setIcon(icon5)
        self.pushButton_New.setObjectName(_fromUtf8("pushButton_New"))
        self.horizontalLayout_2.addWidget(self.pushButton_New)
        self.horizontalLayout_2.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "发货记录", None))
        self.pushButton_Filter.setText(_translate("Form", "筛选", None))
        self.pushButton_Delete.setText(_translate("Form", "删除", None))
        self.pushButton_Modify.setText(_translate("Form", "修改", None))
        self.pushButton_New.setText(_translate("Form", "新增", None))

import resource_rc
