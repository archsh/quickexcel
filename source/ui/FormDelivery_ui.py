# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/FormDelivery.ui'
#
# Created: Mon Jul 22 16:12:27 2013
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

class Ui_FormDelivery(object):
    def setupUi(self, FormDelivery):
        FormDelivery.setObjectName(_fromUtf8("FormDelivery"))
        FormDelivery.resize(658, 173)
        font = QtGui.QFont()
        font.setPointSize(10)
        FormDelivery.setFont(font)
        self.verticalLayout_2 = QtGui.QVBoxLayout(FormDelivery)
        self.verticalLayout_2.setMargin(3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(FormDelivery)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setMinimumSize(QtCore.QSize(80, 0))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_2.addWidget(self.label_9)
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setMinimumSize(QtCore.QSize(120, 0))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setMinimumSize(QtCore.QSize(80, 0))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.comboBox_3 = QtGui.QComboBox(self.groupBox)
        self.comboBox_3.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setDuplicatesEnabled(True)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setMinimumSize(QtCore.QSize(80, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboBox_4 = QtGui.QComboBox(self.groupBox)
        self.comboBox_4.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setDuplicatesEnabled(True)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.horizontalLayout_2.addWidget(self.comboBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setMinimumSize(QtCore.QSize(80, 0))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setMinimumSize(QtCore.QSize(120, 0))
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.horizontalLayout_3.addWidget(self.doubleSpinBox)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setMinimumSize(QtCore.QSize(80, 0))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_2.setMinimumSize(QtCore.QSize(120, 0))
        self.doubleSpinBox_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_2)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setMinimumSize(QtCore.QSize(80, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.dateEdit_2 = QtGui.QDateEdit(self.groupBox)
        self.dateEdit_2.setMinimumSize(QtCore.QSize(120, 0))
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.horizontalLayout_3.addWidget(self.dateEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setMinimumSize(QtCore.QSize(80, 0))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout.addWidget(self.label_11)
        self.comboBox_5 = QtGui.QComboBox(self.groupBox)
        self.comboBox_5.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_5.setEditable(True)
        self.comboBox_5.setDuplicatesEnabled(True)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.horizontalLayout.addWidget(self.comboBox_5)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setMinimumSize(QtCore.QSize(80, 0))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout.addWidget(self.label_12)
        self.comboBox_6 = QtGui.QComboBox(self.groupBox)
        self.comboBox_6.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_6.setEditable(True)
        self.comboBox_6.setDuplicatesEnabled(True)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.horizontalLayout.addWidget(self.comboBox_6)
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setMinimumSize(QtCore.QSize(80, 0))
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout.addWidget(self.label_13)
        self.comboBox_7 = QtGui.QComboBox(self.groupBox)
        self.comboBox_7.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_7.setEditable(True)
        self.comboBox_7.setDuplicatesEnabled(True)
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.horizontalLayout.addWidget(self.comboBox_7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_10 = QtGui.QLabel(FormDelivery)
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_4.addWidget(self.label_10)
        self.pushButton_2 = QtGui.QPushButton(FormDelivery)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(FormDelivery)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.horizontalLayout_4.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(FormDelivery)
        QtCore.QMetaObject.connectSlotsByName(FormDelivery)

    def retranslateUi(self, FormDelivery):
        FormDelivery.setWindowTitle(_translate("FormDelivery", "FormDelivery", None))
        self.groupBox.setTitle(_translate("FormDelivery", "发货记录/退货记录", None))
        self.label_9.setText(_translate("FormDelivery", "发货单号：", None))
        self.label_5.setText(_translate("FormDelivery", "客 户：", None))
        self.label_4.setText(_translate("FormDelivery", "物 料：", None))
        self.label_7.setText(_translate("FormDelivery", "单 价：", None))
        self.label_8.setText(_translate("FormDelivery", "金 额：", None))
        self.label_6.setText(_translate("FormDelivery", "日 期：", None))
        self.label_11.setText(_translate("FormDelivery", "收货人：", None))
        self.label_12.setText(_translate("FormDelivery", "业务员：", None))
        self.label_13.setText(_translate("FormDelivery", "记 录：", None))
        self.pushButton_2.setText(_translate("FormDelivery", "取 消", None))
        self.pushButton.setText(_translate("FormDelivery", "保 存", None))

