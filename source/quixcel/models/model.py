from .base import *

from PyQt4 import QtCore

class QuickTableModel(QtCore.QAbstractTableModel):
    def __init__(self,parent=None, tabledef=None):
        super(QuickTableModel, self).__init__(parent)
        if not tabledef and not isinstance(tabledef,Base):
            raise Exception('Invalid tabledef.')
        self.tabledef = tabledef
        self.quick_session = get_db_session()
        self.columns = [(c.name,c.doc)for c in tabledef.__table__.columns]
        self.query=None
        

    def rowCount(self, parent=None):
        return self.quick_session.query(self.tabledef).count()
    
    def columnCount(self, parent=None):
        return len(self.columns)

    def data(self, index, role):
        if not index.isValid():
            return None

        if role != QtCore.Qt.DisplayRole:
            return None

        item = index.internalPointer()
        return getattr(item,self.columns[index.column()][0])

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.NoItemFlags
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            if section>=0 and section<len(self.columns):
                return self.columns[section][1]
        return None

