import numpy as np
import cv2 as cv
import glob
import networkx as nx
import matplotlib.pyplot as plt
import scipy
from scipy.spatial import distance
img =cv.imread("D:\Hoc_ky_212_2022\De_cuong_luan_van_tot_nghiep\gg (9).jpg",cv.IMREAD_GRAYSCALE)
cat,img_1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
#image = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,8,2)
image = cv.resize(img_1, (50,50))


#CONSTRUCTION OF HORIZONTAL EDGES
hx, hy = np.where(image[1:] & image[:-1]) #horizontal edge start positions
h_units = np.array([hx, hy]).T
h_starts = [tuple(n) for n in h_units]
h_ends = [tuple(n) for n in h_units + (1, 0)] #end positions = start positions shifted by vector (1,0)
horizontal_edges = zip(h_starts, h_ends)

#CONSTRUCTION OF VERTICAL EDGES
vx, vy = np.where(image[:,1:] & image[:,:-1]) #vertical edge start positions
v_units = np.array([vy, vx]).T
v_starts = [tuple(n) for n in v_units]
v_ends = [tuple(n) for n in v_units + (0, 1)] #end positions = start positions shifted by vector (0,1)
vertical_edges = zip(v_starts, v_ends)

G = nx.Graph()
G.add_edges_from(horizontal_edges)
G.add_edges_from(vertical_edges)

nx.draw(G)
plt.show()
