### Model of Delivery
from PyQt4 import QtCore
from .base import *
from .model import QuickTableModel

class DeliveryModel(QuickTableModel):
    def data(self, index, role):
        pass

class DeliverySummaryModel(QtCore.QAbstractTableModel):
    pass
