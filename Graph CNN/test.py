import numpy as np
import cv2 as cv
import glob
import networkx as nx
import matplotlib.pyplot as plt
import scipy
from scipy.spatial import distance

img =cv.imread("D:\Hoc_ky_212_2022\De_cuong_luan_van_tot_nghiep\gg (9).jpg",cv.IMREAD_GRAYSCALE)
threshold = img.copy()
threshold[threshold <= 120] = 0
threshold[threshold > 120] = 255
#image = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
#image = cv.resize(img_1, (50,50))
cv.imshow("cat",img)
cv.waitKey()