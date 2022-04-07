from PIL import Image
import numpy as np
import cv2 as cv
import networkx as nx
import scipy
from scipy.spatial import distance
import matplotlib.pyplot as plt

G = nx.Graph()
size = 4
img_1 = cv.imread("D:\Hoc_ky_212_2022\De_cuong_luan_van_tot_nghiep\Graph CNN\cat.jpg",cv.IMREAD_GRAYSCALE)
img = cv.resize(img_1,(size,size))
n = 0
rows = img.shape[0]
columns = img.shape[1]
print(rows)
print(columns)

pos=nx.get_node_attributes(G,'pos')
for x in range(0, rows):
    for y in range(0, columns):
            n += 1
            G.add_node(n,pos = (y,x))
            pos=nx.get_node_attributes(G,'pos')
print(pos)
print(img[0])    

# Generating Edges based on the max distance allowed
for x in G.nodes:
    for y in G.nodes:
        G.add_edge(x, y)

nx.draw(G,pos=pos, with_labels=True)
print(img)
plt.imshow(img)
plt.show()

