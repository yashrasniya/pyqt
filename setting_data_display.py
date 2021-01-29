import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
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
        self.button = QPushButton('Save and Exit', self)
        self.button.move(20, 80)

        # connect button to function on_click
        self.button.clicked.connect(lambda: setting_data_saver_and_updating.gogo(self.textbox.text()))
        self.textbox.setText("happy")
        self.show()
        return self.textbox.text()

    @pyqtSlot()
    def on_click(self):
        self.textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + self.textboxValue, QMessageBox.Ok,
                             QMessageBox.Ok)
        # self.textbox.setText("")
        return self.textbox.text()




# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#
#     sys.exit(app.exec_())