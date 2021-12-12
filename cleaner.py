import shutil
import os

def clean_folder():
    shutil.rmtree("static/serials/barcodes")
    os.mkdir("static/serials/barcodes")
    shutil.rmtree("static/serials/qrcodes")
    os.mkdir("static/serials/qrcodes")
    shutil.rmtree("static/serials/codes")
    os.mkdir("static/serials/codes")
    shutil.rmtree("static/downloads")
    os.mkdir("static/downloads")
    
# clean_folder()