import sqlite3


class data_saver:
    def __init__(self, entry_data, tabel_name, file_name):
        """

        :param entry_data: it must have data like this "'name of collum','name of collum','name of collum'"
        :param tabel_name: it must be a string
        :param file_name: and this also be string
        """
        self.entry_data = entry_data
        self.tabel_name = tabel_name
        self.file_name = file_name
        # self.oid = input("enter a oid num: ")
        self.mangement()

    def mangement(self):
        self.creattabel()

    def start(self):  # this fachtion for start sqlite databass
        self.sqlite_data = sqlite3.connect(f"{self.file_name}.db")
        self.cursor = self.sqlite_data.cursor()

    def close(self):  # this fachtion for ending sqlite databass
        self.sqlite_data.commit()
        self.sqlite_data.close()
    def delete_by_id(self,id):
        self.start()
        self.cursor.execute(f"DELETE FROM {self.tabel_name} WHERE id={id}")
        self.close()
    def show(self):
        self.start()
        self.cursor.execute(f"SELECT * FROM {self.tabel_name}")
        value = self.cursor.fetchall()

        self.close()
        return value

    def creattabel(self):
        self.start()
        # self.cursor.execute(f"CREATE TABLE {self.tabel_name}(ID INT PRIMARY KEY,{self.entry_data})")

        try:

            self.cursor.execute(f"CREATE TABLE {self.tabel_name}(ID INT PRIMARY KEY,{self.entry_data})")
        except sqlite3.OperationalError:
            print("tabel allrady exiest")

        self.close()

    def update(self, row_name=None, data_for_changing=None, oid_number=None):

        self.start()
        # self.cursor.execute(f"UPDATE {self.tabel_name} set {row_name}={data_for_changing} where ID = {oid_number}")
        try:
            self.cursor.execute(f"UPDATE {self.tabel_name} set {row_name}={data_for_changing} where ID = {oid_number}")
        except:
            import sys
            print(sys.exc_info())
            print(f"UPDATE {self.tabel_name} set {data_for_changing} where ID = {oid_number}")
            self.cursor.execute(f"UPDATE {self.tabel_name} set {data_for_changing} where ID = {oid_number}")


        self.close()

    def insert(self, data_for_adding):
        self.start()
        self.cursor.execute(f"INSERT INTO {self.tabel_name}  VALUES({data_for_adding})")
        self.close()


# jj = data_saver("'name' TEXT,'x' INT,'y' INT", "jja", "aysh")
# jj.insert("6,'yash',5,5")
# jj.update("'", "'name'='yahs',x = 6", "2")
# print(jj.show())
# print("ok")
# data_saverm = data_saver("'name','x','y'", "data", "data")
# haha=data_saverm.show()
# print(haha)