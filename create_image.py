from PIL import Image
import numpy as np
import os

import filerw


def invert_array(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = (int(a[i][j] == 0))
    return a

# сохраненные образы
x = filerw.read_file_to_two_dimensional_array_of_ints("letter_e1.txt")

data = np.array(x)
data = data.reshape(8,8)
data = invert_array(data)
img = Image.fromarray(data.astype('uint8')*255, mode='L')
img.save("e1.png")

