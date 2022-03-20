import cv2 as cv
import os
import openpyxl
from openpyxl import Workbook
import glob

wb = Workbook()
ws = wb.active

for image in glob.glob("/home/son/Myproject/Thuc_tap/Btap_1/*.jpg"):
    img = cv.imread(image)
    (w,h,c) = img.shape
    print(w,h,c)
    img_new = cv.resize(img,(int(h/2),int(w/2)))
    basename = os.path.basename(image)
    name = os.path.splitext(basename)[0]
    ws.append([name,"{}x{}".format(h,w),"{}x{}".format(int(h/2),int(w/2))])
    wb.save("/home/son/Myproject/Thuc_tap/Btap_1/Btap_1_b.xlsx")