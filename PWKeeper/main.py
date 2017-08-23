import sys
from PyQt4 import QtGui
from gui.PWKeeper import PWKeeper

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    pwk = PWKeeper()
    sys.exit(app.exec_())