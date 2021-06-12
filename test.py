from PIL import Image
import numpy as np


def invert_array(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = (int(a[i][j] == 0))
    return a


data = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
data = invert_array(data)

data = np.array(data)
print(data)
my_array = [0,1,1,1,1,1,1,0,0]
my_array = np.array(my_array)
my_array = my_array.reshape((3, 3))
img = Image.fromarray(data.astype('uint8')*255, mode='L')
img.save('my.png')
img.show()
