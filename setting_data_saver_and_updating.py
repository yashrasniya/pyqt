


import data_saver_in_mysql as data_saver



class gogo:
    def __init__(self, text):
        self.data_saver_for_setting_data_upper_entry_data = data_saver.data_saver(
            "name TEXT,state BLOB,x_max_value INT,y_max_value INT", "upper_entry_data", "data1")
        self.data_saver_for_setting_data_lower_entry_data = data_saver.data_saver(
                "name TEXT,state BLOB,x_max_value INT,y_max_value INT", "lower_entry_data", "data1")
        self.data_saver_for_setting_data_coordinate_of_ui = data_saver.data_saver(
            "starting_coordinate_x REAL,starting_coordinate_y REAL,ending_coordinate_x REAL,"
            "ending_coordinate_y REAL",
            "coordinate_of_ui", "data1")

        self.text = text
        self.data_in_array_form = self.text.split("%")
        self.print_()


    def print_(self):

        full_array=self.arry_creater_for_setting()

        self.setting_data_saver(full_array)
    def arry_creater_for_setting(self):

        """
                a = [
            [
                [
                    (1, 'yash', 1, 999, 999), (2, 'happy', 1, 999, 999), (3, '3', 1, 999, 999), (4, '4', 1, 999, 999)],
                (1, 0.0, 0.0, 281.0, 401.0), (2, 0.0, 0.0, 265.0, 544.0)],
            [
                [(1, '5', 1, 999, 999), (2, '6', 1, 999, 999), (3, '7', 1, 999, 999), (4, '4', 1, 999, 999)],
                (3, 280.0, 0.0, 271.0, 401.0), (4, 0.0, -601.0, 255.0, 1000.0)]
        ]
        :return:[[1, '', True, 999, 999], [2, 'happy', True, 999, 999], [3, 'gogog', True, 999, 999], [4, 'sdkfj', True, 999, 999],
         [5, 'ksafj', True, 999, 999], [6, 'sdkfj', True, 999, 999], [7, 'ksdjfa', True, 999, 999], [8, 'sdfa', True, 999, 999]]
        """
        array_of_data = []

        for name in self.data_in_array_form:
            array_of_data.append([name, True, 999, 999])

        print(array_of_data)
        return [[array_of_data, [0, 0, 281, 401], [0, 0, 265, 544]],
                                   [[["1", True, 999, 999], ["6", True, 999, 999], ["7", True, 999, 999],
                                     ["4", True, 999, 999]],
                                    [280, 0, 271, 401], [0, -601, 255, 1000]

                                    ]]
        pass
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
                    # print(data_saver.data_saver(
                    #     "'name' TEXT,'state' BLOB,'x_max_value1' INT,'y_max_value1' INT", "upper_entry_data",
                    #     "data").show())
                    if a:
                        # self.updating_data(None,
                        #                    f"name = '{data_for_saving[0]}',"
                        #                    f"state = {data_for_saving[1]},"
                        #                    f"x_max_value = {data_for_saving[2]},"
                        #                    f"y_max_value = {data_for_saving[3]}",
                        #                    c, self.data_saver_for_setting_data_upper_entry_data)
                        self.updating_data("name", f'{data_for_saving[0]}', c, self.data_saver_for_setting_data_upper_entry_data)
                        self.updating_data("state", f'{data_for_saving[1]}', c, self.data_saver_for_setting_data_upper_entry_data)
                        self.updating_data("x_max_value", f'{data_for_saving[2]}', c, self.data_saver_for_setting_data_upper_entry_data)
                        self.updating_data("y_max_value", f'{data_for_saving[3]}', c, self.data_saver_for_setting_data_upper_entry_data)

                        c += 1
                    elif not a:
                        # self.updating_data(None,
                        #                    f"name= '{data_for_saving[0]}',"
                        #                    f"state ={data_for_saving[1]},"
                        #                    f"x_max_value ={data_for_saving[2]},"
                        #                    f"y_max_value ={data_for_saving[3]}",
                        #                    d, self.data_saver_for_setting_data_lower_entry_data)
                        self.updating_data("name", f"{data_for_saving[0]}", d,
                                           self.data_saver_for_setting_data_upper_entry_data)
                        self.updating_data("state", f"{data_for_saving[1]}", d,
                                           self.data_saver_for_setting_data_upper_entry_data)
                        self.updating_data("x_max_value", f"{data_for_saving[2]}", d,
                                           self.data_saver_for_setting_data_upper_entry_data)
                        self.updating_data("y_max_value", f'{data_for_saving[3]}', d,
                                           self.data_saver_for_setting_data_upper_entry_data)
                        d += 1
            a=True

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
                    import sys
                    print(sys.exc_info())
                    self.updating_data(None, f"starting_coordinate_x = {data_for_saving[0]},"
                                           f"starting_coordinate_y = {data_for_saving[1]},"
                                           f"ending_coordinate_x = {data_for_saving[2]},"
                                           f"ending_coordinate_y = {data_for_saving[3]}",
                                       e, self.data_saver_for_setting_data_coordinate_of_ui)
                e += 1
            b += 1

        pass

    def saving_data(self, string_type_data, call_name):

        call_name.insert(string_type_data)
    def updating_data(self, row_name: str, data_for_changing, oid_number: int, call_name):
        if row_name==None:


            call_name.update(f"", f"{data_for_changing}", oid_number)
        else:
            call_name.update(f"{row_name}", f"'{data_for_changing}'", oid_number)