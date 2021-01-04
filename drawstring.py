import data_saver


class drawstring:
    def __init__(self):
        self.data = data_saver.data_saver("'name','x','y'", "data", "data")
        pass

    def start(self):
        pass

    def drawing_data_for_top_entrys(self, data_for_drawing,pdf,font_number=9):
        """

        :type pdf: object
        """
        a = 0
        self.collating_data()
        for two_d_array in self.location_points_list:
            pdf.setFontSize(font_number)
            print(two_d_array,len(data_for_drawing),len(self.location_points_list))
            pdf.drawString(int(two_d_array[-2]), int(two_d_array[-1]), data_for_drawing[a])
            a += 1
        pass

    def collating_data(self):
        self.location_points_list = self.data.show()
