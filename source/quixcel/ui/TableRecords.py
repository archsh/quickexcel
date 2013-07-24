# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from .base.TableRecords_ui import Ui_TableRecords
from ..models.model import QuickTableModel
from ..models.base import Customer, Employee, Product, Delivery, Receipt
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

class TableRecords(QtGui.QWidget,Ui_TableRecords):
    def setupModel(self):
        if self._target=='DeliveryList':
            self._model = QuickTableModel(tabledef=Delivery,parent=self.tableView_Records)
        elif self._target=='DeliverySummary':
            self._model = QuickTableModel(tabledef=Delivery,parent=self.tableView_Records)
        elif self._target=='ReceiptList':
            self._model = QuickTableModel(tabledef=Receipt,parent=self.tableView_Records)
        elif self._target=='ReceiptSummary':
            self._model = QuickTableModel(tabledef=Receipt,parent=self.tableView_Records)
        elif self._target=='EmployeeList':
            self._model = QuickTableModel(tabledef=Employee,parent=self.tableView_Records)
        elif self._target=='CustomerList':
            self._model = QuickTableModel(tabledef=Customer,parent=self.tableView_Records)
        elif self._target=='ProductList':
            self._model = QuickTableModel(tabledef=Product,parent=self.tableView_Records)
        proxyModel = QtGui.QSortFilterProxyModel()
        proxyModel.setSourceModel(self._model);
        self.tableView_Records.setModel(proxyModel)
        self.tableView_Records.setSortingEnabled(True)
        self.tableView_Records.resizeColumnsToContents()
        #self.tableView_Records.setSelectionBehavior(QAbstractItemView.SelectRows)
    
    def __init__(self,target='DeliveryList',rootwin=None):
        if target not in ('DeliveryList','DeliverySummary','ReceiptList','ReceiptSummary','EmployeeList','CustomerList','ProductList'):
            raise Exception('Wrong target.')
        if not rootwin:
            raise Exception('Rootwin should provided.')
        self._target  = target
        self._rootwin = rootwin
        super(TableRecords, self).__init__()
        self.setupUi(self)
        self.pushButton_Delete.setEnabled(False)
        self.pushButton_Last10Page.setEnabled(False)
        self.pushButton_LastPage.setEnabled(False)
        self.pushButton_Modify.setEnabled(False)
        self.pushButton_Next10Page.setEnabled(False)
        self.pushButton_NextPage.setEnabled(False)
        
        if target=='DeliveryList':
            self.setWindowTitle(u"发货记录")
            self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_114_list.png")))
            self.label_Title.setText(_translate("TableRecords", "发货记录", None))
        elif target=='DeliverySummary':
            self.setWindowTitle(u"发货汇总")
            self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_119_table.png")))
            self.label_Title.setText(_translate("TableRecords", "发货汇总", None))
        elif target=='ReceiptList':
            self.setWindowTitle(u"收款记录")
            self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_113_justify.png")))
            self.label_Title.setText(_translate("TableRecords", "收款记录", None))
        elif target=='ReceiptSummary':
            self.setWindowTitle(u"收款汇总")
            self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_325_wallet.png")))
            self.label_Title.setText(_translate("TableRecords", "收款汇总", None))
        elif target=='EmployeeList':
            self.setWindowTitle(u"业务列表")
            self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_043_group.png")))
            self.label_Title.setText(_translate("TableRecords", "业务列表", None))
        elif target=='CustomerList':
            self.setWindowTitle(u"客户列表")
            self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_024_parents.png")))
            self.label_Title.setText(_translate("TableRecords", "客户列表", None))
        elif target=='ProductList':
            self.setWindowTitle(u"产品列表")
            self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_149_folder_new.png")))
            self.label_Title.setText(_translate("TableRecords", "产品列表", None))
        self.setupModel()
        QtCore.QObject.connect(self.pushButton_Delete, QtCore.SIGNAL(_fromUtf8("clicked()")), self.do_Delete)
        QtCore.QObject.connect(self.pushButton_Filter, QtCore.SIGNAL(_fromUtf8("clicked()")), self.do_Filter)
        QtCore.QObject.connect(self.pushButton_Last10Page, QtCore.SIGNAL(_fromUtf8("clicked()")), self.do_Last10Page)
        QtCore.QObject.connect(self.pushButton_LastPage, QtCore.SIGNAL(_fromUtf8("clicked()")), self.do_LastPage)
        QtCore.QObject.connect(self.pushButton_Modify, QtCore.SIGNAL(_fromUtf8("clicked()")), self.do_Modify)
        QtCore.QObject.connect(self.pushButton_New, QtCore.SIGNAL(_fromUtf8("clicked()")), self.do_New)
        QtCore.QObject.connect(self.pushButton_Next10Page, QtCore.SIGNAL(_fromUtf8("clicked()")), self.do_Next10Page)
        QtCore.QObject.connect(self.pushButton_NextPage, QtCore.SIGNAL(_fromUtf8("clicked()")), self.do_NextPage)
        QtCore.QObject.connect(self.pushButton_Reload, QtCore.SIGNAL(_fromUtf8("clicked()")), self.do_Reload)
        QtCore.QObject.connect(self.comboBox_NumPerPage, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.do_Change_NumPerPage)
        
    def do_Delete(self):
        pass
        
    def do_Filter(self):
        pass
        
    def do_Last10Page(self):
        pass
    
    def do_LastPage(self):
        pass
    
    def do_Modify(self):
        pass
    
    def do_New(self):
        pass
    
    def do_Next10Page(self):
        pass
    
    def do_NextPage(self):
        pass
    
    def do_Reload(self):
        pass
    
    def do_Change_NumPerPage(self,num):
        pass
    
    

    
    
    
    
    
        
        
        
    
    

