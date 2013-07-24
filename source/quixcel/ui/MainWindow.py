# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from .base.MainWindow_ui import Ui_MainWindow
from quixcel.models.base import get_db_session, setup_db_session, initialize_db
from .TableRecords import TableRecords
from .TableSummaries import TableSummaries

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class MainWindow(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,config='quickexcel.ini'):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.mdiArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.setCentralWidget(self.mdiArea)
        #self.mdiArea.subWindowActivated.connect(self.updateMenus)
        self.windowMapper = QtCore.QSignalMapper(self)
        self.windowMapper.mapped[QtGui.QWidget].connect(self.setActiveSubWindow)
        QtCore.QObject.connect(self.action_About, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_About)
        QtCore.QObject.connect(self.action_Backup, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_Backup)
        QtCore.QObject.connect(self.action_Changepassword, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_Changepassword)
        QtCore.QObject.connect(self.action_Customers, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_Customers)
        QtCore.QObject.connect(self.action_DataExport, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_DataExport)
        QtCore.QObject.connect(self.action_DataImport, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_DataImport)
        QtCore.QObject.connect(self.action_Deliver, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_Deliver)
        QtCore.QObject.connect(self.action_DeliveryRecords, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_DeliveryRecords)
        QtCore.QObject.connect(self.action_DeliveryReport, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_DeliveryReport)
        QtCore.QObject.connect(self.action_DeliverySummarize, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_DeliverySummarize)
        QtCore.QObject.connect(self.action_Employees, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_Employees)
        QtCore.QObject.connect(self.action_Exit, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_Exit)
        QtCore.QObject.connect(self.action_Products, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_Products)
        QtCore.QObject.connect(self.action_Receipt, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_Receipt)
        QtCore.QObject.connect(self.action_ReceiptRecords, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_ReceiptRecords)
        QtCore.QObject.connect(self.action_ReceiptReport, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_ReceiptReport)
        QtCore.QObject.connect(self.action_ReceiptSheet, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_ReceiptSheet)
        QtCore.QObject.connect(self.action_ReceiptSummarize, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_ReceiptSummarize)
        QtCore.QObject.connect(self.action_Restore, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_Restore)
        QtCore.QObject.connect(self.action_Return, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_Return)
        self.config_file = config
        self.load_Config()
    
    def setActiveSubWindow(self, window):
        if window:
            self.mdiArea.setActiveSubWindow(window)
    
    def load_Config(self):
        import ConfigParser
        if not self.config_file:
            reply = QtGui.QMessageBox.critical(self, "QMessageBox.critical()",
                    u"无效的配置文件！",
                    QtGui.QMessageBox.Abort)
            self.close()
        else:
            config = ConfigParser.ConfigParser()
            config.read(self.config_file)
        self.db_uri = config.get('global','db_uri') if config.has_option('global','db_uri') else 'sqlite:///quickexcel.db'
        print 'DB URL:', self.db_uri
        self.do_Init()
        
    
    def do_Init(self):
        setup_db_session(self.db_uri)
        initialize_db()
        pass
    
    
    def do_Configure(self):
        pass
    
    
    def do_About(self):
        pass
    
    def do_Backup(self):
        pass
    
    def do_Changepassword(self):
        pass
    
    def do_Customers(self):
        for subwin in self.mdiArea.subWindowList():
            if isinstance(subwin.widget(),TableRecords) and subwin.widget()._target=='CustomerList':
                subwin.showMaximized()
                return
        else:
            child = TableRecords(target='CustomerList',rootwin=self)
            self.mdiArea.addSubWindow(child)
            child.showMaximized()
    
    def do_DataExport(self):
        pass
    
    def do_DataImport(self):
        pass
    
    def do_Deliver(self):
        pass
    
    def do_DeliveryRecords(self):
        print 'do_DeliveryRecords'
        for subwin in self.mdiArea.subWindowList():
            if isinstance(subwin.widget(),TableRecords) and subwin.widget()._target=='DeliveryList':
                subwin.showMaximized()
                return
        else:
            child = TableRecords(target='DeliveryList',rootwin=self)
            self.mdiArea.addSubWindow(child)
            child.showMaximized()
    
    def do_DeliveryReport(self):
        pass
    
    def do_DeliverySummarize(self):
        print 'do_DeliverySummarize'
        for subwin in self.mdiArea.subWindowList():
            if isinstance(subwin.widget(),TableSummaries) and subwin.widget()._target=='DeliverySummary':
                subwin.showMaximized()
                return
        else:
            child = TableSummaries(target='DeliverySummary',rootwin=self)
            self.mdiArea.addSubWindow(child)
            child.showMaximized()
    
    def do_Employees(self):
        for subwin in self.mdiArea.subWindowList():
            if isinstance(subwin.widget(),TableRecords) and subwin.widget()._target=='EmployeeList':
                subwin.showMaximized()
                return
        else:
            child = TableRecords(target='EmployeeList',rootwin=self)
            self.mdiArea.addSubWindow(child)
            child.showMaximized()
    
    def do_Exit(self):
        self.close()
    
    def do_Products(self):
        for subwin in self.mdiArea.subWindowList():
            if isinstance(subwin.widget(),TableRecords) and subwin.widget()._target=='ProductList':
                subwin.showMaximized()
                return
        else:
            child = TableRecords(target='ProductList',rootwin=self)
            self.mdiArea.addSubWindow(child)
            child.showMaximized()
    
    def do_Receipt(self):
        pass
    
    def do_ReceiptRecords(self):
        print 'do_ReceiptRecords'
        for subwin in self.mdiArea.subWindowList():
            if isinstance(subwin.widget(),TableRecords) and subwin.widget()._target=='ReceiptList':
                subwin.showMaximized()
                return
        else:
            child = TableRecords(target='ReceiptList',rootwin=self)
            self.mdiArea.addSubWindow(child)
            child.showMaximized()
    
    def do_ReceiptReport(self):
        pass
    
    def do_ReceiptSheet(self):
        pass
    
    def do_ReceiptSummarize(self):
        print 'do_ReceiptSummarize'
        for subwin in self.mdiArea.subWindowList():
            if isinstance(subwin.widget(),TableSummaries) and subwin.widget()._target=='ReceiptSummary':
                subwin.showMaximized()
                return
        else:
            child = TableSummaries(target='ReceiptSummary',rootwin=self)
            self.mdiArea.addSubWindow(child)
            child.showMaximized()
    
    def do_Restore(self):
        pass
    
    def do_Return(self):
        pass
    
    
    

