# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/TableRecords.ui'
#
# Created: Fri Aug 16 17:24:44 2013
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

class Ui_TableRecords(object):
    def setupUi(self, TableRecords):
        TableRecords.setObjectName(_fromUtf8("TableRecords"))
        TableRecords.resize(791, 557)
        font = QtGui.QFont()
        font.setPointSize(10)
        TableRecords.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(TableRecords)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setMargin(3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_Icon = QtGui.QLabel(TableRecords)
        self.label_Icon.setText(_fromUtf8(""))
        self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_072_bookmark.png")))
        self.label_Icon.setObjectName(_fromUtf8("label_Icon"))
        self.horizontalLayout.addWidget(self.label_Icon)
        self.label_Title = QtGui.QLabel(TableRecords)
        self.label_Title.setObjectName(_fromUtf8("label_Title"))
        self.horizontalLayout.addWidget(self.label_Title)
        self.label_FilterMask = QtGui.QLabel(TableRecords)
        self.label_FilterMask.setText(_fromUtf8(""))
        self.label_FilterMask.setAlignment(QtCore.Qt.AlignCenter)
        self.label_FilterMask.setObjectName(_fromUtf8("label_FilterMask"))
        self.horizontalLayout.addWidget(self.label_FilterMask)
        self.pushButton_Filter = QtGui.QPushButton(TableRecords)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_027_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Filter.setIcon(icon)
        self.pushButton_Filter.setFlat(False)
        self.pushButton_Filter.setObjectName(_fromUtf8("pushButton_Filter"))
        self.horizontalLayout.addWidget(self.pushButton_Filter)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(TableRecords)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.tableView_Records = QtGui.QTableView(TableRecords)
        self.tableView_Records.setObjectName(_fromUtf8("tableView_Records"))
        self.verticalLayout.addWidget(self.tableView_Records)
        self.groupBox = QtGui.QGroupBox(TableRecords)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setMargin(3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.comboBox_NumPerPage = QtGui.QComboBox(self.groupBox)
        self.comboBox_NumPerPage.setEditable(True)
        self.comboBox_NumPerPage.setObjectName(_fromUtf8("comboBox_NumPerPage"))
        self.comboBox_NumPerPage.addItem(_fromUtf8(""))
        self.comboBox_NumPerPage.addItem(_fromUtf8(""))
        self.comboBox_NumPerPage.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox_NumPerPage)
        self.pushButton_Last10Page = QtGui.QPushButton(self.groupBox)
        self.pushButton_Last10Page.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_171_fast_backward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Last10Page.setIcon(icon1)
        self.pushButton_Last10Page.setFlat(True)
        self.pushButton_Last10Page.setObjectName(_fromUtf8("pushButton_Last10Page"))
        self.horizontalLayout_2.addWidget(self.pushButton_Last10Page)
        self.pushButton_LastPage = QtGui.QPushButton(self.groupBox)
        self.pushButton_LastPage.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_170_step_backward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_LastPage.setIcon(icon2)
        self.pushButton_LastPage.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_LastPage.setFlat(True)
        self.pushButton_LastPage.setObjectName(_fromUtf8("pushButton_LastPage"))
        self.horizontalLayout_2.addWidget(self.pushButton_LastPage)
        self.lineEdit_Page = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_Page.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_Page.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Page.setReadOnly(True)
        self.lineEdit_Page.setObjectName(_fromUtf8("lineEdit_Page"))
        self.horizontalLayout_2.addWidget(self.lineEdit_Page)
        self.pushButton_NextPage = QtGui.QPushButton(self.groupBox)
        self.pushButton_NextPage.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_178_step_forward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_NextPage.setIcon(icon3)
        self.pushButton_NextPage.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_NextPage.setFlat(True)
        self.pushButton_NextPage.setObjectName(_fromUtf8("pushButton_NextPage"))
        self.horizontalLayout_2.addWidget(self.pushButton_NextPage)
        self.pushButton_Next10Page = QtGui.QPushButton(self.groupBox)
        self.pushButton_Next10Page.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_177_fast_forward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Next10Page.setIcon(icon4)
        self.pushButton_Next10Page.setFlat(True)
        self.pushButton_Next10Page.setObjectName(_fromUtf8("pushButton_Next10Page"))
        self.horizontalLayout_2.addWidget(self.pushButton_Next10Page)
        self.pushButton_Reload = QtGui.QPushButton(self.groupBox)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_081_refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Reload.setIcon(icon5)
        self.pushButton_Reload.setAutoRepeat(False)
        self.pushButton_Reload.setFlat(False)
        self.pushButton_Reload.setObjectName(_fromUtf8("pushButton_Reload"))
        self.horizontalLayout_2.addWidget(self.pushButton_Reload)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton_Delete = QtGui.QPushButton(self.groupBox)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_191_circle_minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Delete.setIcon(icon6)
        self.pushButton_Delete.setFlat(False)
        self.pushButton_Delete.setObjectName(_fromUtf8("pushButton_Delete"))
        self.horizontalLayout_2.addWidget(self.pushButton_Delete)
        self.pushButton_Modify = QtGui.QPushButton(self.groupBox)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_193_circle_ok.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Modify.setIcon(icon7)
        self.pushButton_Modify.setFlat(False)
        self.pushButton_Modify.setObjectName(_fromUtf8("pushButton_Modify"))
        self.horizontalLayout_2.addWidget(self.pushButton_Modify)
        self.pushButton_New = QtGui.QPushButton(self.groupBox)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_190_circle_plus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_New.setIcon(icon8)
        self.pushButton_New.setFlat(False)
        self.pushButton_New.setObjectName(_fromUtf8("pushButton_New"))
        self.horizontalLayout_2.addWidget(self.pushButton_New)
        self.horizontalLayout_2.setStretch(7, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(TableRecords)
        QtCore.QObject.connect(self.tableView_Records, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), TableRecords.repaint)
        QtCore.QMetaObject.connectSlotsByName(TableRecords)

    def retranslateUi(self, TableRecords):
        TableRecords.setWindowTitle(_translate("TableRecords", "TableRecords", None))
        self.label_Title.setText(_translate("TableRecords", "发货记录", None))
        self.pushButton_Filter.setText(_translate("TableRecords", "筛选 (&F)", None))
        self.pushButton_Filter.setShortcut(_translate("TableRecords", "F3", None))
        self.comboBox_NumPerPage.setItemText(0, _translate("TableRecords", "25", None))
        self.comboBox_NumPerPage.setItemText(1, _translate("TableRecords", "50", None))
        self.comboBox_NumPerPage.setItemText(2, _translate("TableRecords", "100", None))
        self.pushButton_LastPage.setShortcut(_translate("TableRecords", "PgUp", None))
        self.pushButton_NextPage.setShortcut(_translate("TableRecords", "PgDown", None))
        self.pushButton_Reload.setText(_translate("TableRecords", "刷新 (F5)", None))
        self.pushButton_Reload.setShortcut(_translate("TableRecords", "F5", None))
        self.pushButton_Delete.setText(_translate("TableRecords", "删除 (&D)", None))
        self.pushButton_Delete.setShortcut(_translate("TableRecords", "Del", None))
        self.pushButton_Modify.setText(_translate("TableRecords", "修改 (&E)", None))
        self.pushButton_Modify.setShortcut(_translate("TableRecords", "Return", None))
        self.pushButton_New.setText(_translate("TableRecords", "新增 (&N)", None))
        self.pushButton_New.setShortcut(_translate("TableRecords", "Ins", None))

import resource_rc
