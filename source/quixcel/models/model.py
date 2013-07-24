from .base import *

from PyQt4 import QtCore

class QuickTableModel(QtCore.QAbstractTableModel):
    def __init__(self,parent=None, tabledef=None):
        super(QuickTableModel, self).__init__(parent)
        if not tabledef and not isinstance(tabledef,Base):
            raise Exception('Invalid tabledef.')
        self.tabledef = tabledef
        self.quick_session = get_db_session()
        self.columns = [(c.name,c.doc)for c in tabledef.__table__.columns][1:]
        self.query=None
        self.refresh()
        

    def rowCount(self, parent=None):
        return self.quick_session.query(self.tabledef).count()
    
    def columnCount(self, parent=None):
        return len(self.columns)

    def data(self, index, role):
        if not index.isValid():
            return None

        if role != QtCore.Qt.DisplayRole:
            return None

        #item = index.row()
        return '%s'%getattr(self.query_data[index.row()],self.columns[index.column()][0])

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.NoItemFlags
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable # | QtCore.Qt.ItemIsEditable

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section>=0 and section<len(self.columns):
                    return self.columns[section][1]
            else:
                return self.query_data[section].id
        return None

    def getIDFromText(self, text):
        return self.currentID(text)

    def index(self, row, column, parent):
        data = getattr(self.query_data[row],self.columns[column][0])
        return self.createIndex(row, column, data)

    def insertRows(self, row, count, parent):
        self.beginInsertRows(parent, row - 1, row - 1)
        self.query_data.insert(row, [0, ''])
        self.endInsertRows()
        return True

    def insertRecord(self, value):
        if self.insertSQL:
            connection, cursor = getPgCursor(self.dbInfo)
            try:
                try:
                    id = getNextVal(cursor, self.sequence)
                    sql = self.insertSQL % (id, value)
                    cursor.execute(sql)
                    connection.commit()
                finally:
                    connection.close()
            except:
                return (0, '')
            return id, value
        return (0, '')

    def parent(self, index):
        return QModelIndex()
  
    def refresh(self):
        self.query_data = self._query_data()

    def setData(self, index, value, role):
        id, value = self.insertRecord(str(value.toString()))
        if id:
            data = index.internalPointer()
            data[0] = id
            data[1] = value
            self.emit(SIGNAL('dataChanged(const QModelIndex &, '
              'const QModelIndex &)'), index, index)
            return True
        return False
    
    def setID(self, id):
        rowCount = 0
        for row in self.query_data:
            if row.id == id:
                return rowCount
            rowCount += 1
        return None
    
    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        print 'Sort by column(%d)'%Ncol, order
        self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
        reverse = True if order == Qt.DescendingOrder else False
        self.query_data = sorted(self.query_data, key=lambda x: getattr(x,self.columns[Ncol][0]),reverse=reverse)        
        self.emit(QtCore.SIGNAL("layoutChanged()"))
    
    def _query_data(self):
        return self.quick_session.query(self.tabledef).all()
    
