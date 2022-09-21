from PIL import Image
import numpy as np
from csv import reader

with open('residual_image_1024.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    array=[]
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        temp = row[0].split()
        array.append(np.asarray(temp))
# slice56 = np.random.random((1024, 1024))
# print(array)
formatted = np.asarray(array)
floatversion = formatted.astype(np.float64)


# formatted = (slice56 * 65535 / np.max(slice56)).astype('uint16')
intversion = floatversion.astype(np.int32)
img = Image.fromarray(intversion)
img.show()