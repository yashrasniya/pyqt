import data_saver

data_saver_for_setting_data_upper_entry_data = data_saver.data_saver(
    "'name' TEXT,'state' BLOB,'x_max_value1' INT,'y_max_value1' INT", "upper_entry_data", "data")
data_saver_for_setting_data_lower_entry_data = data_saver.data_saver(
    "'name' TEXT,'state' BLOB,'x_max_value2' INT,'y_max_value2' INT", "lower_entry_data", "data")
data_saver_for_setting_data_coordinate_of_ui = data_saver.data_saver(
    "'starting_coordinate_x' REAL,'starting_coordinate_y' REAL,'ending_coordinate_x' REAL,'ending_coordinate_y' REAL",
    "coordinate_of_ui", "data")
a=[
            [
                data_saver_for_setting_data_upper_entry_data.show(),
                data_saver_for_setting_data_coordinate_of_ui.show()[0],
                data_saver_for_setting_data_coordinate_of_ui.show()[1]
            ],
            [
                data_saver_for_setting_data_lower_entry_data.show(),
                data_saver_for_setting_data_coordinate_of_ui.show()[2],
                data_saver_for_setting_data_coordinate_of_ui.show()[3]
            ]
        ]
print(a)