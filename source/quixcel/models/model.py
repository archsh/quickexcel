from .base import *

from PyQt4 import QtCore

class QuickTableModel(QtCore.QAbstractTableModel):
    def __init__(self,parent=None, tabledef=None):
        super(QuickTableModel, self).__init__(parent)
        if not tabledef and not isinstance(tabledef,Base):
            raise Exception('Invalid tabledef.')
        self.tabledef = tabledef
        self.quick_session = get_db_session()
        self.columns = [(c.name,c.doc,c)for c in tabledef.__table__.columns][1:]
        self.query=None
        self.refresh()
        

    def rowCount(self, parent=None):
        return self.quick_session.query(self.tabledef).count()
    
    def columnCount(self, parent=None):
        return len(self.columns)

    def data(self, index, role):
        #print 'index:',index, 'role:',role
        if not index.isValid():
            return None
        if role == QtCore.Qt.DisplayRole:
            return '%s'%getattr(self.query_data[index.row()],self.columns[index.column()][0])
        elif role == QtCore.Qt.TextAlignmentRole:
            clmn = self.columns[index.column()][2]
            #print 'Column Type:', clmn.type.__class__.__name__
            if clmn.type.__class__.__name__ in ('INTEGER','NUMERIC'):
                return QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter
            else:
                return QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter
        else:
            return None
    
    def get(self,index,*fields):
        if not index.isValid():
            return None
        else:
            obj = self.query_data[index.row()]
            if not fields:
                return obj
            else:
                for f in fields:
                    pass
                

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
        elif role==QtCore.Qt.TextAlignmentRole:
                return QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter
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

    def parent(self, index):
        return QModelIndex()
  
    def refresh(self):
        self.beginResetModel()
        self.query_data = self._query_data()
        self.endResetModel()
        #self.emit(QtCore.SIGNAL('dataChanged(const QModelIndex &, '
        #      'const QModelIndex &)'), None, None)
        #self.emit(QtCore.SIGNAL("layoutChanged()"))
    
    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        print 'Sort by column(%d)'%Ncol, order
        self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
        reverse = True if order == QtCore.Qt.DescendingOrder else False
        self.query_data = sorted(self.query_data, key=lambda x: getattr(x,self.columns[Ncol][0]),reverse=reverse)        
        self.emit(QtCore.SIGNAL("layoutChanged()"))
    
    def _query_data(self):
        return self.quick_session.query(self.tabledef).all()
    
    
    def set_num_per_page(self, num=25):
        self.num_per_page = num
    
    def go_page(self, num=0):
        pass
    
    def get_pages(self):
        pass
    
    def get_page(self):
        pass
    
    
    
    
    
    
