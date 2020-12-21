# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seting.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self, data):
        self.verticalLayout = []
        self.scrollAreaWidgetContents = []
        # self.data = [
        #
        #     [[["1", True, 999, 999, ], ["2", True, 999, 999, ], ["3", True, 999, 999, ], ["4", True, 999, 999, ],
        #       ["1", True, 999, 999, ], ["2", True, 999, 999, ], ["3", True, 999, 999, ], ["4", True, 999, 999, ],
        #       ["1", True, 999, 999, ], ["2", True, 999, 999, ], ["3", True, 999, 999, ], ["4", True, 999, 999, ]],
        #      [0, 0, 281, 401], [0, 0, 265, 544]],
        #
        #     [[["5", True, 999, 999, ], ["6", True, 999, 999, ], ["7", True, 999, 999, ], ["4", True, 999, 999, ]],
        #      [280, 0, 271, 401], [0, -601, 255, 1000]]
        #
        # ]
        self.data=data
        self.scrollArea = []
        self.horizontalLayout = []
        self.entry_list = []
        self.items_list = []

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 419)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = []
        # =================================================================
        for data, scrollArea_Geometry, scrollAreaWidgetContents_Geometry in self.data:

            self.scrollArea.append(QtWidgets.QScrollArea(self.centralwidget))
            self.scrollArea[-1].setGeometry(
                QtCore.QRect(scrollArea_Geometry[0], scrollArea_Geometry[1], scrollArea_Geometry[2],
                             scrollArea_Geometry[3]))
            self.scrollArea[-1].setWidgetResizable(True)
            self.scrollArea[-1].setObjectName("scrollArea")
            self.scrollAreaWidgetContents.append(QtWidgets.QWidget())
            self.scrollAreaWidgetContents[-1].setGeometry(
                QtCore.QRect(scrollAreaWidgetContents_Geometry[0], scrollAreaWidgetContents_Geometry[1],
                             scrollAreaWidgetContents_Geometry[2], scrollAreaWidgetContents_Geometry[3]))
            self.scrollAreaWidgetContents[-1].setObjectName("scrollAreaWidgetContents")
            self.verticalLayout.append(QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents[-1]))
            self.verticalLayout[-1].setObjectName(f"{self.verticalLayout[-1]}")
            # =================================================================

            for name, enabled, maximum_number_x, maximum_number_y in data:
                entry_list = []
                self.items_list.append(QtWidgets.QGroupBox(self.scrollAreaWidgetContents[-1]))
                self.items_list[-1].setObjectName(name)
                self.horizontalLayout.append(QtWidgets.QHBoxLayout(self.items_list[-1]))
                self.horizontalLayout[-1].setObjectName(f"{name}horizontalLayout")
                entry_list.append(QtWidgets.QSpinBox(self.items_list[-1]))
                entry_list[-1].setEnabled(enabled)
                entry_list[-1].setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                entry_list[-1].setMaximum(maximum_number_x)
                entry_list[-1].setObjectName(f"{name}_x")
                self.horizontalLayout[-1].addWidget(entry_list[-1])
                entry_list.append(QtWidgets.QSpinBox(self.items_list[-1]))
                entry_list[-1].setMaximum(maximum_number_y)
                entry_list[-1].setObjectName(f"{name}_y")
                self.horizontalLayout[-1].addWidget(entry_list[-1])
                self.verticalLayout[-1].addWidget(self.items_list[-1])
                _translate = QtCore.QCoreApplication.translate
                self.items_list[-1].setTitle(_translate("MainWindow", name))
                # ==============================================================
                self.entry_list.append(entry_list)  # main list for data fetching
                # ==============================================================
                self.scrollArea[-1].setWidget(self.scrollAreaWidgetContents[-1])

        # =================================================================

        # =================================================================

        # =================================================================

        # =================================================================

        # # =================================================================
        # self.address = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        # self.address.setObjectName("address")
        # self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.address)
        # self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        # self.address_x = QtWidgets.QSpinBox(self.address)
        # self.address_x.setMaximum(999)
        # self.address_x.setObjectName("address_x")
        # self.horizontalLayout_8.addWidget(self.address_x)
        # self.address_y = QtWidgets.QSpinBox(self.address)
        # self.address_y.setMaximum(999)
        # self.address_y.setObjectName("address_y")
        # self.horizontalLayout_8.addWidget(self.address_y)
        # self.verticalLayout_3.addWidget(self.address)
        # # =================================================================
        # self.state_of_bayer = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        # self.state_of_bayer.setObjectName("state_of_bayer")
        # self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.state_of_bayer)
        # self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        # self.state_of_bayer_x = QtWidgets.QSpinBox(self.state_of_bayer)
        # self.state_of_bayer_x.setMaximum(999)
        # self.state_of_bayer_x.setObjectName("state_of_bayer_x")
        # self.horizontalLayout_4.addWidget(self.state_of_bayer_x)
        # self.state_of_bayer_y = QtWidgets.QSpinBox(self.state_of_bayer)
        # self.state_of_bayer_y.setMaximum(999)
        # self.state_of_bayer_y.setObjectName("state_of_bayer_y")
        # self.horizontalLayout_4.addWidget(self.state_of_bayer_y)
        # self.verticalLayout_3.addWidget(self.state_of_bayer)
        # # =================================================================
        # self.state_code_of_saleer.raise_()
        # self.name.raise_()
        # self.address.raise_()
        # self.state_of_bayer.raise_()
        # self.state_of_saleer.raise_()
        # self.invoice_date.raise_()
        # # ================================================================
        # # =================================================================
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        # self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        # self.scrollArea_2.setGeometry(QtCore.QRect(280, 0, 271, 401))
        # self.scrollArea_2.setWidgetResizable(True)
        # self.scrollArea_2.setObjectName("scrollArea_2")
        # self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, -601, 255, 1000))
        # self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        # self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        # self.verticalLayout.setObjectName("verticalLayout")
        # self.serial_number = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        # self.serial_number.setObjectName("serial_number")
        # self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.serial_number)
        # self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        # # =================================================================
        # self.serial_number_x = QtWidgets.QSpinBox(self.serial_number)
        # self.serial_number_x.setMaximum(999)
        # self.serial_number_x.setObjectName("serial_number_x")
        # self.horizontalLayout_21.addWidget(self.serial_number_x)
        # self.serial_number_y = QtWidgets.QSpinBox(self.serial_number)
        # self.serial_number_y.setMaximum(999)
        # self.serial_number_y.setObjectName("serial_number_y")
        # self.horizontalLayout_21.addWidget(self.serial_number_y)
        # self.verticalLayout.addWidget(self.serial_number)
        # # =================================================================
        # self.Name_of_Product = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        # self.Name_of_Product.setObjectName("Name_of_Product")
        # self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.Name_of_Product)
        # self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        # self.name_of_producy_x = QtWidgets.QSpinBox(self.Name_of_Product)
        # self.name_of_producy_x.setMaximum(999)
        # self.name_of_producy_x.setObjectName("name_of_producy_x")
        # self.horizontalLayout_11.addWidget(self.name_of_producy_x)
        # self.name_of_product_y = QtWidgets.QSpinBox(self.Name_of_Product)
        # self.name_of_product_y.setMaximum(999)
        # self.name_of_product_y.setObjectName("name_of_product_y")
        # self.horizontalLayout_11.addWidget(self.name_of_product_y)
        # self.verticalLayout.addWidget(self.Name_of_Product)
        # # =================================================================
        # self.Qty = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        # self.Qty.setObjectName("Qty")
        # self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.Qty)
        # self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        # self.Qty_x = QtWidgets.QSpinBox(self.Qty)
        # self.Qty_x.setMaximum(999)
        # self.Qty_x.setObjectName("Qty_x")
        # self.horizontalLayout_12.addWidget(self.Qty_x)
        # self.Qty_y = QtWidgets.QSpinBox(self.Qty)
        # self.Qty_y.setMaximum(999)
        # self.Qty_y.setObjectName("Qty_y")
        # self.horizontalLayout_12.addWidget(self.Qty_y)
        # self.verticalLayout.addWidget(self.Qty)
        # # =================================================================
        # self.Rate = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        # self.Rate.setObjectName("Rate")
        # self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.Rate)
        # self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        # self.rate_x = QtWidgets.QSpinBox(self.Rate)
        # self.rate_x.setMaximum(999)
        # self.rate_x.setObjectName("rate_x")
        # self.horizontalLayout_9.addWidget(self.rate_x)
        # self.rate_y = QtWidgets.QSpinBox(self.Rate)
        # self.rate_y.setMaximum(999)
        # self.rate_y.setObjectName("rate_y")
        # self.horizontalLayout_9.addWidget(self.rate_y)
        # self.verticalLayout.addWidget(self.Rate)
        # # =================================================================
        # self.Amount = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        # self.Amount.setObjectName("Amount")
        # self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.Amount)
        # self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        # self.amount_x = QtWidgets.QSpinBox(self.Amount)
        # self.amount_x.setMaximum(999)
        # self.amount_x.setObjectName("amount_x")
        # self.horizontalLayout_10.addWidget(self.amount_x)
        # self.amount_y = QtWidgets.QSpinBox(self.Amount)
        # self.amount_y.setMaximum(999)
        # self.amount_y.setObjectName("amount_y")
        # self.horizontalLayout_10.addWidget(self.amount_y)
        # self.verticalLayout.addWidget(self.Amount)
        # # =================================================================
        # self.amount_total = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        # self.amount_total.setObjectName("amount_total")
        # self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.amount_total)
        # self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        # self.amount_total_x = QtWidgets.QSpinBox(self.amount_total)
        # self.amount_total_x.setMaximum(999)
        # self.amount_total_x.setObjectName("amount_total_x")
        # self.horizontalLayout_13.addWidget(self.amount_total_x)
        # self.amount_total_y = QtWidgets.QSpinBox(self.amount_total)
        # self.amount_total_y.setMaximum(999)
        # self.amount_total_y.setObjectName("amount_total_y")
        # self.horizontalLayout_13.addWidget(self.amount_total_y)
        # self.verticalLayout.addWidget(self.amount_total)
        # # =================================================================
        # self.tax_amount = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        # self.tax_amount.setObjectName("tax_amount")
        # self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.tax_amount)
        # self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        # self.tax_amount_x = QtWidgets.QSpinBox(self.tax_amount)
        # self.tax_amount_x.setMaximum(999)
        # self.tax_amount_x.setObjectName("tax_amount_x")
        # self.horizontalLayout_17.addWidget(self.tax_amount_x)
        # self.tax_amount_y_2 = QtWidgets.QSpinBox(self.tax_amount)
        # self.tax_amount_y_2.setMaximum(999)
        # self.tax_amount_y_2.setObjectName("tax_amount_y_2")
        # self.horizontalLayout_17.addWidget(self.tax_amount_y_2)
        # self.verticalLayout.addWidget(self.tax_amount)
        # # =================================================================
        # self.total_amount_after_tax = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        # self.total_amount_after_tax.setObjectName("total_amount_after_tax")
        # self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.total_amount_after_tax)
        # self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        # self.total_amount_after_tax_x = QtWidgets.QSpinBox(self.total_amount_after_tax)
        # self.total_amount_after_tax_x.setMaximum(999)
        # self.total_amount_after_tax_x.setObjectName("total_amount_after_tax_x")
        # self.horizontalLayout_18.addWidget(self.total_amount_after_tax_x)
        # self.tax_amount_y = QtWidgets.QSpinBox(self.total_amount_after_tax)
        # self.tax_amount_y.setMaximum(999)
        # self.tax_amount_y.setObjectName("tax_amount_y")
        # self.horizontalLayout_18.addWidget(self.tax_amount_y)
        # self.verticalLayout.addWidget(self.total_amount_after_tax)
        # # =================================================================
        # self.total_invoice_amount_in_word = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        # self.total_invoice_amount_in_word.setObjectName("total_invoice_amount_in_word")
        # self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.total_invoice_amount_in_word)
        # self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        # self.total_invoice_amount_in_word_x = QtWidgets.QSpinBox(self.total_invoice_amount_in_word)
        # self.total_invoice_amount_in_word_x.setMaximum(999)
        # self.total_invoice_amount_in_word_x.setObjectName("total_invoice_amount_in_word_x")
        # self.horizontalLayout_19.addWidget(self.total_invoice_amount_in_word_x)
        # self.total_invoice_amount_in_word_y = QtWidgets.QSpinBox(self.total_invoice_amount_in_word)
        # self.total_invoice_amount_in_word_y.setMaximum(999)
        # self.total_invoice_amount_in_word_y.setObjectName("total_invoice_amount_in_word_y")
        # self.horizontalLayout_19.addWidget(self.total_invoice_amount_in_word_y)
        # self.verticalLayout.addWidget(self.total_invoice_amount_in_word)
        # # =================================================================
        # self.cgst = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        # self.cgst.setObjectName("cgst")
        # self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.cgst)
        # self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        # self.cgst_x = QtWidgets.QSpinBox(self.cgst)
        # self.cgst_x.setMaximum(999)
        # self.cgst_x.setObjectName("cgst_x")
        # self.horizontalLayout_20.addWidget(self.cgst_x)
        # self.cgst_y = QtWidgets.QSpinBox(self.cgst)
        # self.cgst_y.setMaximum(999)
        # self.cgst_y.setObjectName("cgst_y")
        # self.horizontalLayout_20.addWidget(self.cgst_y)
        # self.verticalLayout.addWidget(self.cgst)
        # # =================================================================
        # self.sgst = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        # self.sgst.setObjectName("sgst")
        # self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.sgst)
        # self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        # self.sgst_x = QtWidgets.QSpinBox(self.sgst)
        # self.sgst_x.setMaximum(999)
        # self.sgst_x.setObjectName("sgst_x")
        # self.horizontalLayout_14.addWidget(self.sgst_x)
        # self.sgst_y = QtWidgets.QSpinBox(self.sgst)
        # self.sgst_y.setMaximum(999)
        # self.sgst_y.setObjectName("sgst_y")
        # self.horizontalLayout_14.addWidget(self.sgst_y)
        # self.verticalLayout.addWidget(self.sgst)
        # # =================================================================
        # self.cgst_percentage = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        # self.cgst_percentage.setObjectName("cgst_percentage")
        # self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.cgst_percentage)
        # self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        # self.cgst_percentage_x = QtWidgets.QSpinBox(self.cgst_percentage)
        # self.cgst_percentage_x.setMaximum(999)
        # self.cgst_percentage_x.setObjectName("cgst_percentage_x")
        # self.horizontalLayout_15.addWidget(self.cgst_percentage_x)
        # self.cgst_percentage_y = QtWidgets.QSpinBox(self.cgst_percentage)
        # self.cgst_percentage_y.setMaximum(999)
        # self.cgst_percentage_y.setObjectName("cgst_percentage_y")
        # self.horizontalLayout_15.addWidget(self.cgst_percentage_y)
        # self.verticalLayout.addWidget(self.cgst_percentage)
        # # =================================================================
        # self.sgst_percentage = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        # self.sgst_percentage.setObjectName("sgst_percentage")
        # self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.sgst_percentage)
        # self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        # self.sgst_percentage_x = QtWidgets.QSpinBox(self.sgst_percentage)
        # self.sgst_percentage_x.setMaximum(999)
        # self.sgst_percentage_x.setObjectName("sgst_percentage_x")
        # self.horizontalLayout_16.addWidget(self.sgst_percentage_x)
        # self.sgst_percentage_y = QtWidgets.QSpinBox(self.sgst_percentage)
        # self.sgst_percentage_y.setMaximum(999)
        # self.sgst_percentage_y.setObjectName("sgst_percentage_y")
        # self.horizontalLayout_16.addWidget(self.sgst_percentage_y)
        # self.sgst_percentage_y.raise_()
        # self.sgst_percentage_x.raise_()
        # self.verticalLayout.addWidget(self.sgst_percentage)
        # =================================================================

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        return self.entry_list

    def finding_output(self, entry_list_name, do_you_want_to_set_value=False, entry_values_list=None):

        if do_you_want_to_set_value != True:
            full_list_of_entry_data = []
            for small_list in entry_list_name:
                x_and_y_data_list = []
                for entry_name in small_list:
                    x_and_y_data_list.append(entry_name.value())
                full_list_of_entry_data.append(x_and_y_data_list)

            return full_list_of_entry_data
        elif do_you_want_to_set_value:
            a = 0

            for fist_name,second_name in entry_list_name:
                b = 0
                try:
                    fist_name.setValue(int(entry_values_list[a][-1]))
                    fist_name.show()
                    second_name.setValue(int(entry_values_list[a][-2]))
                    second_name.show()
                except TypeError:
                    pass
                a += 1

    def start(self, data_of_entry, do_you_want_to_set_value=False, entry_values_list=None):

        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow(data_of_entry)
        entry_list_name = ui.setupUi(MainWindow)

        if do_you_want_to_set_value:
            print(do_you_want_to_set_value)
            print(entry_values_list)
            self.finding_output(entry_list_name, do_you_want_to_set_value=do_you_want_to_set_value,
                                entry_values_list=entry_values_list)
        MainWindow.show()
        app.exec_()

        return self.finding_output(entry_list_name, do_you_want_to_set_value=False, entry_values_list=entry_values_list)
        # sys.exit()
