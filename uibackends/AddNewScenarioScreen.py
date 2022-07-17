# gui imports
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

# style sheet import
from ui_stylesheets import Styles

#page imports
from uibackends.AdditionScreen import AdditionWindow

# function imports
from database.db_connections import db_conn_def


class AddNewScenarioWindow(QDialog):

    def __init__(self, pagetoshow):
        super(AddNewScenarioWindow, self).__init__()
        uic.loadUi('ui/NewScenario.ui', self)

        # data on load --------------------------------------------------
        self.getClients()
        self.getCategories()
        self.checklabel.setText('')



        # hold the screen you will go back to if cancel or "X" is pressed
        self.pagetoshow = pagetoshow
        self.pagename = self

        # button controls -------------------------------------------------
        self.cancelbutton.clicked.connect(self.goBackPage)
        self.newclientbutton.clicked.connect(self.goToNewClient)
        self.newcategorybutton.clicked.connect(self.goToNewCategory)
        self.refreshbutton.clicked.connect(self.refresh)
        self.continuebutton.clicked.connect(self.continueprocess)

        # assert styles-------------------------------------------------
        self.setStyleSheet(Styles.windowbackground(self))
        self.continuebutton.setStyleSheet(Styles.actionbutton(self))
        self.cancelbutton.setStyleSheet(Styles.cancelbutton(self))
        self.clientgroupbox.setStyleSheet(Styles.groupbox(self))
        self.categorygroupbox.setStyleSheet(Styles.groupbox(self))
        self.scenariogroupbox.setStyleSheet(Styles.groupbox(self))
        self.newclientbutton.setStyleSheet(Styles.additionbutton(self))
        self.newcategorybutton.setStyleSheet(Styles.additionbutton(self))
        self.selectclientlabel.setStyleSheet(Styles.bodytext(self))
        self.clientcombobox.setStyleSheet(Styles.combobox(self))
        self.categorylabel.setStyleSheet(Styles.bodytext(self))
        self.categorycombobox.setStyleSheet(Styles.combobox(self))
        self.scenariolabel.setStyleSheet(Styles.bodytext(self))
        self.scenariocombobox.setStyleSheet(Styles.combobox(self))
        self.noscenariolabel.setStyleSheet(Styles.bodytext(self))
        self.refreshbutton.setStyleSheet(Styles.actionbutton(self))
        self.namelabel.setStyleSheet(Styles.headingtextbold(self))
        self.checklabel.setStyleSheet(Styles.bodytext(self))

    # functions below -------------------------------------
    def continueprocess(self):
        pass


    def refresh(self):
        self.getClients()
        self.getCategories()

    def getCategories(self):
        self.categorycombobox.clear()
        sql = 'SELECT DISTINCT(category) from categories'
        catlistitems = db_conn_def('select',sql=sql, table_name='categories')
        for category in catlistitems['payload']:
            self.categorycombobox.addItem(category[0])


    def getClients(self):
        self.clientcombobox.clear()
        sql = 'SELECT DISTINCT(client) from clients'
        ddlistitems = db_conn_def('select', sql=sql, table_name='clients')
        for client in ddlistitems['payload']:
            self.clientcombobox.addItem(client[0])

    def goToNewClient(self):
        self.w = AdditionWindow(pagetoshow=self.pagename, additiontype='client')
        self.w.show()
        self.hide()

    def goToNewCategory(self):
        self.w = AdditionWindow(pagetoshow=self.pagename, additiontype='category')
        self.w.show()
        self.hide()


    def goBackPage(self):
        self.pagetoshow.show()
        self.destroy()

    def closeEvent(self, event):
        self.pagetoshow.show()
        self.destroy()
