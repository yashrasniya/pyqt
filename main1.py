import calculation1
import drawstring as dr
from reportlab.pdfgen import canvas
import os

class drawstring:
    def __int__(self, list_of_top_entrys, list_of_all_entrys,path):
        self.list_of_top_entrys = list_of_top_entrys
        self.list_of_all_entrys = list_of_all_entrys
        self.path=path
        self.cal = calculation.clculation()
        self.datetime = self.cal.time()

        self.pdf = canvas.Canvas(f"{self.list_of_top_entrys[2]}{self.datetime}.pdf")
        self.pdf.drawImage('pdf_3.jpg', 0, 00, width=595.276, height=841.89)
        self.start()

    def start(self):
        drawstring = dr.drawstring()
        drawstring.start(self.list_of_top_entrys, self.pdf)
        os.chdir(self.path)
        self.pdf.save()
        pass
