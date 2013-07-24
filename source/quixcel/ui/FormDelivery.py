# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from .base.FormDelivery_ui import Ui_FormDelivery
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
    
class FormDelivery(QtGui.QWidget,Ui_FormDelivery):
    def __init__(self,delivery=None):
        super(FormDelivery, self).__init__()
        self.setupUi(self)

