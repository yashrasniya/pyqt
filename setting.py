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
                QtCore.QRect(scrollArea_Geometry[-4], scrollArea_Geometry[-3], scrollArea_Geometry[-2],
                             scrollArea_Geometry[-1]))
            self.scrollArea[-1].setWidgetResizable(True)
            self.scrollArea[-1].setObjectName("scrollArea")
            self.scrollAreaWidgetContents.append(QtWidgets.QWidget())
            self.scrollAreaWidgetContents[-1].setGeometry(
                QtCore.QRect(scrollAreaWidgetContents_Geometry[-4], scrollAreaWidgetContents_Geometry[-3],
                             scrollAreaWidgetContents_Geometry[-2], scrollAreaWidgetContents_Geometry[-1]))
            self.scrollAreaWidgetContents[-1].setObjectName("scrollAreaWidgetContents")
            self.verticalLayout.append(QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents[-1]))
            self.verticalLayout[-1].setObjectName(f"{self.verticalLayout[-1]}")
            # =================================================================

            for id,name, enabled, maximum_number_x, maximum_number_y in data:
                entry_list = []
                self.items_list.append(QtWidgets.QGroupBox(self.scrollAreaWidgetContents[-1]))
                self.items_list[-1].setObjectName(name)
                self.horizontalLayout.append(QtWidgets.QHBoxLayout(self.items_list[-1]))
                self.horizontalLayout[-1].setObjectName(f"{name}horizontalLayout")
                entry_list.append(QtWidgets.QSpinBox(self.items_list[-1]))
                entry_list[-1].setEnabled(bool(enabled))
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
                    fist_name.setValue(int(entry_values_list[a][-2]))
                    fist_name.show()
                    second_name.setValue(int(entry_values_list[a][-1]))
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
