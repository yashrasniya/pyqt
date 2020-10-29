import datetime
import sqlite3


class SaveAs:
    def __init__(self, list_top_entry, list2, name):
        self.date = str(datetime.datetime.now().strftime("%d-%m-%Y"))
        self.list = list2
        self.list_top_entry = list_top_entry
        self.name = name
        self.cerate()

    def cerate(self):
        tabel = sqlite3.connect(f"{self.name}_{self.date}.db")
        car = tabel.cursor()
        car.execute(
            "CREATE TABLE bill(nameP,gst,size,Quantity,Rate)")  # for macking a tabbel which name is bill
        tabel.commit()
        car.close()
        self.add_in_tabel()
        self.saveing_top_entrys()

    def add_in_tabel(self):
        tabel = sqlite3.connect(f"{self.name}_{self.date}.db")
        car = tabel.cursor()

        for list in self.list:
            print(type(list[0]), list[0], list[1], list[2], list[3], list[4])
            print()
            car.execute('INSERT INTO bill(nameP,gst,size,Quantity,Rate) VALUES(?,?,?,?,?)',
                        (list[0], list[1], list[2],
                         list[3], list[4],
                         ))  # inserting the product data in sqlite data bass
        print("completed")
        tabel.commit()
        car.close()

    def saveing_top_entrys(self):

        tabel = sqlite3.connect(f"{self.name}_{self.date}.db")
        car = tabel.cursor()
        car.execute(
            "CREATE TABLE top_entrys_data( \n"
            "            Invoice_number,\n"
            "            Date,\n"
            "            Name,\n"
            "            Addres, \n"
            "            Gst_in_Percentage,\n"
            "            Gst_Number,\n"
            "            State,\n"
            "            State_Code\n"
            "            )")
        car.execute('''INSERT INTO top_entrys_data(
        Invoice_number,
             Date,
            Name,
            Addres, 
            Gst_in_Percentage,
            Gst_Number,
            State,
            State_Code) VALUES(?,?,?,?,?,?,?,?)''',
                    (self.list_top_entry[0],
                     self.list_top_entry[1],
                     self.list_top_entry[2],
                     self.list_top_entry[3],
                     self.list_top_entry[4],
                     self.list_top_entry[5],
                     self.list_top_entry[6],
                     self.list_top_entry[7]
                     ))
        tabel.commit()
        car.close()


class Show:


    def show_tabel(self,file_name):
        self.file_name = file_name
        tabel = sqlite3.connect(self.file_name)
        print(self.file_name)
        car = tabel.cursor()

        carpat = car.execute("SELECT nameP,gst,size,Quantity,Rate from bill")
        # for fetchall product data
        self.product_data = car.fetchall()

        car.execute("""SELECT Invoice_number,
            Date,
            Name,
            Addres, 
            Gst_in_Percentage,
            Gst_Number,
            State,
            State_Code from top_entrys_data""")  # for fetchall customer data
        self.customer_data = car.fetchall()
        tabel.commit()
        car.close()
        return self.product_data, self.customer_data
