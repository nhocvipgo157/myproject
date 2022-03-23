import numpy as np
import cv2 as cv
import glob
import networkx as nx
import matplotlib.pyplot as plt
import scipy
from scipy.spatial import distance

img =cv.imread("D:\Hoc_ky_212_2022\De_cuong_luan_van_tot_nghiep\gg (9).jpg",cv.IMREAD_GRAYSCALE)
cat,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
#image = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
#image = cv.resize(img_1, (50,50))
cv.imshow("cat",thresh1)
cv.waitKey()