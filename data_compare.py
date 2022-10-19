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
with open('img.csv', 'r') as read_obj1:
    # pass the file object to reader() to get the reader object
    csv_reader1 = reader(read_obj1)
    array1=[]
    # Iterate over each row in the csv using reader object
    for row in csv_reader1:
        # row variable is a list that represents a row in csv
        if(len(row)>0):
            temp1 = row[0].split()
        
            array1.append(np.asarray(temp1))
formatted = np.asarray(array)
formatted1=np.asarray(array1)
result=formatted1.astype(np.float64)
floatversion = formatted.astype(np.float64)
print(np.amax(floatversion))
print(np.amax(result))
