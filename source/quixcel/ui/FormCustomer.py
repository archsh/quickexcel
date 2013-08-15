# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from .base.FormCustomer_ui import Ui_FormCustomer
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
        super(FormCustomer, self).__init__()
        self.setupUi(self)

