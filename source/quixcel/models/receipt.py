### Model of Receipt
from PyQt4 import QtCore
from .base import *
from .model import QuickTableModel

class ReceiptModel(QuickTableModel):
    def data(self, index, role):
        pass

class ReceiptSummaryModel(QtCore.QAbstractTableModel):
    pass