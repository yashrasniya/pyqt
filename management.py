import setting
import threading
import data_saver
from PyQt5 import QtCore, QtGui, QtWidgets


class Management:
    def __init__(self):

        self.data_of_entry = [

            [
                [
                    ["yash", True, 999, 999, ], ["happy", True, 999, 999, ], ["3", True, 999, 999, ],
                    ["4", True, 999, 999, ]
                ],
                [0, 0, 281, 401], [0, 0, 265, 544]
            ],

            [[["5", True, 999, 999, ], ["6", True, 999, 999, ], ["7", True, 999, 999, ], ["4", True, 999, 999, ]],
             [280, 0, 271, 401], [0, -601, 255, 1000]]

        ]
        #     ============================================================================
        # main part=========================================================================
        self.data_saverm = data_saver.data_saver("'name','x','y'", "data", "data")
        self.start_the_ui()

    def start_the_ui(self):
        import sys
        self.ui_mainwindow = setting.Ui_MainWindow(self.data_of_entry)
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.entry_list_name = self.ui_mainwindow.setupUi(MainWindow)
        MainWindow.show()
        try:
            self.display_data()
        except IndexError:
            pass
        app.exec_()
        self.saving_or_updating_data()

    def do_something(self):

        pass

    def display_data(self):

        data_saved = self.data_saverm.show()
        print(data_saved)
        self.ui_mainwindow.finding_output(self.entry_list_name,
                                          do_you_want_to_set_value=True, entry_values_list=data_saved)
        pass

    def saving_or_updating_data(self):
        self.entry_data_filled_by_user = self.ui_mainwindow.finding_output(self.entry_list_name,
                                                                           do_you_want_to_set_value=False)
        a = 0
        for _data_of_entry in self.data_of_entry:

            for data_of_entry in _data_of_entry[0]:
                name_of_entry = data_of_entry[0]
                x_y_data = self.entry_data_filled_by_user[a][0]
               
                try:
                    self.saving_data(
                        f"{a + 1},'{name_of_entry}',{self.entry_data_filled_by_user[a][0]},{self.entry_data_filled_by_user[a][1]}")

                except :
                    self.updating_data("name", name_of_entry, a + 1)
                    self.updating_data("x", self.entry_data_filled_by_user[a][1], a + 1)
                    self.updating_data("y", self.entry_data_filled_by_user[a][0], a + 1)
                    
                    
                a += 1
        for deleteing_data in self.data_saverm.show()[a:]:
            self.data_saverm.delete_by_id(deleteing_data[0])
        pass  # sqlite3.IntegrityError

    def updating_data(self, row_name, data_for_changering, oid_number):
        
        self.data_saverm.update(f"{row_name}", f"'{data_for_changering}'", oid_number)
        pass

    def saving_data(self, string_type_data):

        self.data_saverm.insert(string_type_data)

    def looop(self):
        time = 5
        times = threading.Timer(time, self.looop)

        print("ok")

        times.start()

        print("oook")


jj = Management()
