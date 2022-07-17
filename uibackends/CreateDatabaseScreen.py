# gui imports
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

# function imports
from database.db_table_creation import create_all_tables

# style sheet imports
from ui_stylesheets import Styles


class CreateDatabaseWindow(QDialog):

    def __init__(self, pagetoshow):
        super(CreateDatabaseWindow, self).__init__()
        self.pagetoshow = pagetoshow
        uic.loadUi('ui/DatabaseCreation.ui', self)
        self.cancelbutton.clicked.connect(self.goBackPage)  # button to go back to landing and cancel
        self.createbutton.clicked.connect(self.createdatabase)  # button to start database function

        # apply the stylesheet references here, means that I can create one document that will impact all UIs screens
        self.createbutton.setStyleSheet(Styles.actionbutton(self))
        self.cancelbutton.setStyleSheet(Styles.cancelbutton(self))
        self.processList.setStyleSheet(Styles.listview(self))
        self.setStyleSheet(Styles.windowbackground(self))

    # the cancel function that will back a page
    def goBackPage(self):
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
        self.cancelbutton.setText('Proceed')
        self.createbutton.setEnabled(False)
        self.createbutton.setStyleSheet(
            '''
            color:rgb(86,85,85);                                        
            background-color:gray;
            border-width: 2px;
            border-radius: 10px;
            border-color: beige;
            font: bold 14px;
            min-width: 5em;
            padding: 6px;
            ''')
