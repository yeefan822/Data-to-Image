from PIL import Image
import numpy as np
from csv import reader
import cv2
from matplotlib import pyplot as plt


with open('residual_1024.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    array=[]
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        temp = row[0].split()
        array.append(np.asarray(temp))
with open('dirty_image_1024.csv', 'r') as read_obj1:
    # pass the file object to reader() to get the reader object
    csv_reader1 = reader(read_obj1)
    array1=[]
    # Iterate over each row in the csv using reader object
    for row in csv_reader1:
        # row variable is a list that represents a row in csv
        temp1 = row[0].split()
        array1.append(np.asarray(temp1))
formatted = np.asarray(array)
formatted1 = np.asarray(array1)
floatversion = formatted.astype(np.float64)
floatversion1 = formatted1.astype(np.float64)
fv = floatversion1 - floatversion

image = (fv - np.amin(fv))/(np.amax(fv)-np.amin(fv))
image = (image*255).astype(np.uint8)

#image = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
#print(image)
plt.imshow(image,interpolation='none')
plt.colorbar()
plt.show()
#img=Image.fromarray(image, "RGB")
#img.show()
# print(np.amax(floatversion))
# print(np.amin(floatversion))
# abovezero = floatversion - np.amin(floatversion)
# print(np.amin(abovezero))
# print(np.amax(abovezero))
# portion = 255/np.amax(abovezero)
# rgbarray = abovezero * portion
# intversion = rgbarray.astype(np.uint8)
# img = Image.fromarray(intversion)
# img.show()
