import setting
import threading
import data_saver
from PyQt5 import QtCore, QtGui, QtWidgets


class Management:
    def __init__(self):

        self.data_saver_for_setting_data_upper_entry_data = data_saver.data_saver(
            "'name' TEXT,'state' BLOB,'x_max_value1' INT,'y_max_value1' INT", "upper_entry_data", "data")
        self.data_saver_for_setting_data_lower_entry_data = data_saver.data_saver(
            "'name' TEXT,'state' BLOB,'x_max_value2' INT,'y_max_value2' INT", "lower_entry_data", "data")
        self.data_saver_for_setting_data_coordinate_of_ui = data_saver.data_saver(
            "'starting_coordinate_x' REAL,'starting_coordinate_y' REAL,'ending_coordinate_x' REAL,'ending_coordinate_y' REAL",
            "coordinate_of_ui", "data")
        # self.data_of_entry = [
        #
        #     [
        #         [
        #             ["yash", True, 999, 999], ["happy", True, 999, 999], ["3", True, 999, 999],
        #             ["4", True, 999, 999]
        #         ],
        #         [0, 0, 281, 401], [0, 0, 265, 544]
        #     ],
        #
        #     [
        #         [
        #             ["5", True, 999, 999], ["6", True, 999, 999], ["7", True, 999, 999], ["4", True, 999, 999]
        #         ],
        #         [280, 0, 271, 401], [0, -601, 255, 1000]
        #     ]
        #
        # ]
        a = [
            [
                [
                    (1, 'yash', 1, 999, 999), (2, 'happy', 1, 999, 999), (3, '3', 1, 999, 999), (4, '4', 1, 999, 999)],
                (1, 0.0, 0.0, 281.0, 401.0), (2, 0.0, 0.0, 265.0, 544.0)],
            [
                [(1, '5', 1, 999, 999), (2, '6', 1, 999, 999), (3, '7', 1, 999, 999), (4, '4', 1, 999, 999)],
                (3, 280.0, 0.0, 271.0, 401.0), (4, 0.0, -601.0, 255.0, 1000.0)]
        ]

        #     ============================================================================
        # main part=========================================================================
        self.data_saver_for_location = data_saver.data_saver("'name','x','y'", "data", "data")
        # self.setting_data_saver()
        # self.showing_data_in_word_file()
        self.data_of_entry = self.setting_data_fetchall()
        # self.showing_data_in_word_file(self.data_of_entry)
        self.start_the_ui()

    def showing_data_in_word_file(self, data=None):
        with open("data.txt", "+a") as wr:
            if data != None:
                wr.write(str(data))
            else:
                data = wr.read()
                print(data)

                return self.setting_data_saver(data)

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
        a = True
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
                except Error as e:
                    print(e)
                    if a:
                        self.updating_data("",
                                           f"'name'= {data_for_saving[0]},"
                                           f"'state' ={data_for_saving[1]},"
                                           f"'x_max_value1' ={data_for_saving[2]},"
                                           f"'y_max_value1' ={data_for_saving[3]}",
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
            self.display_data()
        except IndexError:
            pass
        app.exec_()
        self.saving_or_updating_data()

    def do_something(self):

        pass

    def display_data(self):

        data_saved = self.data_saver_for_location.show()
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
                print(self.entry_data_filled_by_user[a])
                try:
                    self.saving_data(
                        f"{a + 1},'{name_of_entry}',{self.entry_data_filled_by_user[a][0]},{self.entry_data_filled_by_user[a][1]}",
                        self.data_saver_for_location)

                except:
                    self.updating_data("name", name_of_entry, a + 1, self.data_saver_for_location)
                    self.updating_data("x", self.entry_data_filled_by_user[a][0], a + 1, self.data_saver_for_location)
                    self.updating_data("y", self.entry_data_filled_by_user[a][1], a + 1, self.data_saver_for_location)

                a += 1
        for deleteing_data in self.data_saver_for_location.show()[a:]:
            self.data_saver_for_location.delete_by_id(deleteing_data[0])
        pass  # sqlite3.IntegrityError

    def updating_data(self, row_name: str, data_for_changing, oid_number: int, call_name):

        call_name.update(f"{row_name}", f"'{data_for_changing}'", oid_number)
        pass

    def saving_data(self, string_type_data, call_name):

        call_name.insert(string_type_data)

    def looop(self):
        time = 5
        times = threading.Timer(time, self.looop)

        print("ok")

        times.start()

        print("oook")


jj = Management()
