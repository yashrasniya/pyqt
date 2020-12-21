class drawing:
    def __int__(self):
        pass

    def drawing_data(self):
    try:
        print(self.gst_in_percentage)
        self.gst = int(self.gst_in_percentage)

    except:
        total = 0
        count = 0
        for gst in self.list_name:
            print(gst[1])
            total = int(gst[1]) + total
            count += 1
        self.gst = int(total / count)

    self.pdf.setFontSize(9)
    self.name = self.name.upper()
    self.pdf.drawString(130, 622, self.invoic_number)
    self.pdf.drawString(130, 610, self.date)
    self.pdf.drawString(90, 575, self.name)
    if len(self.address) > 38:
        address_1 = self.address[0:38]
        address_2 = self.address[38:]
        self.pdf.drawString(90, 560, address_1)
        if len(address_2) > 38:
            self.pdf.setFontSize(7)
        self.pdf.drawString(90, 548, address_2)
        self.pdf.setFontSize(9)
    else:
        self.pdf.drawString(90, 560, self.address)

    self.pdf.drawString(90, 528, self.gst_number)
    self.pdf.drawString(90, 515, self.state)
    self.pdf.drawString(250, 510, self.state_code)
    self.pdf.drawString(130, 600, "UTTARAKHAND")
    self.pdf.drawString(250, 600, "05")
    self.prooses()