# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/TableSummaries.ui'
#
# Created: Wed Jul 24 20:17:33 2013
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

class Ui_TableSummaries(object):
    def setupUi(self, TableSummaries):
        TableSummaries.setObjectName(_fromUtf8("TableSummaries"))
        TableSummaries.resize(957, 456)
        self.verticalLayout = QtGui.QVBoxLayout(TableSummaries)
        self.verticalLayout.setMargin(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_Icon = QtGui.QLabel(TableSummaries)
        self.label_Icon.setText(_fromUtf8(""))
        self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_072_bookmark.png")))
        self.label_Icon.setObjectName(_fromUtf8("label_Icon"))
        self.horizontalLayout.addWidget(self.label_Icon)
        self.label_Title = QtGui.QLabel(TableSummaries)
        self.label_Title.setObjectName(_fromUtf8("label_Title"))
        self.horizontalLayout.addWidget(self.label_Title)
        self.label_FilterMask = QtGui.QLabel(TableSummaries)
        self.label_FilterMask.setText(_fromUtf8(""))
        self.label_FilterMask.setAlignment(QtCore.Qt.AlignCenter)
        self.label_FilterMask.setObjectName(_fromUtf8("label_FilterMask"))
        self.horizontalLayout.addWidget(self.label_FilterMask)
        self.label = QtGui.QLabel(TableSummaries)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_ChartType = QtGui.QComboBox(TableSummaries)
        self.comboBox_ChartType.setFrame(False)
        self.comboBox_ChartType.setObjectName(_fromUtf8("comboBox_ChartType"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_042_pie_chart.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_ChartType.addItem(icon, _fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_040_stats.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_ChartType.addItem(icon1, _fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_041_charts.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_ChartType.addItem(icon2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox_ChartType)
        self.pushButton_Filter = QtGui.QPushButton(TableSummaries)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_027_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Filter.setIcon(icon3)
        self.pushButton_Filter.setFlat(False)
        self.pushButton_Filter.setObjectName(_fromUtf8("pushButton_Filter"))
        self.horizontalLayout.addWidget(self.pushButton_Filter)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtGui.QFrame(TableSummaries)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.splitter = QtGui.QSplitter(TableSummaries)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(QtGui.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtGui.QFrame.Plain)
        self.splitter.setMidLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.tableView_Records = QtGui.QTableView(self.splitter)
        self.tableView_Records.setMinimumSize(QtCore.QSize(250, 200))
        self.tableView_Records.setObjectName(_fromUtf8("tableView_Records"))
        self.widget_Chart = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_Chart.sizePolicy().hasHeightForWidth())
        self.widget_Chart.setSizePolicy(sizePolicy)
        self.widget_Chart.setMinimumSize(QtCore.QSize(250, 200))
        self.widget_Chart.setObjectName(_fromUtf8("widget_Chart"))
        self.verticalLayout.addWidget(self.splitter)
        self.line = QtGui.QFrame(TableSummaries)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(TableSummaries)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton_Print = QtGui.QPushButton(TableSummaries)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_015_print.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Print.setIcon(icon4)
        self.pushButton_Print.setObjectName(_fromUtf8("pushButton_Print"))
        self.horizontalLayout_2.addWidget(self.pushButton_Print)
        self.pushButton_ExportImage = QtGui.QPushButton(TableSummaries)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_138_picture.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ExportImage.setIcon(icon5)
        self.pushButton_ExportImage.setObjectName(_fromUtf8("pushButton_ExportImage"))
        self.horizontalLayout_2.addWidget(self.pushButton_ExportImage)
        self.pushButton_ExportExcel = QtGui.QPushButton(TableSummaries)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_119_table.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ExportExcel.setIcon(icon6)
        self.pushButton_ExportExcel.setObjectName(_fromUtf8("pushButton_ExportExcel"))
        self.horizontalLayout_2.addWidget(self.pushButton_ExportExcel)
        self.horizontalLayout_2.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(TableSummaries)
        QtCore.QMetaObject.connectSlotsByName(TableSummaries)

    def retranslateUi(self, TableSummaries):
        TableSummaries.setWindowTitle(_translate("TableSummaries", "TableSummaries", None))
        self.label_Title.setText(_translate("TableSummaries", "发货记录", None))
        self.label.setText(_translate("TableSummaries", "图表类型：", None))
        self.comboBox_ChartType.setItemText(0, _translate("TableSummaries", "饼图", None))
        self.comboBox_ChartType.setItemText(1, _translate("TableSummaries", "趋势图", None))
        self.comboBox_ChartType.setItemText(2, _translate("TableSummaries", "柱状图", None))
        self.pushButton_Filter.setText(_translate("TableSummaries", "筛选 (&F)", None))
        self.pushButton_Filter.setShortcut(_translate("TableSummaries", "F3", None))
        self.pushButton_Print.setText(_translate("TableSummaries", "打印 (&P)", None))
        self.pushButton_Print.setShortcut(_translate("TableSummaries", "Ctrl+P", None))
        self.pushButton_ExportImage.setText(_translate("TableSummaries", "导出图片 (&M)", None))
        self.pushButton_ExportImage.setShortcut(_translate("TableSummaries", "Ctrl+M", None))
        self.pushButton_ExportExcel.setText(_translate("TableSummaries", "导出表格 (&X)", None))
        self.pushButton_ExportExcel.setShortcut(_translate("TableSummaries", "Ctrl+X", None))

import resource_rc
