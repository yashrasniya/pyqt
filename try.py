import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import setting_data_saver_and_updating

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 140

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        array=[]
        apaa=[234,23454,235,23425,2]
        b=1
        for a in apaa:
            array.append(QPushButton(f"{a}", self))
            array[-1].move(20*b, 80*b)
            array[-1].setObjectName(f"gog{a}")
            b+=1
            print(a)
        # connect button to function on_click
            array[-1].clicked.connect(lambda state,x=a: self.on_click(x))
        self.textbox.setText("happy")
        self.show()

    def on_click(self,a):
        print(a)






app = QtWidgets.QApplication(sys.argv)
ex = App()
print(ex.initUI())
sys.exit(app.exec_())

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#
#     sys.exit(app.exec_())