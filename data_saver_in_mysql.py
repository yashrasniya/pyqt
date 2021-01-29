import mysql.connector

import sqlite3


class data_saver:
    def __init__(self, entry_data, tabel_name, file_name):
        """

        :param entry_data: it must have data like this "'name of collum','name of collum','name of collum'"
        :param tabel_name: it must be a string
        :param file_name: and this also be string
        """
        self.entry_data = entry_data
        self.table_name = tabel_name
        self.file_name = file_name
        # self.oid = input("enter a oid num: ")
        self.mangement()

    def mangement(self):
        self.start()
        self.creattabel()
        self.close()

    def start(self):  # this fachtion for start sqlite databass
        try:
            self.mysql = mysql.connector.connect(host="localhost",
                                                 user="root",
                                                 password="yash2017",
                                                 database=f"{self.file_name}"
                                                 )
            self.cursor=self.mysql.cursor()
        except:
            import sys
            print(sys.exc_info())
            self.mysql = mysql.connector.connect(host="localhost",
                                                 user="root",
                                                 password="yash2017"
                                                 )

            self.cursor = self.mysql.cursor()
            self.cursor = self.cursor.execute(f"CREATE DATABASE {self.file_name}").cursor()





    def close(self):  # this fachtion for ending sqlite databass
        self.mysql.commit()
        self.mysql.close()

    def delete_by_id(self, id):
        self.start()
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id={id}")
        self.close()

    def show(self):
        self.start()
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        value = self.cursor.fetchall()

        self.close()
        return value

    def creattabel(self):

        # self.cursor.execute(f"CREATE TABLE {self.tabel_name}(ID INT PRIMARY KEY,{self.entry_data})")

        try:
            print(f"CREATE TABLE {self.table_name}(ID INT PRIMARY KEY,{self.entry_data})")
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name}(id INT AUTO_INCREMENT PRIMARY KEY,{self.entry_data})")

        except mysql.connector.errors.ProgrammingError:
            print("tabel allrady exiest")



    def update(self, row_name=None, data_for_changing=None, oid_number=None):

        self.start()
        # self.cursor.execute(f"UPDATE {self.tabel_name} set {row_name}={data_for_changing} where ID = {oid_number}")
        # print(f"UPDATE {self.table_name} set {row_name}={data_for_changing} where ID = {oid_number}")
        try:
            print(f"UPDATE {self.table_name} set {row_name}={data_for_changing} where ID = {oid_number}")
            self.cursor.execute(f"UPDATE {self.table_name} set {row_name}={data_for_changing} where ID = {oid_number}")
            self.mysql.commit()

        except:
            import sys
            print(sys.exc_info())
            print(f"UPDATE {self.table_name} set {data_for_changing} where ID = {oid_number}")
            self.cursor.execute(f"UPDATE {self.table_name} set {data_for_changing} where ID = {oid_number}")
            self.mysql.commit()

        self.close()

    def insert(self, data_for_adding):
        self.start()
        print(f"INSERT INTO {self.table_name}  VALUES({data_for_adding})")
        self.cursor.execute(f"INSERT INTO {self.table_name}  VALUES({data_for_adding})")
        self.close()


# jj = data_saver("name VARCHAR(255),x INTEGER,y INTEGER", "sdaf", "aysh")
# jj.insert("'yash',5,5")
# jj.update("name", "'jkgg'", "7")
# print(jj.show())
# print("ok")
# data_saverm = data_saver("'name','x','y'", "data", "data")
# haha=data_saverm.show()
# print(haha)
