# gui imports

import sys
import PyQt5
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import  QApplication, QMainWindow

# page imports
from uibackends.CreateDatabaseScreen import CreateDatabaseWindow
from uibackends.AboutScreen import AboutScreen

# functionality imports


# The below two if statements make the GUI work for high res screens, absolute life saver
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class LandingWindow(QMainWindow):

    def __init__(self):
        super(LandingWindow, self).__init__()
        self.w = None
        uic.loadUi('ui/MainWindow.ui', self)  # Load the PyQt5 UI file
        self.actionCreate.triggered.connect(self.showCreateDatabase)
        self.actionAbout.triggered.connect(self.showAbout)

    def showCreateDatabase(self):
        self.w = CreateDatabaseWindow(pagetoshow=landingwindow)
        self.w.show()
        self.hide()

    def showAbout(self):
        self.w = AboutScreen(pagetoshow=landingwindow)
        self.w.show()
        self.hide()

    def closeEvent(self, event):
        print('close event fired')
        sys.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    landingwindow = LandingWindow()
    landingwindow.show()
    sys.exit(app.exec_())

