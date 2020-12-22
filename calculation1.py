class calculation:
    def __int__(self, list_of_int_data):
        self.list_of_int_data = list_of_int_data

        pass

    def start(self):
        total_with_out_gst = 0
        total_with_gst = 0
        total_amount_of_a_product_with_gst_list = []
        total_amount_of_a_product_without_gst_list = []
        for singel_row_data in self.list_of_int_data:
            total_amount_of_a_product_without_gst_list.append(
                self.total_amount_of_a_product(singel_row_data[-2], singel_row_data[-1],
                                               singel_row_data[-3]))
            total_with_out_gst += total_amount_of_a_product_without_gst_list[-1]
            total_amount_of_a_product_with_gst_list.append(
                self.total_amount_of_a_product(singel_row_data[-2], singel_row_data[-1],
                                               singel_row_data[-3],
                                               singel_row_data[-4]))
            total_with_gst += total_amount_of_a_product_with_gst_list[-1]
        return [total_with_out_gst, total_with_gst], [total_amount_of_a_product_with_gst_list,
                                                      total_amount_of_a_product_without_gst_list]

    def total_amount_of_a_product(self, qty, rate, size, gst=0):
        qty, rate, size, gst = int(qty), int(rate), int(size), int(gst)
        if gst != 0:
            return (size * (qty * rate)) * (gst / 100)
        elif gst == 0:
            return size * (qty * rate)


# jj = calculation()
# jj.__int__([['sdfkl', '18', '64', '464', '64'], ['', '64', '64', '646', '4']])
# haha = jj.start()
# print(haha)
