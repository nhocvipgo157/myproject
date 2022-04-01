import cv2 as cv
import numpy as np
import keras
import os

categories = ["Cat","Dog","Panda","Unknown"]
categories_1 = [""]
datadir = ("Testing")

img_size = 244
def prepare(filepath):
    img_array = cv.imread(filepath,cv.IMREAD_GRAYSCALE)
    new_array = cv.resize(img_array, (img_size, img_size))
    new_array = new_array / 255.0
    return new_array.reshape(-1, img_size, img_size, 1)

model = keras.models.load_model('train_model.pb')


path_img = "A:\Pictures\Wallpaper\cau-do-ngay-ca-thang-tu-cau-do-1-4-ngay-noi-doi.jpg"
prediction = model.predict([prepare('{}'.format(path_img))])
print(prediction)
dudoan = categories[int(np.argmax(prediction))]
print(dudoan)
       
        