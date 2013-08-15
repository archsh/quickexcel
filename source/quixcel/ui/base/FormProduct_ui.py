# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/FormProduct.ui'
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

class Ui_FormProduct(object):
    def setupUi(self, FormProduct):
        FormProduct.setObjectName(_fromUtf8("FormProduct"))
        FormProduct.resize(234, 218)
        font = QtGui.QFont()
        font.setPointSize(10)
        FormProduct.setFont(font)
        self.verticalLayout_2 = QtGui.QVBoxLayout(FormProduct)
        self.verticalLayout_2.setMargin(3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(FormProduct)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setMinimumSize(QtCore.QSize(80, 0))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.comboBox_Model_Name = QtGui.QComboBox(self.groupBox)
        self.comboBox_Model_Name.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_Model_Name.setEditable(True)
        self.comboBox_Model_Name.setDuplicatesEnabled(True)
        self.comboBox_Model_Name.setObjectName(_fromUtf8("comboBox_Model_Name"))
        self.horizontalLayout_2.addWidget(self.comboBox_Model_Name)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setMinimumSize(QtCore.QSize(80, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBox_Model_Suffix = QtGui.QComboBox(self.groupBox)
        self.comboBox_Model_Suffix.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_Model_Suffix.setEditable(True)
        self.comboBox_Model_Suffix.setDuplicatesEnabled(True)
        self.comboBox_Model_Suffix.setObjectName(_fromUtf8("comboBox_Model_Suffix"))
        self.horizontalLayout_3.addWidget(self.comboBox_Model_Suffix)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setMinimumSize(QtCore.QSize(80, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.comboBox_Model_Suffix_2 = QtGui.QComboBox(self.groupBox)
        self.comboBox_Model_Suffix_2.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_Model_Suffix_2.setEditable(True)
        self.comboBox_Model_Suffix_2.setDuplicatesEnabled(True)
        self.comboBox_Model_Suffix_2.setObjectName(_fromUtf8("comboBox_Model_Suffix_2"))
        self.horizontalLayout_6.addWidget(self.comboBox_Model_Suffix_2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setMinimumSize(QtCore.QSize(80, 0))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.doubleSpinBox_Price = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_Price.setMinimumSize(QtCore.QSize(120, 0))
        self.doubleSpinBox_Price.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_Price.setObjectName(_fromUtf8("doubleSpinBox_Price"))
        self.horizontalLayout_5.addWidget(self.doubleSpinBox_Price)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setMinimumSize(QtCore.QSize(80, 0))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_10 = QtGui.QLabel(FormProduct)
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_4.addWidget(self.label_10)
        self.pushButton_Cancel = QtGui.QPushButton(FormProduct)
        self.pushButton_Cancel.setObjectName(_fromUtf8("pushButton_Cancel"))
        self.horizontalLayout_4.addWidget(self.pushButton_Cancel)
        self.pushButton_Save = QtGui.QPushButton(FormProduct)
        self.pushButton_Save.setObjectName(_fromUtf8("pushButton_Save"))
        self.horizontalLayout_4.addWidget(self.pushButton_Save)
        self.horizontalLayout_4.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(FormProduct)
        QtCore.QMetaObject.connectSlotsByName(FormProduct)

    def retranslateUi(self, FormProduct):
        FormProduct.setWindowTitle(_translate("FormProduct", "FormProduct", None))
        self.groupBox.setTitle(_translate("FormProduct", "产品信息：", None))
        self.label_5.setText(_translate("FormProduct", "主型号：", None))
        self.label_4.setText(_translate("FormProduct", "副型号：", None))
        self.label_6.setText(_translate("FormProduct", "扩展型号：", None))
        self.label_7.setText(_translate("FormProduct", "单 价：", None))
        self.label_8.setText(_translate("FormProduct", "备 注：", None))
        self.pushButton_Cancel.setText(_translate("FormProduct", "取 消 (&C)", None))
        self.pushButton_Save.setText(_translate("FormProduct", "保 存 (&S)", None))

