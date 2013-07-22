# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from .base.TableRecords_ui import Ui_TableRecords
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
    

class TableRecords(QtGui.QWidget,Ui_TableRecords):
    def __init__(self,target=None):
        super(TableRecords, self).__init__()
        self.setupUi(self)
    
    

