### Model of Employee

from .base import *
from .model import QuickTableModel

class EmployeeModel(QuickTableModel):
    def data(self, index, role):
        pass