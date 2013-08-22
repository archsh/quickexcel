# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from .base.TableRecords_ui import Ui_TableRecords
from ..models.model import QuickTableModel
from ..models.base import Customer, Employee, Product, Delivery, Receipt
from .FormCustomer import FormCustomer
from .FormDelivery import FormDelivery
from .FormEmployee import FormEmployee
from .FormProduct import FormProduct
from .FormReceipt import FormReceipt
from quixcel.models.base import get_db_session

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
        #elif self._target=='DeliverySummary':
        #    self._model = QuickTableModel(tabledef=Delivery,parent=self.tableView_Records)
        elif self._target=='ReceiptList':
            self._model = QuickTableModel(tabledef=Receipt,parent=self.tableView_Records)
        #elif self._target=='ReceiptSummary':
        #    self._model = QuickTableModel(tabledef=Receipt,parent=self.tableView_Records)
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
        #selectionModel = QtGui.QItemSelectionModel(proxyModel)
        #self.tableView_Records.setSelectionModel(selectionModel)
        self.tableView_Records.setSelectionMode(QtGui.QTableView.SingleSelection)
        self.tableView_Records.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.selectionModel = self.tableView_Records.selectionModel()
    
    def __init__(self,target='DeliveryList',rootwin=None):
        if target not in ('DeliveryList','ReceiptList','EmployeeList','CustomerList','ProductList'):# 'DeliverySummary','ReceiptSummary',
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
        #elif target=='DeliverySummary':
        #    self.setWindowTitle(u"发货汇总")
        #    self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_119_table.png")))
        #    self.label_Title.setText(_translate("TableRecords", "发货汇总", None))
        elif target=='ReceiptList':
            self.setWindowTitle(u"收款记录")
            self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_113_justify.png")))
            self.label_Title.setText(_translate("TableRecords", "收款记录", None))
        #elif target=='ReceiptSummary':
        #    self.setWindowTitle(u"收款汇总")
        #    self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_325_wallet.png")))
        #    self.label_Title.setText(_translate("TableRecords", "收款汇总", None))
        elif target=='EmployeeList':
            self.setWindowTitle(u"业务员资料")
            self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_043_group.png")))
            self.label_Title.setText(_translate("TableRecords", "业务员资料", None))
        elif target=='CustomerList':
            self.setWindowTitle(u"客户资料")
            self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_024_parents.png")))
            self.label_Title.setText(_translate("TableRecords", "客户资料", None))
        elif target=='ProductList':
            self.setWindowTitle(u"产品资料")
            self.label_Icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/glyphicons_149_folder_new.png")))
            self.label_Title.setText(_translate("TableRecords", "产品资料", None))
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
        #QtCore.QObject.connect(self.tableView_Records, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.do_SelectionChanged)
        #QtCore.QObject.connect(self.selectionModel, QtCore.SIGNAL(_fromUtf8("selectionChanged(QItemSelection, QItemSelection)")), self.do_SelectionChanged)
        #QtCore.QObject.connect(self.selectionModel, QtCore.SIGNAL(_fromUtf8("currentRowChanged(QItemSelection, QItemSelection)")), self.do_SelectionChanged)
        self.tableView_Records.selectionModel().currentRowChanged.connect(self.do_SelectionChanged)

        
    
    def do_SelectionChanged(self,selectedIndex, deselectedIndex):
        print 'Selected:',selectedIndex
        print 'Deselected:',deselectedIndex
        if selectedIndex:
            self.pushButton_Modify.setEnabled(True)
            self.pushButton_Delete.setEnabled(True)
        else:
            self.pushButton_Modify.setEnabled(False)
            self.pushButton_Delete.setEnabled(False)
        obj = self._model.get(self.tableView_Records.model().mapToSource(selectedIndex))
        print 'Selected Object:', obj.id, obj.name
        
    def do_Delete(self):
        print 'do_Delete'
        obj = self._model.get(self.tableView_Records.model().mapToSource(self.tableView_Records.selectedIndexes()[0]))
        if not obj:
            return
        else:
            reply = QtGui.QMessageBox.question(self, u"确定删除吗？",
                u"确定要删除这条记录吗？",
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)
            if reply == QtGui.QMessageBox.Yes:
                #self.tableView_Records.model().removeRows(self.tableView_Records.selectedIndexes()[0].row(),1)
                #self.tableView_Records.selectedIndexes()[0]
                get_db_session().delete(obj)
                self._model.refresh()
                self.pushButton_Modify.setEnabled(False)
                self.pushButton_Delete.setEnabled(False)
            else:
                return
        
    def do_Filter(self):
        print 'do_Filter'
        
    def do_Last10Page(self):
        print 'do_Last10Page'
    
    def do_LastPage(self):
        print 'do_LastPage'
    
    def do_Modify(self):
        print 'do_Modify'
        obj = self._model.get(self.tableView_Records.model().mapToSource(self.tableView_Records.selectedIndexes()[0]))
        if not obj:
            return
        if self._target=='DeliveryList':
            #self._model = QuickTableModel(tabledef=Delivery,parent=self.tableView_Records)
            dlg = FormDelivery(obj)
        #elif self._target=='DeliverySummary':
        #    self._model = QuickTableModel(tabledef=Delivery,parent=self.tableView_Records)
        elif self._target=='ReceiptList':
            #self._model = QuickTableModel(tabledef=Receipt,parent=self.tableView_Records)
            dlg = FormReceipt(obj)
        #elif self._target=='ReceiptSummary':
        #    self._model = QuickTableModel(tabledef=Receipt,parent=self.tableView_Records)
        elif self._target=='EmployeeList':
            #self._model = QuickTableModel(tabledef=Employee,parent=self.tableView_Records)
            dlg = FormEmployee(obj)
        elif self._target=='CustomerList':
            #self._model = QuickTableModel(tabledef=Customer,parent=self.tableView_Records)
            dlg = FormCustomer(obj)
        elif self._target=='ProductList':
            #self._model = QuickTableModel(tabledef=Product,parent=self.tableView_Records)
            dlg = FormProduct(obj)
        ret = dlg.exec_()
        if ret:
            self.do_Reload()
    
    def do_New(self):
        if self._target=='DeliveryList':
            #self._model = QuickTableModel(tabledef=Delivery,parent=self.tableView_Records)
            dlg = FormDelivery()
        #elif self._target=='DeliverySummary':
        #    self._model = QuickTableModel(tabledef=Delivery,parent=self.tableView_Records)
        elif self._target=='ReceiptList':
            #self._model = QuickTableModel(tabledef=Receipt,parent=self.tableView_Records)
            dlg = FormReceipt()
        #elif self._target=='ReceiptSummary':
        #    self._model = QuickTableModel(tabledef=Receipt,parent=self.tableView_Records)
        elif self._target=='EmployeeList':
            #self._model = QuickTableModel(tabledef=Employee,parent=self.tableView_Records)
            dlg = FormEmployee()
        elif self._target=='CustomerList':
            #self._model = QuickTableModel(tabledef=Customer,parent=self.tableView_Records)
            dlg = FormCustomer()
        elif self._target=='ProductList':
            #self._model = QuickTableModel(tabledef=Product,parent=self.tableView_Records)
            dlg = FormProduct()
        ret = dlg.exec_()
        if ret:
            self.do_Reload()
        #print 'Ret:',ret
    
    def do_Next10Page(self):
        print 'do_Next10Page'
    
    def do_NextPage(self):
        print 'do_NextPage'
    
    def do_Reload(self):
        self._model.refresh()
        self.pushButton_Modify.setEnabled(False)
        self.pushButton_Delete.setEnabled(False)
    
    def do_Change_NumPerPage(self,num):
        print 'do_Change_NumPerPage'
    
    

    
    
    
    
    
        
        
        
    
    

