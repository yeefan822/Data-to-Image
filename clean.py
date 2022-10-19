from PIL import Image
import numpy as np
from csv import reader
import cv2
from matplotlib import pyplot as plt


with open('dirty_image_1024.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    array=[]
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        temp = row[0].split()
        array.append(np.asarray(temp))
with open('point_spread_function_1024.csv', 'r') as read_obj1:
    # pass the file object to reader() to get the reader object
    csv_reader1 = reader(read_obj1)
    array1=[]
    # Iterate over each row in the csv using reader object
    for row in csv_reader1:
        # row variable is a list that represents a row in csv
        temp1 = row[0].split()
        array1.append(np.asarray(temp1))
formatted = np.asarray(array)
formatted1=np.asarray(array1)
psf=formatted1.astype(np.float64)
floatversion = formatted.astype(np.float64)
dirty = formatted.astype(np.float64)
for i in range(6000):
    maxindex=floatversion.argmax()
    #print(floatversion[int(maxindex/1024)][maxindex-int(maxindex/1024)*1024])
    floatversion[int(maxindex/1024)][maxindex-int(maxindex/1024)*1024]=floatversion[int(maxindex/1024)][maxindex-int(maxindex/1024)*1024]+0.2*psf[int(maxindex/1024)][maxindex-int(maxindex/1024)*1024]
    #print(floatversion[int(maxindex/1024)][maxindex-int(maxindex/1024)*1024])
    #print(dirty[int(maxindex/1024)][maxindex-int(maxindex/1024)*1024]-floatversion[int(maxindex/1024)][maxindex-int(maxindex/1024)*1024])

image = (floatversion - np.amin(floatversion))/(np.amax(floatversion)-np.amin(floatversion))
image = (image*255).astype(np.uint8)
print(floatversion[511][519])
plt.imshow(image,interpolation='none')
plt.colorbar()
plt.show()
