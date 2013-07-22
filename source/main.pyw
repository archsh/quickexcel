#!/usr/bin/env python

###### 
from PyQt4 import QtCore, QtGui

if __name__ == '__main__':

    import sys
    from ui.MainWindow import MainWindow

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.resize(1024, 680)
    window.show()
    sys.exit(app.exec_())