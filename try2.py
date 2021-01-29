import PySide.QtCore as qc
import PySide.QtGui as qg
class simpleUI(qg.QDialog):
    def __init__(self):
        qg.QDialog.__init__(self)
        self.setWindowTitle('Simple UI')
        self.btn=[]
        for x in range(5) :
           self.btn.append(x)
           self.btn[x]= qg.QPushButton(self)
           self.btn[x].setText('this is btn number{0}'.format(x))
           self.btn[x].setGeometry(qc.QRect(0,100+(x*20), 100,20))
           self.btn[x].clicked.connect(lambda a=x: self.notifyMe(a))
    def notifyMe(self,index):
        print(index)
dialog = simpleUI()
dialog.show()