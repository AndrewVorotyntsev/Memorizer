import random


def zeros(a):
    c = []
    for i in range(a):
        c.append(0)
    return c


def ones(a, b):
    c = []
    for i in range(a):
        c.append([])
        for j in range(b):
            c[i].append(1)
    return c


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


def receiver1(x, r):
    for i in range(len(x)):
        if x[i] == 1:
            for j in range(len(r)):
                if r[j] == 1:
                    return 0
            return 1
    return 0


def receiver2(x):
    for i in range(len(x)):
        if x[i] == 1:
            return 1
    return 0


def reset(x, c, h):
    x_1 = 0
    c_1 = 0
    for i in range(len(x)):
        if x[i] == 1:
            x_1 += 1
    for j in range(len(c)):
        if c[i] == 1:
            c_1 += 1
    if (c_1 / x_1) > h:
        return 1
    return 0


def convolution(a, b):
    c = 0
    for i in range(len(a)):
        c += a[i] * b[i]
    return c


def activation(n):
    m = []
    max = 0
    for i in range(len(n)):
        if n[i] > n[max]:
            max = i
    for j in range(len(n)):
        if j == max:
            m.append(1)
        else:
            m.append(0)
    return m


def find_one(r):
    for i in range(len(r)):
        if r[i] == 1:
            return i


def learn(c, j, b, t):
    # Считаем сумму c
    total_c = 0
    for k in range(len(c)):
        total_c += c[k]
    # Считаем веса b
    for i in range(len(b[j])):
        b[j].append((2*c[i])/(1+ total_c))


def multiply_vectors(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return c


def inhibit(n, m):
    for i in range(len(m)):
        if i == n:
            m[i] = 0
    return m

def sum_array(m):
    s = 0
    for i in m:
        s += i
    if s > 1:
        return True
    else:
        return False


