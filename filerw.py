# Функции для работы с файлами


def read_file_to_one_dimensional_array_of_ints(file_name):
    array_to_write = []
    with open(file_name) as f:
        for line in f:
            for x in line.split():
                array_to_write.append(int(x))
    return array_to_write


def read_file_to_two_dimensional_array_of_ints(file_name):
    array_to_write = []
    with open(file_name) as f:
        for line in f:
            array_to_write.append([int(x) for x in line.split()])
    return array_to_write


def read_file_to_two_dimensional_array_of_floats(file_name):
    array_to_write = []
    with open(file_name) as f:
        for line in f:
            array_to_write.append([float(x) for x in line.split()])
    return array_to_write


def write_array_to_file_in_one_line(array_to_read, file_name):
    file_name = open(file_name, "w")
    one_line = ""
    for i in range(len(array_to_read)):
        for j in range(len(array_to_read[i])):
            one_line = one_line + str(array_to_read[i][j]) + " "
        file_name.write(one_line)


def write_array_to_file_in_many_lines(array_to_read, file_name):
    file_to_write = open(file_name, "w")
    for i in range(len(array_to_read)):
        # Для загрузки в несколько строк объявляем переменную строки после запуска цикла
        line = ""
        for j in range(len(array_to_read[i])):
            line = line + str(array_to_read[i][j]) + " "
        line = line.strip(" ") + "\n"
        file_to_write.write(line)


