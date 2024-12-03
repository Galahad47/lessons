import numpy as np
import string
import random
import num2words as n2w
# 1
def task1():
    dedus = "viktor Dzoi jhiv !"
    l = ""
    for i in reversed(dedus):
        l = l + i
    print(l)

# 2
def task2():
    num = []
    for i in range(0,10):
        n = 2 ** i
        num.append(n)
    n1 = np.min(num)
    n2 = np.max(num)
    n3 = np.sum(num[n1:n2]) 
    print(n1,n2,n3)

# 3    
def task3():
    num1 = [] # +++
    num2 = [] # ---
    for i in range(-10,10):
        n = np.exp(np.pi/2 + i)
        if n > 0:
            num1.append(n) # Отбираю все минимальные цифры и максимальные
        else:
            num2.append(n)
        
    lzi = num2.index(0)
    pos = num1[lzi + 1:]
    avg = sum(pos) / len(pos)
    print(avg)
        
#4     
def task4(sequence):
    f0 = -1
    s0 = -1

    for i, value in enumerate(sequence):
        if value == 0:
            if f0 == -1:
                f0 = i
            elif s0 == -1:
                s0 = i
                break

    if f0 == -1 or s0 == -1:
        return 0

    # Подсчитаем количество отрицательных элементов между ними
    c = sum(1 for x in sequence[f0 + 1:s0] if x < 0)
    return c

#5
def task5(sequence):

    max_value = np.max(sequence)
    max_index = sequence.index(max_value)
    new_sequence = []
    
    for i in range(len(sequence)):
        if i <= max_index:
            new_sequence.append(sequence[i])
        elif sequence[i] != 0:
            new_sequence.append(sequence[i])
    
    return new_sequence


#6
def task6(matrix):
    if not matrix or not matrix[0]:
        return matrix

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Список для хранения количества четных элементов в каждом столбце
    even_counts = [0] * num_cols

    # Подсчет четных элементов в каждом столбце
    for j in range(num_cols):
        for i in range(num_rows):
            if matrix[i][j] % 2 == 0:
                even_counts[j] += 1

    min_index = even_counts.index(min(even_counts))
    max_index = even_counts.index(max(even_counts))

    for i in range(num_rows):
        matrix[i][min_index], matrix[i][max_index] = matrix[i][max_index], matrix[i][min_index]

    return matrix

def task7(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return matrix

    n = len(matrix)
    # Список для хранения минимальных элементов в каждом столбцеX
    column_mins = [float('inf')] * n

    # Находим минимальные элементы в каждом столбце
    for j in range(n):
        for i in range(n):
            if matrix[i][j] < column_mins[j]:
                column_mins[j] = matrix[i][j]

    # Увеличиваем элементы на диагонали(просто добавляем колонку)
    for i in range(n):
        matrix[i][i] += column_mins[i]

    return matrix

def task8(matrix):
    pos_columns = []
    new_matrix = []
    if not matrix or not matrix[0]:  # Проверка на пустую матрицу
        return matrix

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    

    # Проверяем каждый столбец
    for j in range(num_cols):
        all_non_positive = True  # Пусть все значения положительны
        for i in range(num_rows):
            if matrix[i][j] > 0:  # Если найден положительный элемент
                all_non_positive = False
                break
        if not all_non_positive:
            pos_columns.append(j)
    
    for i in range(num_rows):
        new_row = [matrix[i][j] for j in pos_columns]
        new_matrix.append(new_row)

    return new_matrix



def task9(thing):
    result = []
    fractional_elements = [x for x in thing if isinstance(x, float)]
    largest_fractions = sorted(fractional_elements, reverse=True)[:3]

    for x in thing:
        result.append(x)
        # Если текущий элемент - один из трех наибольших дробных, то добавляем
        if x in largest_fractions:
            half_sum = x / 2
            result.append(half_sum)

    return result


#task 10
def task10(thing):
    data = []; main = []
    for i in range(len(thing)):
        data.append(thing[i])
        for j in thing:
            main = data[j],data[j-1]
    print(main)


def task11(data):
    d = []; a = []; t = []
    for i in data:
        d.append(i)
        a.append(len(i))
    t.append(np.min(a))
    return t



def task12(data):
    text = []
    for i in data:
        text.append(list(map(list,i)))
    text = [item for sublist in text for item in sublist]
    text = ''.join(text)
    text_no_point = text.translate(str.maketrans('', '', string.punctuation))

    return text_no_point


def task13(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as fo:
        lines1 = set(line.strip() for line in f1)
        lines2 = set(line.strip() for line in f2)
        unique_lines = lines1 - lines2
        for line in unique_lines:
            fo.write(line + '\n')



def task14(data):
    lat_let = list(string.ascii_lowercase)
    data = data.lower()
    letter = sorted(set(filter(lambda x: x in lat_let, text)))
    return letter
# Приедешь я спрошу потому что по идее так он будет выдавать всё кроме латинских букв



#data1 - это массив который уже отсортирован а data2 - это искомая величина
def task15(data1,data2 ): 
    min = 0
    max = len(data1) - 1
    while min <= max:
        med = (min + max) / 2
        if data1[med] == data2:
            return med + 1
        elif data1[med < data2]:
            min = med + 1 #сдвиг влево
        else:
            max = med - 1 # вправо

#Тут я не понял, а если не найти значение?

def task16(matrix):
    resmatrix = []
    for i in matrix:
        a = 0 #нули
        b = 0 # <0
        for el in i:
            if el == 0:
                a = a + 1
            elif el < 0:
                b = b + 1
        if a <= b:
            resmatrix.append(i)
    print(resmatrix)


def task17(data):
    res = []
    def a(num):
        if num <=1:
            return False
        elif num <= 3:
            return True
        else:
            for i in range(1,num):
                if num % i == 0:
                    return False
            return True
    
    for i in range(len(data)):
        if not a(data[i]):
            res.append(data[i])
        print(res)
##########################################################################
# Вот тут прикольно, я тут прям из книги часть скрипта копипастил, там есть после объяснения кортежей есть создание словаря, тут он пригодится чтобы хранить слова из текста
# Я решил не удалять мои попытки они смешные довольно)
# def task18(data):
#     alpth = {}
#     res = ""
#     for i in range(len(data)):
#         if data[i] in alpth:
#             alpth[data[i]].append(i)
#         else:
#             alpth[data[i]] = [i]
    
#     for j in alpth.keys():
#         pos = alpth[j]
#         random.shuffle(pos)
#         res = res + (j * len(pos) + ''.join([j for _ in pos]))
    print(res)

    # def start():
    #     data = []
    #     for i in list(open("text.txt","r")):
    #         data.append(i)
    #     return data


# data = "Data Scientist"
# # data = data + str(open("text.txt"))
# print(task18(data))
# print(data)
#########################################################################

def task18_1(data):
    dat = ""
    resultWord = ""
    alphavet = {}
    res = ""
    for i in data:
        a = dat.join(i)
        d = a.split()
        for j in d:
            if len(j) > 3:
                m = len(j) // 2
                pos = alphavet[j]
                random.shuffle(pos)
                resultWord += j[:1] + j[-1] + ''.join([j[i] for i in pos[:m]])
                alphavet[j] = pos
            else:
                res += j + " "
    return res


# data = open("text.txt","r")
# task18_1(data)


def task19(num):
    for i in num:
        text = n2w.num2words(i)
        if i > 999999:
            print("Не знаю, помню только до миллиона")
        else:
            print(text)

number = input("Введите через пробел числа: ").split()
number = [int(value) for value in number]
print(number,"\n",task19(number))
