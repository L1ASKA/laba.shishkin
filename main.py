#Вещественные числа, заключенные в кавычки (все виды). Кавычки не выводятся. Целая часть числа
#выводится словами.

with open('laba3.txt', 'r') as file:
    char = file.read()
    numbers = char.split()
for number in numbers:
    if (number.startswith('"') and number.endswith('"')) or (number.startswith("'") and number.endswith("'")):
        value = number[1:-1]  # Удаляем кавычки
        try:
            # Проверка, является ли значение вещественным числом
            d={
                0: "Ноль",
                1:"0дин",
                2: "Два",
                3: "Три",
                4: "Четыре",
                5: "Пять",
                6: "Шесть",
                7: "Семь",
                8: "Восемь",
                9: "Девять",
            }

            float_value = float(value)
            int_part = int(float_value)
            des_part = str(abs(float_value-int_part)).split(".")[1]
            list_1 = []
            list_2 = []
            for i in str(int_part):
                if i=="-":
                    list_2.append(i)
                else:
                    list_1.append(d.get(int(i)))

            result_1=' '.join(list_1)
            result_2=' '.join(list_2)

            print(f"Это вещественное число: {result_2}{result_1}.{des_part}")
        except ValueError:
            print("Это не вещественное число:", value)
    else:
        print("Значение не находится в кавычках:", number)



