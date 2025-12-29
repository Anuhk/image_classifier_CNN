import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets,layers,models



(training_img,training_labels),(testing_img,testing_labels)=datasets.cifar10.load_data()

#Scale down intensity values from 0-255 to 0-1
training_img,testing_img=training_img/255,testing_img/255

class_names=['Plane','Car','Bird','cat','Deer','Dog','Frog','Horse','Ship','Truck']

for i in range(16):
    plt.subplot(4,4,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(training_img[i],cmap=plt.cm.binary)
    plt.xlabel(class_names[training_labels[i][0]])

plt.show()

