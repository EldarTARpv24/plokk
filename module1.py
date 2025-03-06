# ÜL 1

# это вертикальные домики
# numb = int(input("Сколько сделать домиков?"))

# for kolichestvo in range(0, numb):
#     print("   ~~~~~")
#     print("  /_____\\")
#     print("  | []  |")
#     print("  -------")
#     print()

# это массовая застройка

# numb = int(input("Сколько сделать домиков?"))

# for kolichestvo in range(0, numb):
#     print("   ~~~~~ " * numb)
#     print("  /_____\\" * numb)
#     print("  | []  |" * numb)
#     print("  -------" * numb)

#ÜL 2

# n = int(input("Введите количество учащихся в 2 классах: "))
# random_num = 0
# import random
# summ = 0
# number_of_grades = 0
# for numb in range(n * 2):
#     random_num = random.randint(1, 5)
#     print(random_num)
#     number_of_grades += 1
#     summ += random_num
# mid_grade = summ / number_of_grades
# round(mid_grade, 1)
# print("Средний балл равен:", mid_grade)

#ÜL 3

# import random

# num_õpilased = random.randint(10,35 )
# min_hinne = 6
# max_hinne = 0

# for i in range(num_õpilased):
#     hinne = random.randint(1, 5)  
#     print(f"Оценка ученика: {hinne}")

#     if hinne > max_hinne:
#         max_hinne = hinne
#     if hinne < min_hinne:
#         min_hinne = hinne

# print(f"Минимальная оценка: {min_hinne}")
# print(f"Максимальная оценка: {max_hinne}")

#ÜL 4

# civil_summ = 0
# kilo_summ = 0

# import random
# for numb in range(12):
#     civil = random.randint(1000, 10000)
#     civil_summ += civil
#     killometr = random.randint(10, 100)
#     kilo_summ += killometr
# press = civil_summ / kilo_summ
# round(press, 1)
# print("Плотность равна: ",press)

#ÜL 5

minim = int(input("Введите минимум: "))
maxim = int(input("Введите максимум: "))
step = float(input("Введите шаг: "))

while minim < maxim:
    try:
        print(minim)
        minim += step
        y = -0.5 * minim + minim
        yy = -0.5 * maxim + maxim
        print(y, "значение")
        print(maxim)
        print(yy, "значение")
        if minim > maxim:
            break
    except ValueError:
        print("error")

