# gui imports
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

# function imports
from database.db_table_creation import create_all_tables


class CreateDatabaseWindow(QDialog):

    def __init__(self, pagetoshow):
        super(CreateDatabaseWindow, self).__init__()
        self.pagetoshow = pagetoshow
        uic.loadUi('ui/DatabaseCreation.ui', self)
        self.cancelbutton.clicked.connect(self.showlanding)  # button to go back to landing and cancel
        self.createbutton.clicked.connect(self.createdatabase)  # button to start database function

    # the cancel function that will back a page
    def showlanding(self):
        self.pagetoshow.show()
        self.destroy()

    def closeEvent(self, event):
        self.pagetoshow.show()
        self.destroy()


    # The function to create the database
    def createdatabase(self):
        db_status = create_all_tables()
        lst_index = 0
        for d in db_status:
            for i in d.items():
                self.processList.addItem(i[1])

            lst_index += 1
