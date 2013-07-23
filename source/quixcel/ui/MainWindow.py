# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from .base.MainWindow_ui import Ui_MainWindow
from quixcel.models.base import get_db_session, setup_db_session, initialize_db

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class MainWindow(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,config='quickexcel.ini'):
        super(MainWindow, self).__init__()
        self.setupUi(self)
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
        QtCore.QObject.connect(self.action_Goods, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_Goods)
        QtCore.QObject.connect(self.action_Receipt, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_Receipt)
        QtCore.QObject.connect(self.action_ReceiptRecords, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_ReceiptRecords)
        QtCore.QObject.connect(self.action_ReceiptReport, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_ReceiptReport)
        QtCore.QObject.connect(self.action_ReceiptSheet, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_ReceiptSheet)
        QtCore.QObject.connect(self.action_ReceiptSummarize, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_ReceiptSummarize)
        QtCore.QObject.connect(self.action_Restore, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_Restore)
        QtCore.QObject.connect(self.action_Return, QtCore.SIGNAL(_fromUtf8("triggered()")), self.do_Return)
        self.config_file = config
        self.load_Config()
    
    def load_Config(self):
        import ConfigParser
        if self.config_file:
            reply = QtGui.QMessageBox.critical(self, "QMessageBox.critical()",
                    u"无效的配置文件！",
                    QtGui.QMessageBox.Abort)
            self.close()
        else:
            config = ConfigParser.ConfigParser()
            config.read(options.configfile)
        self.db_file = config.get('global','dbfile') if config.has_option('global','dbfile') else 'sqlite:///quickexcel.db'
        
    
    def do_Init(self):
        setup_db_session(self.db_file)
    
    
    def do_Configure(self):
        pass
    
    
    def do_About(self):
        pass
    
    def do_Backup(self):
        pass
    
    def do_Changepassword(self):
        pass
    
    def do_Customers(self):
        pass
    
    def do_DataExport(self):
        pass
    
    def do_DataImport(self):
        pass
    
    def do_Deliver(self):
        pass
    
    def do_DeliveryRecords(self):
        pass
    
    def do_DeliveryReport(self):
        pass
    
    def do_DeliverySummarize(self):
        pass
    
    def do_Employees(self):
        pass
    
    def do_Exit(self):
        self.close()
    
    def do_Goods(self):
        pass
    
    def do_Receipt(self):
        pass
    
    def do_ReceiptRecords(self):
        pass
    
    def do_ReceiptReport(self):
        pass
    
    def do_ReceiptSheet(self):
        pass
    
    def do_ReceiptSummarize(self):
        pass
    
    def do_Restore(self):
        pass
    
    def do_Return(self):
        pass
    
    
    

