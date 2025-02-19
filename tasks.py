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
def task9(numbers):
    a = [];b=[];c=[];d=[]
    for i in numbers:
        a.append(i)
        if (i % 1) > 0:
            b.append(i)
            b = sorting(b)
    psum = sum(b[-3:])/2
    for i,datai in enumerate(a):
        for j,dataj in enumerate(b[-3:]):
            if datai == dataj:
                c.append(i)
    for i,dat in enumerate(a):
        d.append(dat)
        if i in c:
            d.append(psum)
    return d

    


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
def task13(p1,p2):
    with open(p1, "r",encoding="utf-8") as t1, open(p2, "r",encoding="utf-8") as t2:
        text1 = t1.read().split(".");text2 = t2.read().split(".");text3 = []
        if text1 != text2:
            text3.append(text1)
        return text3
         
# p1 = "D:/work/aari/text.txt";p2 = "D:/work/aari/text1.txt"
# d = task13(p1,p2)
# print(d)

# Task 14
def task14(p1):
    with open(p1, "r", encoding="utf-8") as t1:
        text1 = t1.read()
        x = 0
        latin_letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in text1:
            for j in range(0,len(latin_letter)):
                if i in latin_letter[j]:
                    x += 1
        return x

# p1 = "D:/work/aari/text.txt"
# d = task14(p1)
# print(d)

# Task 15
def task15(x,b):
    d = []
    n = len(x)
    for i in range(n):
        swapped = False 
        for j in range(0, n - i - 1): 
            if x[j] < x[j + 1]: 
                x[j], x[j + 1] = x[j + 1], x[j]  
            swapped = True
        if not swapped:
            break
    d.append(x)
    print(d)
    ind0 = 0;indlas = len(x) - 1
    while ind0 <= indlas:
        indmed = (ind0 + indlas) // 2
        if x[indmed] == b:
            return indmed
        elif b > x[indmed]:
            indlas = indmed - 1
        else:
            ind0 = indmed + 1
    return "нет значений"

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






def task21(s1, s2):
    t1 = len(s1);t2 = len(s2)
    if t1 < t2:
        return task21(s2, s1)
    if t2 == 0:
        return t1
    x = range(t2 + 1)
    for i, c1 in enumerate(s1):
        y = [i + 1]
        for j, c2 in enumerate(s2):
            a = x[j + 1] + 1 
            b = y[j] + 1       
            c = x[j] + (c1 != c2)
            y.append(min(a, b, c))
        x = y
    return x[-1]
s1 = "kitten"
s2 = "sitting"
result = task21(s1, s2)