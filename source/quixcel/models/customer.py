### Model of Customer

from .base import *

from PyQt4 import QtCore

class QuickItem(object):
    def __init__(self, inst=None):
        pass
    


class QuickTableModel(QtCore.QAbstractTableModel):
    def __init__(self,tabledef=None):
        super(CustomerModel, self).__init__()
        if not tabledef and not isinstance(tabledef,Base):
            raise Exception('Invalid tabledef.')
        self.tabledef = tabledef
        self.quick_session = get_db_session()

    def rowCount(self, parent=None):
        return self.quick_session.query(self.tabledef).count()
    
    def columnCount(self, parent=None):
        return self.quick_session.query(self.tabledef).count()

    def data(self, index, role):
        if not index.isValid():
            return None

        if role != QtCore.Qt.DisplayRole:
            return None

        item = index.internalPointer()

        node = item.node()
        attributes = []
        attributeMap = node.attributes()

        if index.column() == 0:
            return node.nodeName()
        
        elif index.column() == 1:
            for i in range(0, attributeMap.count()):
                attribute = attributeMap.item(i)
                attributes.append(attribute.nodeName() + '="' +
                                  attribute.nodeValue() + '"')

            return " ".join(attributes)

        if index.column() == 2:
            value = node.nodeValue()
            if value is None:
                return ''

            return ' '.join(node.nodeValue().split('\n'))

        return None

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.NoItemFlags
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            if section == 0:
                return "Name"

            if section == 1:
                return "Attributes"

            if section == 2:
                return "Value"

        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()
