import matplotlib.pyplot as plt
import numpy as np
a = []

print("введите n от 2 до 100")
n = int(input())
print("введите число k ")
k = int(input())
print("введите от  1 до 3")
print("1. Заполнение из файла")
print("2. Рандомное заполнение")
print("3. Генератор")
choice = int(input())

# инициализация матрицы а
if choice==1:
    file = open('laba2.txt', 'r')
    for i in range(n):
        st = file.readline()
        a.append([int(x) for x in st.split()])

    print("A")
    for i in a:
        print(i)

elif choice==2:
    a = np.random.randint(-10, 10, size=(n,n))
    print("A")
    for i in a:
        print(" ".join(f"{value:3d}" for value in i))
elif choice==3:
    a=[[0] * n for _ in range(n)]
    if n % 2 == 0: #Чётная матрица
        for i in range(n):
            for j in range(n):
                if n/2>i and n/2>j: #B
                    a[i][j]=1
                elif n/2 <= i and n /2 > j: #C
                    a[i][j]=2
                elif n/ 2 > i and n/2 <= j: #E
                    a[i][j] = 3
                elif n/ 2 <= i and n/2 <= j: #D
                    a[i][j] = 4
    else: #неЧётная матрица
        for i in range(n):
            for j in range(n):
                if i==(n-1)/2 or j==(n-1)/2:
                    continue
                elif n/2>i and n/2>j: #B
                    a[i][j]=1
                elif n/2<=i and n/2>j: #C
                    a[i][j]=2
                elif n/2 <= j: #E
                    a[i][j] = 3
                elif n/ 2 <= i and n/2 <= j: #D
                    a[i][j] = 4

    print("A")
    for i in a:
        print(i)
else:
    print("неверный ввод")

f = np.copy(a)
print("F")
for i in f:
    print(i)

count0 =0
for i in range(int(n/2)): #количество нулевых элементов в нечётных столбцах
    for j in range(int((n+1)/2),n):
        if j % 2 !=0:
            if a[i][j]==0:
                count0+=1
            else:
                continue
        else:
            continue

print(count0)

count1=0
for i in range(int(n/2)): # отрицательные элементы в чётных строках
    for j in range(int((n+1)/2),n):
        if i % 2 ==0:
            if a[i][j]<0:
                count1+=1
            else:
                continue
        else:
            continue

print(count1)

array_E=[]
array_B=[]
array_C=[]
iterator_B=0
iterator_E=0
iterator_C=0




if count0>count1: #меняем в и с симметрично
    for i in range(int(n / 2)):  # B
        for j in range(int(n / 2)):
            array_B.append(f[i][j])
    print("B")
    print(array_B)

    for i in range(int(n / 2),n): #C
        for j in range(int(n / 2)):
            array_C.append(f[i][j])
    print("C")
    print(array_C)
    # меняем местами
    for i in range(int(n / 2),n): #C
        for j in range(int(n / 2)):
            f[i][j]=array_B[iterator_B]
            iterator_B+=1

    for i in range(int(n / 2)):  # B
        for j in range(int(n / 2)):
            f[i][j] = array_C[iterator_C]
            iterator_C += 1
    print("F")
    for i in f:
        print(i)

else:
    for i in range(int((n/ 2)-1),-1,-1):  # E
        for j in range(n-1,int((n-1)/ 2),-1):
            array_E.append(f[i][j])
    print("E")
    print(array_E)

    for i in range(int((n/ 2)-1),-1,-1):  # B
        for j in range(int((n / 2)-1),-1,-1):
            print(j)
            array_B.append(f[i][j])
    print("B")
    print(array_B)
#меняем местами
    for i in range(int(n / 2)):  # B
        for j in range(int(n / 2)):
            f[i][j]=array_E[iterator_E]
            iterator_E+=1
    for i in range(int(n / 2)):  # E
        for j in range(int((n + 1) / 2), n):
            f[i][j] = array_B[iterator_B]
            iterator_B += 1

    print("F")
    for i in f:
        print(i)
amount_diagonal_values_F=0
for i in range(n):  # определяем сумму диагональных элементов матрицы F
    for j in range(n):
        if i == j or i + j == n - 1:
            amount_diagonal_values_F += f[i][j]

print(f"amount_diagonal_values_F = {amount_diagonal_values_F}")

def_matrix_a = int(np.linalg.det(a))  # определяем определитель матрицы А

print(f"def_matrix_a = {def_matrix_a}")

# 1
transposition_A = [[0] * n for _ in range(n)]  # транспонируем матрицу А
for i in range(n):  # at
    for j in range(n):
        transposition_A[i][j] = a[j][i]
#print("transposition_A")
#for i in transposition_A:
    #print(i)

if def_matrix_a<amount_diagonal_values_F:
    # 2
    power_A = np.linalg.matrix_power(a, -1)  # матрица А в -1 степени(А**-1)
    # print("А**-1")
    # for i in power_A:
    # print(i)

    # 3
    mult_powerA_At = [[0] * n for _ in range(n)]
    for i in range(n):  # А**-1 * A**t
        for j in range(n):
            sum_mult_powerA_At = 0
            for p in range(n):
                sum_mult_powerA_At += power_A[i][p] * transposition_A[p][j]
            mult_powerA_At[i][j] = sum_mult_powerA_At
    #print("multiplication_powerA_At")
    #for i in mult_powerA_At:
        #print(i)

    #4
    for i in range(n):  # k*F
        for j in range(n):
            f[i][j] *= k



    result= [[0] * n for _ in range(n)]
    #5
    for i in range(n):  # mult_powerA_At - f
        for j in range(n):
            result[i][j]=mult_powerA_At[i][j] - f[i][j]

    print("Result")
    for i in result:
        print(i)

else:
    #2
    # нижняя треугольная матрица G
    G = np.tril(a)
    #print("G")
    #for i in G:
         #print(i)

    # 3
    power_F = np.linalg.matrix_power(f, -1)  # матрица F в -1 степени(А**-1)
    #print("F**-1")
    #for i in power_F:
       #print(i)

    #4 At+G
    At_G=[[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            At_G[i][j]=transposition_A[i][j]+G[i][j]
    #print("At_G")
    #for i in At_G:
        #print(i)

    #5 At_G - F**(-1)
    At_G_F = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            At_G_F[i][j] = At_G[i][j] - power_F[i][j]
    # print("At_G_F")
    # for i in At_G_F:
    # print(i)

    #6At_G_F*K
    for i in range(n):
        for j in range(n):
            At_G_F[i][j] *= k

    result=np.copy(At_G_F)
    print("result")
    print(result)

# Первый график - простое изображение матрицы (heatmap)
plt.subplot(1, 3, 1)
plt.imshow(f, cmap='viridis')
plt.colorbar()
plt.title('Heatmap')

# Второй график - линиями (line plot)
plt.figure()
plt.subplot(1, 3, 2)
for i in range(n):
    plt.plot(f[i,:])
plt.title('Line Plot')

# Третий график - гистограмма значений матрицы
plt.subplot(1, 3, 3)
plt.hist(f.flatten(), bins=3)
plt.title('Histogram')

# Настройка отображения графиков
plt.tight_layout()
plt.show()
