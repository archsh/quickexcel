# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from .base.FormCustomer_ui import Ui_FormCustomer
from ..models.base import Customer, get_db_session

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
    
    def do_Remove(self):
        if self.customer:
            pass
    
    
    def do_Save(self):
        if self.customer:
            self.customer.name=unicode(self.lineEdit_Name.text())
            self.customer.short_name=unicode(self.lineEdit_Short_name.text())
            self.customer.address=unicode(self.lineEdit_Address.text())
            self.customer.email=unicode(self.lineEdit_Email.text())
            self.customer.contact=unicode(self.lineEdit_Contact.text())
            self.customer.telephone=unicode(self.lineEdit_Telephone.text())
            self.customer.cellphone=unicode(self.lineEdit_Cellphone.text())
            self.customer.comment=unicode(self.lineEdit_Comment.text())
            get_db_session().flush()
        else:
            self.customer = Customer(
                name=unicode(self.lineEdit_Name.text()),
                short_name=unicode(self.lineEdit_Short_name.text()),
                address=unicode(self.lineEdit_Address.text()),
                email=unicode(self.lineEdit_Email.text()),
                contact=unicode(self.lineEdit_Contact.text()),
                telephone=unicode(self.lineEdit_Telephone.text()),
                cellphone=unicode(self.lineEdit_Cellphone.text()),
                comment=unicode(self.lineEdit_Comment.text())
            )
            get_db_session().add(self.customer)
        get_db_session().commit()
        self.accept()
    
    def do_Cancel(self):
        self.reject()

