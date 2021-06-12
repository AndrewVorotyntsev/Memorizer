from PIL import Image
import numpy as np
import os

import filerw


def invert_array(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = (int(a[i][j] == 0))
    return a


def refresh_image_memory():
    # сохраненные образы
    t = filerw.read_file_to_two_dimensional_array_of_ints("t.txt")
    for i in range(10):
        data = np.array(t[i])
        data = data.reshape(8,8)
        data = invert_array(data)
        img = Image.fromarray(data.astype('uint8')*255, mode='L')
        main = os.path.dirname(__file__)
        file_name = "neuron_" + str(i) + ".png"
        # Формируем путь до файла
        file_path = os.path.join(main, "neurons", file_name)
        img.save(file_path)

