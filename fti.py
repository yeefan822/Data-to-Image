from PIL import Image
import numpy as np

slice56 = np.random.random((1024, 1024))

# convert values to 0 - 65535 int16 format
formatted = (slice56 * 65535 / np.max(slice56)).astype('uint16')
img = Image.fromarray(formatted)
img.show()