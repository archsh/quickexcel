# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from .base.FormCustomer_ui import Ui_FormCustomer
from ..models.base import Customer

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
    
class FormCustomer(QtGui.QDialog,Ui_FormCustomer):
    def __init__(self,customer=None):
        assert customer is None or isinstance(customer,Customer)
        self.customer = customer
        super(FormCustomer, self).__init__()
        self.setupUi(self)
        QtCore.QObject.connect(self.pushButton_Save, QtCore.SIGNAL(_fromUtf8("clicked()")), self.do_Save)
        QtCore.QObject.connect(self.pushButton_Cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), self.do_Cancel)
    
    def do_Save(self):
        if not self.customer:
            self.customer.name=1
            self.customer.short_name=2
            self.customer.address=3
            self.customer.email=4
            self.customer.contact=5
            self.customer.telephone=6
            self.customer.cellphone=7
            self.customer.comment=8
        else:
            self.customer = Customer(
                name=1,
                short_name=2,
                address=3,
                email=4,
                contact=5,
                telephone=6,
                cellphone=7,
                comment=8
            )
    
    def do_Cancel(self):
        self.close()

