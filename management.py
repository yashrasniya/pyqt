import threading
import data_saver_in_mysql
import data_saver
import setting
from PyQt5 import QtWidgets
import setting_data_display
import sys


class Management:
    def __init__(self):

        self.data_saver_for_setting_data_upper_entry_data = data_saver_in_mysql.data_saver(
            "'name' TEXT,'state' BLOB,'x_max_value1' INT,'y_max_value1' INT", "upper_entry_data", "data1")
        self.data_saver_for_setting_data_lower_entry_data = data_saver_in_mysql.data_saver(
            "'name' TEXT,'state' BLOB,'x_max_value2' INT,'y_max_value2' INT", "lower_entry_data", "data1")
        self.data_saver_for_setting_data_coordinate_of_ui = data_saver_in_mysql.data_saver(
            "'starting_coordinate_x' REAL,'starting_coordinate_y' REAL,'ending_coordinate_x' REAL,"
            "'ending_coordinate_y' REAL",
            "coordinate_of_ui", "data1")

        #     ============================================================================
        # main part=========================================================================
        self.data_saver_for_location = data_saver.data_saver("'name','x','y'", "data", "data")
        # self.setting_data_saver()
        # self.showing_data_in_word_file()
        self.data_of_entry = self.setting_data_fetchall()
        # self.setting_data_displaying()
        # self.showing_data_in_word_file(self.data_of_entry)
        # self.start_the_ui()

    def showing_data_in_word_file(self, data=None):
        with open("data.txt", "+a") as wr:
            if data is not None:
                wr.write(str(data))
            else:
                data = wr.read()
                print(data)

                return self.setting_data_saver(data)

    def setting_data_displaying(self):

        app = QtWidgets.QApplication(sys.argv)
        ex = setting_data_display.App()
        print(ex.initUI())
        sys.exit(app.exec_())

    def setting_data_fetchall(self):
        return [
            [
                self.data_saver_for_setting_data_upper_entry_data.show(),
                self.data_saver_for_setting_data_coordinate_of_ui.show()[0],
                self.data_saver_for_setting_data_coordinate_of_ui.show()[1]
            ],
            [
                self.data_saver_for_setting_data_lower_entry_data.show(),
                self.data_saver_for_setting_data_coordinate_of_ui.show()[2],
                self.data_saver_for_setting_data_coordinate_of_ui.show()[3]
            ]
        ]

    def setting_data_saver(self, data_of_entry):
        a = False
        c, d = 1, 1
        for small_list in data_of_entry:

            for data_for_saving in small_list[0]:
                try:
                    if a:
                        self.saving_data(
                            f"{c},'{data_for_saving[0]}',{data_for_saving[1]},{data_for_saving[2]},{data_for_saving[3]}",
                            self.data_saver_for_setting_data_upper_entry_data)
                        c += 1


                    elif not a:
                        self.saving_data(
                            f"{d},'{data_for_saving[0]}',{data_for_saving[1]},{data_for_saving[2]},{data_for_saving[3]}",
                            self.data_saver_for_setting_data_lower_entry_data)
                        d += 1
                except:
                    import sys
                    print(sys.exc_info())
                    if a:
                        self.updating_data("",
                                           f"'name' = {data_for_saving[0]},"
                                           f"'state' = {data_for_saving[1]},"
                                           f"'x_max_value1' = {data_for_saving[2]},"
                                           f"'y_max_value1' = {data_for_saving[3]}",
                                           c, self.data_saver_for_setting_data_upper_entry_data)
                    elif not a:
                        self.updating_data("",
                                           f"'name'= {data_for_saving[0]},"
                                           f"'state' ={data_for_saving[1]},"
                                           f"'x_max_value2' ={data_for_saving[2]},"
                                           f"'y_max_value2' ={data_for_saving[3]}",
                                           d, self.data_saver_for_setting_data_lower_entry_data)

            a = False
        b = 1
        e = 1
        for small_list in data_of_entry:

            for data_for_saving in small_list[1:]:
                print(data_for_saving)
                try:
                    self.saving_data(
                        f"{e},{data_for_saving[0]},{data_for_saving[1]},{data_for_saving[2]},{data_for_saving[3]}",
                        self.data_saver_for_setting_data_coordinate_of_ui)
                except:
                    self.updating_data("", f"'starting_coordinate_x' = {data_for_saving[0]},"
                                           f"'starting_coordinate_y' = {data_for_saving[1]},"
                                           f"'ending_coordinate_x' = {data_for_saving[2]},"
                                           f"'ending_coordinate_y' = {data_for_saving[3]}",
                                       e, self.data_saver_for_setting_data_coordinate_of_ui)
                e += 1
            b += 1

        pass

    def start_the_ui(self):
        import sys
        self.ui_mainwindow = setting.Ui_MainWindow(self.data_of_entry)
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.entry_list_name = self.ui_mainwindow.setupUi(MainWindow)
        MainWindow.show()
        try:
            self.display_data(self.ui_mainwindow, self.entry_list_name)
        except IndexError:
            pass
        app.exec_()
        self.saving_or_updating_data(self.ui_mainwindow, self.entry_list_name, self.data_of_entry)

    def do_something(self):

        pass

    def display_data(self, ui_mainwindow, entry_list_name):

        data_saved = self.data_saver_for_location.show()
        print(data_saved)
        ui_mainwindow.finding_output(entry_list_name,
                                     do_you_want_to_set_value=True, entry_values_list=data_saved)
        pass

    def saving_or_updating_data(self, ui_mainwindow, entry_list_name, data_of_entry):
        self.entry_data_filled_by_user = ui_mainwindow.finding_output(entry_list_name,
                                                                      do_you_want_to_set_value=False)

        a = 0
        for _data_of_entry in data_of_entry:

            for data_of_entry in _data_of_entry[0]:
                name_of_entry = data_of_entry[0]
                x_y_data = self.entry_data_filled_by_user[a][0]
                print(self.entry_data_filled_by_user[a])
                try:
                    self.saving_data(
                        f"{a + 1},'{name_of_entry}',{self.entry_data_filled_by_user[a][0]},{self.entry_data_filled_by_user[a][1]}",
                        self.data_saver_for_location)

                except:
                    import sys
                    print(sys.exc_info())
                    self.updating_data("name", name_of_entry, a + 1, self.data_saver_for_location)
                    self.updating_data("x", self.entry_data_filled_by_user[a][0], a + 1, self.data_saver_for_location)
                    self.updating_data("y", self.entry_data_filled_by_user[a][1], a + 1, self.data_saver_for_location)

                a += 1
        for deleting_data in self.data_saver_for_location.show()[a:]:
            self.data_saver_for_location.delete_by_id(deleting_data[0])
        pass  # sqlite3.IntegrityError

    def updating_data(self, row_name: str, data_for_changing, oid_number: int, call_name):

        call_name.update(f"{row_name}", f"{data_for_changing}", oid_number)
        pass

    def saving_data(self, string_type_data, call_name):

        call_name.insert(string_type_data)

    def looop(self):
        time = 5
        times = threading.Timer(time, self.looop)

        print("ok")

        times.start()

        print("oook")



