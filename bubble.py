from random import randint
a = []
num = 20
for i in range(num):
    a.append(randint(1,99))
print(a)
for i in range(num - 1):
    for j in range(num - 1 - i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1],a[j]
            min = a[0]
            max = a[-1]
print(a,"\n",min,"\n",max)


 