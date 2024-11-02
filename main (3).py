'''Формируется матрица F следующим образом: Скопировать в нее матрицу А и если А
симметрична относительно главной диагонали, то поменять симметрично области 1 и 3
местами, иначе 1 и 2 поменять местами несимметрично. При этом матрица А не меняется.
После чего вычисляется выражение: К * (F+A) * AT – AT + F. Выводятся по мере
формирования А, F и все матричные операции последовательно.'''
import random
a = []
print("введите n от 3 до 100")
n = int(input())
print("введите число к -... to 100")
k = int(input())
print("введите число 1 или 2 ")
print("1.Заполнение из файла")
print("2.Рандомное заполнение")
choice = int(input())

# инициализация матрицы а
if choice==1:
    file = open('file.txt', 'r')
    for i in range(n):
        st = file.readline()
        a.append([int(x) for x in st.split()])

    print("A")
    for i in a:
        print(i)

elif choice==2:
    a=[[random.randint(-10,10) for _ in range(n)] for _ in range(n)]
    print("A")
    for i in a:
        print(i)
else:
    print("некоректный ввод")

print("F")
f = [[0]*n for _ in range(n)] #создание и заполнение 0 матрицы f
for i in f:
    print(i)

for i in range(n):      #копирую a в f
    for j in range(n):
        f[i][j] = a[i][j]
print("F")
for i in f:
    print(i)

d = []
l = []

for i in range(n):
    for j in range(i):
        d.append(f[i][j])
print(d)

for i in range(n):
    for j in range(i+1,n):
        l.append(f[i][j])
print(l)

count=len(d)
point=0
for i in range(count): #симметрична относительно главной диагонали
    if d[i]==l[i]:
        point+=1
    else:
        break

first_area=[]
third_area=[]
second_area=[]
iterator_s=0
iterator_f=0
iterator_t=0
if point != count:
    for i in range(n):  #первая область
        for j in range(i):
            if i > j and i + j < n - 1:
                first_area.append(f[i][j])
    print(first_area)

    for i in range(n):   #3 область
        for j in range(i, n):
            if i < j and i+j > n-1:
                third_area.append(f[i][j])

    print(third_area)
#меняем местами области
    for i in range(n):  #первая область
        for j in range(i):
            if i > j and i + j < n - 1:
                f[i][j] = third_area[iterator_t]
                iterator_t += 1

    for i in range(n):  # 3 область
        for j in range(i, n):
            if i < j and i + j > n - 1:
                f[i][j] = first_area[iterator_f]
                iterator_f += 1

else:
    for i in range(n):  #первая область
        for j in range(i):
            if i > j and i + j < n - 1:
                first_area.append(f[i][j])

    for i in range(n):  #вторая область
        for j in range(i, n):
            if i < j and i+j < n - 1:
                second_area.append(f[i][j])

    print(first_area)
    print(second_area)
#меняем местами области
    for i in range(n):  #первая область
        for j in range(i):
            if i > j and i + j < n - 1:
                 f[i][j]=second_area[iterator_s]
                 iterator_s+=1

    for i in range(n):  #вторая область
        for j in range(i, n):
            if i < j and i + j < n - 1:
                f[i][j] = first_area[iterator_f]
                iterator_f += 1

for i in f:
    print(i)


# К * (F+A)
ex_k_f_a=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        ex_k_f_a[i][j] = f[i][j]+a[i][j]
ex_k_f_a *= k
print("ex_k_f_A")
for i in ex_k_f_a:
    print(i)

#AT
at = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        at[i][j]=a[j][i]
print("at")
for i in at:
    print(i)

#ex_k_f_A * AT

ex_at= [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        s=0
        for p in range(n):
            s += ex_k_f_a[i][p]*at[p][j]
        ex_at[i][j] = s
print("ex_at")
for i in ex_at:
    print(i)

#at + f
at_f=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        at_f[i][j] = at[i][j]+f[i][j]
print("at_f")
for i in at_f:
    print(i)

#ex_at - at_f
ex_at_at_f=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        ex_at_at_f[i][j] = ex_at[i][j]+at_f[i][j]
print("ex_at_at_f")
for i in ex_at_at_f:
    print(i)