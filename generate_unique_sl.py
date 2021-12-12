import random as r
from barcode import EAN13
from barcode.writer import ImageWriter
import pyqrcode
import os
import zipmaker
 

def codegenerator(n):
    number_of_codes = int(n)
    def generate_code():
        l = "0123456789"
        n = len(l)
        s = ""
        i = 0
        while i<15:
            s = s+l[r.randint(0,n-1)]
            i=i+1
        return s
    j = 0
    content = ""
    codes = []
    s = ""
    while j<number_of_codes:
        s = generate_code()
        content = content + s + "\n"
        if s not in codes:
            codes.append(s)
            j = j+1
        
    file = open("static/serials/codes/serials.txt", "w")
    file.write(content) 
    file.close()
    print("codes generated in ./serials.txt file")  

    itr = 1
    for x in codes:
        number = x
        my_code = EAN13(number, writer=ImageWriter())
        my_code.save(f"static/serials/barcodes/barcode_{itr}")
        data = pyqrcode.create(number)
        data.png(f'static/serials/qrcodes/qrcode_{itr}.png', scale = 8)
        itr = itr+1
    folders = [
    "static/serials/barcodes",
    "static/serials/qrcodes",
    "static/serials/codes"
    ]

    zipmaker.zipit(folders, "static/downloads/serials.zip")
