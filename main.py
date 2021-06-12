import os
import filerw
import imagerw
import utils
import mem


def comparison(x, r, g1):
    c = [int(x[i] + r[i] + g1 >= 2) for i in range(len(x))]
    return c
    #return [int(x[i] + r[i] + g1 >= 2) for i in range(len(x))]

def receiver1(x, r):
    if 1 in x:
        return int(1 not in r)
    else:
        return 0


def receiver2(x):
    return int(1 in x)


def compare(x, c):
    x_1 = c_1 = 0
    for i in range(len(x)):
        x_1 += int(x[i] == 1)
        c_1 += int(c[i] == 1)
    return c_1 / x_1


def find_one(r):
    for i in range(len(r)):
        if r[i] == 1:
            return i


def sum_of_elem(a):
    # Считаем сумму c
    total = 0
    for k in range(len(c)):
        total += a[k]
    return total


def learn(c, j):
    # Считаем сумму элементов c
    total_c = sum_of_elem(c)

    global b
    # Считаем веса b
    b[j] = [round((2 * c[i]) / (1 + total_c), 4) for i in range(len(b[j]))]

    global t
    # Считаем веса t
    t[j] = [c[q] for q in range(len(t[j]))]
    return None


def find_similarity():
    # Слой распознавания

    global c
    # Свертка векторов
    net = [utils.convolution(c, b[i]) for i in range(10)]

    # Блокируем нейрон
    global inhibited
    net = utils.multiply_vectors(net, inhibited)

    print("Реакция нейронов")

    # Активируем максимальный нейрон
    out = utils.activation(net)

    print("Выход нейронов")
    print("out", out)

    global r
    r = out

    # Находим победителя
    win = find_one(r)

    print("win №", win)

    # Веерный выход
    p = t[win]
    print("Сигнал обратной связи")
    print("p", p)
    filerw.write_array_to_file_in_one_line([p], "p.txt")

    # Переключаем приемник
    g1 = receiver1(x, p)
    print("Приемник 1", g1)

    print("Подаем вектор x для сравнения")
    print("x", x)

    c = comparison(x, p, g1)

    global similar
    similar = compare(x, c)
    print("схож", similar)

    print("c после поиска", c)
    return win


# Схожесть
h = 0.95

# Инициализация
print("====Первый этап====")

# входной образ

#x = filerw.read_file_to_one_dimensional_array_of_ints("c.txt")  # 64

# Ввод целевого числа
target_image = str(input("Введите целевой образ: "))
# Из введенного числа создается имя файла для входных данных

# Считываем входные данные

x = []

mode = input("Введите формат файла - txt или png ")
while mode is not True:
    # Путь до директории со скриптом
    main = os.path.dirname(__file__)
    file_name = str(target_image) + "." + mode
    # Формируем путь до файла
    file_path = os.path.join(main, "templates", file_name)
    # Первый вариант: считывание из текстового файла
    if mode == "txt":
        x = filerw.read_file_to_one_dimensional_array_of_ints(file_path)
        mode = True
    # Второй вариант: считывание из изображения
    elif mode == "png":
        x = imagerw.convert_image_into_array(file_path)
        mode = True
    else:
        mode = input("Неподходящий формат!\nВведите формат файла - txt или png ")

# сигнал обратной связи
# изначально все нули
p = filerw.read_file_to_one_dimensional_array_of_ints("p.txt")

# Приемник 1
# изначально единица
g1 = receiver1(x, p)

# веса нейронов слоя распознования
b = filerw.read_file_to_two_dimensional_array_of_floats("b.txt")
# сохраненные образы
t = filerw.read_file_to_two_dimensional_array_of_ints("t.txt")

# Сравнение
print("Подаем вектор x")
print("x", x)
print("Сигнал обратной связи")
print("p", p)
print("Приемник 1")
print("g", g1)

c = comparison(x, p, g1)

print("Выход после слоя сравнения")
print("c", c)

print("====Второй этап====")

inhibited = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

win = find_similarity()

print("====Третий этап====")

similar = compare(x, c)

while similar < h and utils.sum_array(inhibited):
    print("Схожесть не достигнута", similar, "<", h)
    print("Заблокированы: ", inhibited)
    print("====Поиск оптим====")
    print("Тормозим нейрон №", win)
    inhibited = utils.inhibit(win, inhibited)
    win = find_similarity()

print("Схожесть достигнута", similar, ">=", h)
print("c для обуч", c)
learn(c, win)
print("Образ", target_image, "запоминает", win, "нейрон")

filerw.write_array_to_file_in_one_line([p], "p.txt")
filerw.write_array_to_file_in_many_lines(b, "b.txt")
filerw.write_array_to_file_in_many_lines(t, "t.txt")

# Обновляем изображения в папке neurons
mem.refresh_image_memory()
