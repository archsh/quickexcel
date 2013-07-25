# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from .base.TableSummaries_ui import Ui_TableSummaries
from ..models.model import QuickTableModel
from ..models.base import Customer, Employee, Product, Delivery, Receipt
from .Charts import PieView
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

class TableSummaries(QtGui.QWidget,Ui_TableSummaries):
    def setupModel(self):
        if self._target=='DeliverySummary':
            self._model = QuickTableModel(tabledef=Delivery,parent=self.tableView_Records)
        elif self._target=='ReceiptSummary':
            self._model = QuickTableModel(tabledef=Receipt,parent=self.tableView_Records)
        proxyModel = QtGui.QSortFilterProxyModel()
        proxyModel.setSourceModel(self._model);
        self.tableView_Records.setModel(self._model)
        self.tableView_Records.setSortingEnabled(True)
        self.tableView_Records.resizeColumnsToContents()
        self.widget_Chart.setModel(self._model)

        self.selectionModel = QtGui.QItemSelectionModel(self._model)
        self.tableView_Records.setSelectionModel(self.selectionModel)
        self.widget_Chart.setSelectionModel(self.selectionModel)

        self.tableView_Records.horizontalHeader().setStretchLastSection(True)
        #self.tableView_Records.setSelectionBehavior(QAbstractItemView.SelectRows)
    
    def __init__(self,target='DeliveryList',rootwin=None):
        if target not in ('DeliverySummary','ReceiptSummary',):# 
            raise Exception('Wrong target.')
        if not rootwin:
            raise Exception('Rootwin should provided.')
        self._target  = target
        self._rootwin = rootwin
        super(TableSummaries, self).__init__()
        self.setupUi(self)
        
        if target=='DeliverySummary':
            self.setWindowTitle(u"发货汇总")
            self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_119_table.png")))
            self.label_Title.setText(_translate("TableRecords", "发货汇总", None))
        elif target=='ReceiptSummary':
            self.setWindowTitle(u"收款汇总")
            self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_325_wallet.png")))
            self.label_Title.setText(_translate("TableRecords", "收款汇总", None))
        self.setupModel()
        
        QtCore.QObject.connect(self.comboBox_ChartType, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.do_Change_ChartType)
        QtCore.QObject.connect(self.pushButton_ExportImage, QtCore.SIGNAL(_fromUtf8("clicked()")), self.do_ExportImage)
        QtCore.QObject.connect(self.pushButton_Filter, QtCore.SIGNAL(_fromUtf8("clicked()")), self.do_Filter)
        QtCore.QObject.connect(self.pushButton_Print, QtCore.SIGNAL(_fromUtf8("clicked()")), self.do_Print)
    
    def do_Print(self):
        pass
        
    def do_Filter(self):
        pass
        
    def do_ExportImage(self):
        pass
    
    def do_Change_ChartType(self,num):
        pass

