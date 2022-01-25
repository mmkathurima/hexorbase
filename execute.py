import os
import sys

from gui import *
from core import *

from PyQt5 import QtCore, QtGui, QtWidgets

def initialize():
    'Set Working directory'
    if 'core' not in os.listdir(os.getcwd()):
        variable = sys.argv[0]
        direc = variable.replace('execute.py',"")
        os.chdir(direc)


if __name__ == '__main__':
    initialize()
    application = QtWidgets.QApplication(sys.argv)
    run = database_core.main_window()
    run.show()
    application.exec_()
