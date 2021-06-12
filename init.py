import utils
import filerw
import mem
import random


def init_recognition():
    b = []
    amount_of_images = 10
    length_of_image = 64
    max = 2/(1 + length_of_image)
    for j in range(amount_of_images):
        b.append([])
        for i in range(length_of_image):
            b[j].append(round(random.uniform(0, max), 4))
    return b


# веса нейронов слой распознования

# изначально одинаково малые значения
b = init_recognition()  # 10 x 64
filerw.write_array_to_file_in_many_lines(b, "b.txt")

# изначально все единицы
# сохраненный образы
t = utils.ones(10, 64)
filerw.write_array_to_file_in_many_lines(t, "t.txt")

p = utils.zeros(64)
filerw.write_array_to_file_in_one_line([p], "p.txt")

# Обновляем изображения в папке neurons
mem.refresh_image_memory()

print("Инициализация сети завершена")
