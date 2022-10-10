from PIL import Image
import numpy as np
from csv import reader
import csv

with open('point_spread_function_1024.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    array=[]
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        temp = row[0].split()
        temp2 = np.repeat(temp,2)
        array.append(np.asarray(temp2))

formatted = np.asarray(array)
x = np.repeat(formatted,2,axis=0)
with open("point_spread_function_2048.csv","w+") as my_csv:
    csv_writer = csv.writer(my_csv,delimiter=",")
    csv_writer.writerows(x)
print(x.size)
# floatversion = formatted.astype(np.float64)
# print(np.amax(floatversion))
# print(np.amin(floatversion))
# abovezero = floatversion - np.amin(floatversion)
# print(np.amin(abovezero))
# print(np.amax(abovezero))
# portion = 255/np.amax(abovezero)
# unit8array = abovezero * portion
# intversion = unit8array.astype(np.uint8)
# img = Image.fromarray(intversion)
# img.show()