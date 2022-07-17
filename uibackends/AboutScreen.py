# gui imports
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog



# style sheet import
from ui_stylesheets import  Styles

class AboutScreen(QDialog):

    def __init__(self, pagetoshow):
        super(AboutScreen, self).__init__()
        uic.loadUi('ui/About.ui', self)
        self.closebutton.clicked.connect(self.backfunction)
        self.pagetoshow = pagetoshow

        # set style sheets for window
        self.setStyleSheet(Styles.windowbackground(self))
        self.closebutton.setStyleSheet(Styles.cancelbutton(self))



    def backfunction(self):
        self.pagetoshow.show()
        self.destroy()

    def closeEvent(self, event):
        self.pagetoshow.show()
        self.destroy()