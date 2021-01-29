import sys
import threading
from tkinter import *
import setting
import pdfmacker
import save
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication, QAction, QFileDialog
from PyQt5.QtGui import QFont
import management
import xyz
import data_saver_in_mysql as data_saver


class my_cal(QMainWindow):
    def __init__(self):
        super(my_cal, self).__init__()
        self.setGeometry(200, 200, 1000, 1000)
        self.setWindowTitle("Bill")
        self.start()

    def start(self):
        self.all_entry_list, self.but, self.y, self.totle_list_label = [], [], [], []  # f=list of entry,i =list of button and entry

        self.y.append(100)
        self.entry()  # start
        self.start = True
        # self.all_entry_list[-1][-1].returnPressed.connect(self.entry)  # when press enter it create a row
        self.loop()
        self.menu()
        self.top_entrys()
        self.Qlabel = QtWidgets.QLabel(self)
        self.Qlabel.setGeometry(500, 500, 200, 50)
        # b1=QtWidgets.QPushButton(self)
        # b1.clicked.connect(self.creating_pdf)

    def donothing(self):
        pass

    def save_as(self):
        self.geting_all_values()
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)")  # creating a dialogebox for name

        save.SaveAs(self.geting_values_of_top_list,
                    self.data_all_entry_list, fileName)

    def open(self):

        open_file = str(QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                    "All Files (*);;Python Files (*.py)")
                        ).split("'")  # creating a dialogebox for file path
        for entrys_for_del in self.all_entry_list:
            for entrys_for_del in entrys_for_del:
                entrys_for_del.deleteLater()
        for label in self.totle_list_label:
            label.deleteLater()
        self.totle_list_label.clear()
        self.nos = 0
        self.all_entry_list.clear()  # delete all data of list
        self.i.clear()  # delete all data of list
        self.i.append(1)  # add 1 for loop funtion
        self.y.clear()
        self.y.append(100)

        print(open_file[1], open_file)
        data = save.Show()
        product_data, customer_data = data.show_tabel(open_file[1])
        num = 0

        print(product_data, customer_data)
        num = 0
        for entry in self.top_entry:
            entry.clear()
            entry.setText(customer_data[0][num])  # display customer data in entry
            num += 1
        num = 0
        for v in product_data:
            self.entry()
            l = 0
            for j in v:
                self.all_entry_list[num][l].setText(j)  # display all data in entry
                self.all_entry_list[num][l].show()
                l += 1
            num += 1

    def menu(self):
        menubar = self.menuBar()
        newAct = QAction('New', self)
        self.actionCopy = QtWidgets.QAction(self)
        # =====================================================
        fileMenu = menubar.addMenu('File')
        save_menu = QAction('save', self)
        open_menu = QAction('open', self)
        save_as_pdf = QAction('Make pdf', self)

        save_menu.triggered.connect(lambda: self.save_as())
        open_menu.triggered.connect(lambda: self.open())
        save_as_pdf.triggered.connect(lambda: self.creating_pdf())

        fileMenu.addAction(newAct)
        fileMenu.addAction(save_menu)
        fileMenu.addAction(open_menu)
        fileMenu.addAction(save_as_pdf)
        # ======================================================

        # =======================================================
        editMenu = menubar.addMenu('Edit')
        copy = editMenu.addMenu("Copy")
        paste = editMenu.addMenu("Paste")
        cut = editMenu.addMenu("Cut")
        self.actionCopy.setObjectName("actionCopy")
        copy.addAction(self.actionCopy)

        _translate = QtCore.QCoreApplication.translate

        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        # =======================================================

        # =======================================================
        SettingsMenu = menubar.addMenu('Settings')

        location_menu = QAction('location', self)
        self.w = None
        location_menu.triggered.connect(self.sow_new_window)

        SettingsMenu.addAction(location_menu)
        # ========================================================

        # =======================================================
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # ========================================================
        menubar.show()  # //////////////////////////////////////////
        # =======================================================
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # ========================================================

    def sow_new_window(self):
        management_ = management.Management()

        import sys
        self.ui_mainwindow = setting.Ui_MainWindow(management_.setting_data_fetchall())
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.entry_list_name = self.ui_mainwindow.setupUi(MainWindow)
        MainWindow.show()
        try:
            management_.display_data(self.ui_mainwindow, self.entry_list_name)
        except IndexError:
            pass
        management_.saving_or_updating_data(self.ui_mainwindow, self.entry_list_name,
                                            management_.setting_data_fetchall())

    def top_entrys(self):

        # ----------------------------------------------#
        # ----------------location----------------------#

        self.x_1, self.y_1 = [], []
        self.x_1.append(0)
        self.y_1.append(50)

        # -------------------------------------------label------------------------------------------------------------------
        label_values = [" Invoice number", "Date", "Name", "Addres", "Gst in Percentage", "Gst Number", "State",
                        "State Code"]
        label_values = data_saver.data_saver(
            "'name' TEXT,'state' BLOB,'x_max_value1' INT,'y_max_value1' INT", "upper_entry_data", "data1").show()
        print(label_values)
        self.label = []
        for name in label_values:
            name = name[-4]
            self.label.append(QtWidgets.QLabel(self))
            self.label[-1].setText(f"{name}")
            self.label[-1].setGeometry(self.x_1[-1], 20, 100, 30)
            self.label[-1].setStyleSheet("color: #433f5b;"
                                         "text-shadow: 2px 2px 4px #000000;"
                                         "font-family: Cursive;"
                                         "font-size: 300%;")
            self.x_1.append(self.x_1[-1] + 100)
            self.label[-1].show()
        self.x_1.clear()
        self.x_1.append(0)
        # -------------------------------entry box---------------------------------------------------

        self.top_entry = []

        for valu in label_values:
            self.top_entry.append(QLineEdit(self))
            self.top_entry[-1].setGeometry(self.x_1[-1], self.y_1[-1], 100, 30)
            self.x_1.append(self.x_1[-1] + 100)
            print(self.top_entry[-1])
            self.top_entry[-1].show()
        self.list_for_product = ['Name',
                                 'Gst',
                                 'Size',
                                 'Quantity',
                                 'Rate'
                                 ]
        self.list_of_product_pyqt = []
        self.x_1.clear()
        self.x_1.append(0)
        for value in self.list_for_product:
            self.list_of_product_pyqt.append(QtWidgets.QLabel(self))
            self.list_of_product_pyqt[-1].setText(f"{value}")
            self.list_of_product_pyqt[-1].setGeometry(self.x_1[-1] + 5, self.y_1[-1] + 30, 100, 30)
            self.x_1.append(self.x_1[-1] + 100)

            self.list_of_product_pyqt[-1].show()
        print('-------------------2---')

    def entry(self):  # for creating a new row of entry

        try:
            self.all_entry_list[-1][-1].returnPressed.disconnect(self.entry)  # unbind the last entry
            pass

        except:
            pass

        en = []
        self.i = []
        self.i.append(0)

        for ii in range(0, 5):  # for 5 entry

            # text  boxs
            x = self.i[-1]
            en.append(QLineEdit(self))
            # en.append(QtWidgets.QSpinBox(self))

            en[ii].setGeometry(x, self.y[-1] + 5, 100, 30)
            en[ii].setStyleSheet("color: #433f5b;"
                                 "text-shadow: 2px 2px 4px #000000;"
                                 "font-family: Cursive;"
                                 "font-size: 300%;"
                                 "background-color: #FF7F50;")
            en[ii].show()

            self.i.append(self.i[-1] + 100)

        self.totle_list_label.append(QtWidgets.QLabel(self))
        self.totle_list_label[-1].setGeometry(self.i[-1], self.y[-1] + 5, 100, 30)
        self.totle_list_label[-1].setFont(QFont('Arial', 15))
        self.y.append(self.y[-1] + 50)
        self.totle_list_label[-1].setText("0.0")
        self.totle_list_label[-1].show()
        self.all_entry_list.append(en)
        print(self.all_entry_list)
        self.all_entry_list[-1][-1].returnPressed.connect(self.entry)  # when press enter it create a row
        try:
            self.total.deleteLater()
        except AttributeError:
            print("erro")
        self.total = QtWidgets.QLabel(self)
        self.total.setFont(QFont('Arial', 15))
        self.total.setGeometry(self.i[-1], self.y[-1] + 50 + 5, 100, 30)

        self.total.setText(" Total:0.0   Total withgst:0.0")
        self.total.show()

    def loop(self):
        # ---------------- for location in side the entry-------------------------------------

        time = 1  # wait for 1 sec
        self.get_qut = []  # list of entry3
        self.get_rate = []  # list of entry4
        self.get_size = []  # list of entry2
        self.get_gst = []
        multiply = []  # list of addition of entry3 + entry4
        print("1")
        for num in range(len(self.all_entry_list)):

            try:
                if self.all_entry_list[num][-2].text() != "" and self.all_entry_list[num][-3].text() != "" and \
                        self.all_entry_list[num][-1].text() != "" and self.all_entry_list[num][-4].text() != "":
                    self.get_qut.append(float(self.all_entry_list[num][-2].text()))  # getting entry3
                    self.get_rate.append(float(self.all_entry_list[num][-1].text()))  # geting entry4
                    self.get_size.append(float(self.all_entry_list[num][-3].text()))
                    self.get_gst.append(float(self.all_entry_list[num][-4].text()))  # getting entry2
                elif self.all_entry_list[num][-2].text() == "" or self.all_entry_list[num][-3].text() == "" or \
                        self.all_entry_list[num][-1].text() == "" or self.all_entry_list[num][-4].text() == "":
                    list_2_value, list_3_value, list_1_value, list_4_value = self.all_entry_list[num][-2].text(), \
                                                                             self.all_entry_list[num][-3].text(), \
                                                                             self.all_entry_list[num][-1].text(), \
                                                                             self.all_entry_list[num][-4].text()
                    print("12\n454\n646\n16")

                    if self.all_entry_list[num][-2].text() == "":
                        list_2_value = 1.0

                    if self.all_entry_list[num][-3].text() == "":
                        list_3_value = 1.0

                    if self.all_entry_list[num][-1].text() == "":
                        list_1_value = 1.0

                    if self.all_entry_list[num][-4].text() == "":
                        list_4_value = 1.0

                    self.get_qut.append(float(list_2_value))  # getting entry3
                    self.get_rate.append(float(list_3_value))  # geting entry4
                    self.get_size.append(float(list_1_value))
                    self.get_gst.append(float(list_4_value))
                else:
                    self.get_qut.append(1)  # getting entry3
                    self.get_rate.append(1)  # geting entry4
                    self.get_size.append(1)
                    self.get_gst.append(1)

            except:

                self.get_qut.append(float(1))  # getting entry3
                self.get_rate.append(float(1))  # geting entry4
                self.get_size.append(float(1))
                self.get_gst.append(float(1))
                self.total.setText("enter the int value")



        try:
            for a in range(0, len(self.get_qut)):
                print(a, "get")
                print(self.get_qut, self.get_rate)

                t = self.get_qut[a] * self.get_rate[a] * self.get_size[a]  # multiply qui and rate

                multiply.append((t, self.get_gst[a]))
            self.nos = 0
            ks = 0
            with_gst_total = 0
            for nass, gst in multiply:
                pre = nass + ks
                with_gst_total = nass + ((nass * gst) / 100) + with_gst_total

                self.totle_list_label[self.nos].setText(
                    f"without gst:{'%.0f' % nass}    withgst:{nass + ((nass * gst) / 100)}")  # show the data as label
                self.totle_list_label[self.nos].adjustSize()
                self.totle_list_label[self.nos].show()
                # ----------------------------------------full total label-----------------------------------------------
                self.total.setText(f"Total:{'%.0f' % pre}    Total withgst:{with_gst_total}")
                self.total.adjustSize()
                self.total.show()

                ks = pre
                self.nos += 1
        except TypeError:

            self.totle_list_label[self.nos].setText(
                f"plzz enter integer value")  # show the data as label
            self.totle_list_label[self.nos].adjustSize()
            self.totle_list_label[self.nos].show()
            print("dasfds")
            pass

        time = threading.Timer(time, self.loop)
        if self.start == False:
            time.cancel()
        else:
            time.start()  # start the loop

    def geting_all_values(self):
        # self.start = False
        # -------------------------------------getting all values entry's---------------------------------
        self.geting_values_of_top_list = []
        self.data_all_entry_list = []
        for vaues in self.top_entry:
            self.geting_values_of_top_list.append(vaues.text())
        for data in self.all_entry_list:
            temperli_list = []
            for data in data:
                temperli_list.append(data.text())
            self.data_all_entry_list.append(temperli_list)

        # ---------------------------------creating pdf-------------------------------------

    def creating_pdf(self):
        self.geting_all_values()
        path = QFileDialog.getExistingDirectory(self)
        jj = xyz.drawstring(self.data_all_entry_list,
                            self.geting_values_of_top_list, path)


def main():
    app = QApplication(sys.argv)
    win = my_cal()
    win.setStyleSheet("color: #433f5b;"
                      "text-shadow: 2px 2px 4px #000000;"
                      "font-family: Cursive;"
                      "font-size: 300%;"
                      "background-color: rgb(230, 230, 250);"
                      )
    win.show()
    try:
        exit(app.exec_())
    except:
        print("----------Error---------")


main()
