# gui imports
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog



class AboutScreen(QDialog):

    def __init__(self, pagetoshow):
        super(AboutScreen, self).__init__()
        uic.loadUi('ui/About.ui', self)
        self.closebutton.clicked.connect(self.backfunction)
        self.pagetoshow = pagetoshow

    def backfunction(self):
        self.pagetoshow.show()
        self.destroy()

    def closeEvent(self, event):
        self.pagetoshow.show()
        self.destroy()