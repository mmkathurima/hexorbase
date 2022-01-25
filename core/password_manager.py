from . import variables
from gui.password_manager import *

from PyQt5 import QtCore, QtGui, QtWidgets

class password_manager(QtWidgets.QDialog,Ui_password_manager):
    ''' Class definition contains functions and Signals
        for management of passwords to be used for
        database login
    '''
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)

        self.inser_credential.clicked.connect(self.insert_credential)
        self.delete_credential.clicked.connect(self.delete_credential_row)
        self.password_save_changes.clicked.connect(self.save_changes)
        self.use_credential.clicked.connect(self.use_credential_default)

        import sqlite3

        database_read = sqlite3.connect(os.getcwd() + os.sep + 'hexorbase_database.db')
        database_query_read = database_read.cursor()
        import time
        try:
            database_query_read.execute('select * from credentials')
            credential_entries = database_query_read.fetchall()

            for iterate in range(0,str(credential_entries).count('(')):
                credential = credential_entries[iterate]

                self.password_manager_table.insertRow(iterate)

                username_section = QtWidgets.QTableWidgetItem()
                password_section = QtWidgets.QTableWidgetItem()

                username_section.setText(credential[0])
                password_section.setText(credential[1])

                self.password_manager_table.setItem(iterate,0,username_section)
                self.password_manager_table.setItem(iterate,1,password_section)

        except(sqlite3.OperationalError,IndexError):
            pass
        database_read.close()




    def insert_credential(self):
        ''' insert a new row to add login details'''
        self.password_manager_table.insertRow(0)



    def delete_credential_row(self):
        ''' remove currently selected row'''
        current_row_number = int(self.password_manager_table.currentRow())
        self.password_manager_table.removeRow(current_row_number)



    def save_changes(self):
        ''' commit changes or additions to
            database
        '''
        import sqlite3

        if 'hexorbase_database.db' in os.listdir(os.getcwd()):
            os.remove(os.getcwd() + os.sep + 'hexorbase_database.db')

        row_numbers = int(self.password_manager_table.rowCount())

        database_file = sqlite3.connect(os.getcwd() + os.sep + 'hexorbase_database.db')      # Creates database for passwords in local working directory
        database_query = database_file.cursor()
        database_query.execute('''create table if not exists 'credentials' (username text, password text)''')

        for iterate in range(row_numbers):
            usernames = QtWidgets.QTableWidgetItem(self.password_manager_table.item(iterate,0))
            passwords = QtWidgets.QTableWidgetItem(self.password_manager_table.item(iterate,1))

            database_query.execute("insert into credentials values ('%s','%s')"%(usernames.text(),passwords.text()))

        database_file.commit()
        database_file.close()



    def use_credential_default(self):
        ''' set text to login area'''
        try:
            current_row = int(self.password_manager_table.currentRow())

            usernames = QtWidgets.QTableWidgetItem(self.password_manager_table.item(current_row,0))
            passwords = QtWidgets.QTableWidgetItem(self.password_manager_table.item(current_row,1))

            variables.username_linedit.setText(usernames.text())
            variables.password_linedit.setText(passwords.text())

            self.close()
        except(Exception):
            QtWidgets.QMessageBox.warning(self,"Null Field","Please insert login details")
