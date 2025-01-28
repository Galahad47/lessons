import numpy as np
import string
import random
import num2words as n2w
# 1
def task1():
    dedus = "viktor Tsoi jhiv !"
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


#step - шаг через какое число ты хочешь узнать получумму
#Task 9
def task9(numbers,step):
    a = [];b=[]; l = []
    for i in numbers:
        if (i % 1) > 0:
            a.append(i)
    d = sorted(a)
    for j in d:
        b.append(j)
    
    for i in range(0, len(b), step):
        s = sum(b[i:i+3]) / 2
        l.append(s)
        b.extend(l)
    
    print(b)
    


# Task 10
def task10(thing):
    val = 0
    main = []; d1=[];d2=[]
    for i in thing:
        if i !=" ":
            main.append(i)
    for j in range(len(main)//2): 
        if main[j] != main[-j-1]:
            val += 1        
    print(val)

# Task 11
def task11(data):
    t = data.split()
    min_word = min(t,key=len)
    t.remove(min_word)
    return " ".join(t)

# Task 12
def task12(data):
    d = []
    for i in range(len(data)):
        print(i)
        if data[i] != ' ':
            if data[i] !='.':
                if data[i] != ',':
                    d.append(data[i])
    print(d)

# Task 13
# def task13(file1, file2, output_file):
#     with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as fo:
#         lines1 = set(line.strip() for line in f1)
#         lines2 = set(line.strip() for line in f2)
#         unique_lines = lines1 - lines2
#         for line in unique_lines:
#             fo.write(line + '\n')
def task13(file1, file2, output_file):
    punctuations = [',' '.' ' ']
    t1 = open(file1,'r'); t2 = open(file2); t3 = open(output_file,'w')
    data1=[];data2=[];data3=[]
    for i in t1:
        for j in t2:
            data1.append(i)
            data2.append(j)
    
    
    
    
        
        
        

p1='/home/andrew/Documents/fortask13/text.txt'
p2='/home/andrew/Documents/fortask13/text1.txt'
p3='/home/andrew/Documents/fortask13/result.txt'

task13(p1,p2,p3)
        





# Task 14
def task14(text):
    lat_let = set(string.ascii_lowercase)
    text = text.lower()
    letter = sorted(set(filter(lambda x: x in lat_let, text)))
    return letter

# Task 15
def task15(data1, data2):
    min_index = 0
    max_index = len(data1) - 1
    while min_index <= max_index:
        med_index = (min_index + max_index) // 2  # Используем целочисленное деление
        if data1[med_index] == data2:
            return med_index
        elif data1[med_index] < data2:
            min_index = med_index + 1
        else:
            max_index = med_index - 1
    return -1  # Возвращаем -1, если значение не найдено

# Task 16
def task16(matrix):
    resmatrix = []
    for row in matrix:
        count_zeros = row.count(0)
        count_negatives = sum(1 for el in row if el < 0)
        if count_zeros <= count_negatives:
            resmatrix.append(row)
    print(resmatrix)

# Task 17
def task17(data):
    res = []
    def is_prime(num):
        if num <= 1:
            return 0
        for i in range(2, int(num**0.5) + 1):  # Проверка делимости до корня из num
            if num % i == 0:
                return 0
        return True
    
    for number in data:
        if not is_prime(number):
            res.append(number)
    print(res)
    

def task18(data):
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



# def task20():


def task21(str1, str2):
    n, m = len(str1), len(str2)
    if n > m:
        str1, str2 = str2, str1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str1[j - 1] != str2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


