# -*- coding: utf-8 -×-

from PyQt4 import QtGui

class PWKeeper(QtGui.QMainWindow):

    def __init__(self):
        super(PWKeeper, self).__init__()
        self.initToolBar()
        self.initDB()
        self.initGrid()

        self.current_row = 0
        self.setGeometry(300, 300, 650, 300)
        self.setWindowTitle('PWKeeper')
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))

    def initToolBar(self):
        newAction = QtGui.QAction(QtGui.QIcon('images/new.png'), 'new', self)
        editAction = QtGui.QAction(QtGui.QIcon('images/edit.png'), 'edit', self)
        delAction = QtGui.QAction(QtGui.QIcon('images/del.png'), 'del', self)

        newAction.setShortcut('Ctrl+N')
        editAction.setShortcut('Ctrl_E')
        delAction.setShortcut('Delete')

        # 事件绑定
        newAction.triggered.connect(self.newAction_def)
        editAction.triggered.connect(self.delAction_def)
        delAction.triggered.connect(self.delAction_def)

        self.tb_new = self.addToolBar('New')
        self.tb_edit = self.addToolBar('Edit')
        self.tb_del = self.addToolBar('Del')

        self.tb_new.addAction(newAction)
        self.tb_edit.addAction(editAction)
        self.tb_del.addAction(delAction)

    def initDB(self):
        pass

    def initGrid(self):
        self.grid = QtGui.QTableWidget()
        self.setCentralWidget(self.grid)
        # set cols=4, row=0
        self.grid.setColumnCount(4)
        self.grid.setRowCount(0)
        column_width = [75, 150, 270, 150]
        for colunm in range(4):
            self.grid.setColumnWidth(colunm, column_width[colunm])
        headerlabels = ['WebSite', 'Username', 'Password', 'Url']
        self.grid.setHorizontalHeaderLabels(headerlabels)
        self.grid.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.grid.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.show()

    def newAction_def(self):
        pass

    def editAction_def(self):
        pass

    def delAction_def(self):
        pass
