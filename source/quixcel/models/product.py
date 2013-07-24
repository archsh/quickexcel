### Model of Product

from .base import *
from .model import QuickTableModel

class ProductModel(QuickTableModel):
    def data(self, index, role):
        pass