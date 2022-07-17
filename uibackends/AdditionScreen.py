# gui imports
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

# style sheet import
from ui_stylesheets import Styles


# function imports
from database.db_connections import db_conn_def


#TODO: need to add error checking for duplicate category and if it fails so that it dosen't just close

class AdditionWindow(QDialog):

    def __init__(self, pagetoshow, additiontype):
        super(AdditionWindow, self).__init__()
        uic.loadUi('ui/AdditionWindow.ui', self)
        self.cancelbutton.clicked.connect(self.goBackPage)
        self.addbutton.clicked.connect(self.addRecord)

    # make variables local------------------------------------------------------------------
        self.pagetoshow = pagetoshow
        self.additiontype = additiontype

    # set of the new label names-----------------------------------------------------------
        if self.additiontype == 'client':
            self.windowlabel.setText('Input the name of the new client:')
            self.checklabel.setText('')

        if self.additiontype == 'category':
            self.windowlabel.setText('Input the name of the new category:')
            self.checklabel.setText('')



    # set the styles ----------------------------------------------------------------------
        self.setStyleSheet(Styles.windowbackground(self))
        self.windowlabel.setStyleSheet(Styles.bodytext(self))
        self.checklabel.setStyleSheet(Styles.bodytext(self))
        self.addbutton.setStyleSheet(Styles.actionbutton(self))
        self.cancelbutton.setStyleSheet(Styles.cancelbutton(self))



    # functions below ---------------------------------------------------------------------

    def addRecord(self):
        if self.additiontype == 'client':
            client_name = self.inputtextbox.text()
            sql = 'INSERT INTO clients (client) VALUES ("{b1}")'.format(b1 = client_name)
            print(sql)
            confirm_sql  = db_conn_def('insert', sql=sql, table_name='client')
            print(confirm_sql)
            self.inputtextbox.setText('')
            self.checklabel.setText('{b1} has been added'.format(b1=client_name))

        if self.additiontype == 'category':
            category_name = self.inputtextbox.text()
            sql = 'INSERT INTO categories (category) VALUES ("{b1}")'.format(b1=category_name)
            print(sql)
            confirm_sql = db_conn_def('insert',sql=sql, table_name='categories')
            print(confirm_sql)
            self.inputtextbox.setText('')
            self.checklabel.setText('{b1} has been added'.format(b1=category_name))


    def goBackPage(self):
        self.pagetoshow.show()
        self.destroy()

    def closeEvent(self, event):
        self.pagetoshow.show()
        self.destroy()


