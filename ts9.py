#Task 9
def sorting(data):
    for i in range(1, len(data)):
        d = data[i]
        j = i -1
        while j >= 0 and data[j] > d:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = d
    return data

    
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
                
# убедиться на нескольких массивах что всё работает

d = [10.3,22.3,1.2,3.4,5.454,2,3,4,5];
e = task9(d)
print(e)

