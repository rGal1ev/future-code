first = """
# 1
a = int(input("Введите длину ребра a: "))
b = int(input("Введите длину ребра b: "))
c = int(input("Введите длину ребра c: "))

V = a * b * c
S = 2 * (a * b + b * c + a * c)

print("Объем параллелепипеда:", V)
print("Площадь поверхности параллелепипеда:", S)
"""

second = """
# 2
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))

average = (a + b) / 2

print("Среднее арифметическое чисел равно", average)
"""

third = """
# 3
a = 5
b = 10
result = a * b

print('Произведение равно:', result)
"""

fourth = """
# 4
r = float(input("Введите радиус: "))
L = 2 * 3.14 * r
print("Длина окружности равна", L)
"""

fifth = """
# 5
a = float(input("Введите длину ребра: "))
s1 = a * a
s2 = 6 * a * a
v = a ** 3

print("Площадь грани: ", s1)
print("Площадь полной поверхности: ", s2)
print("Объем куба: ", v)
"""

sixth = """
# 6
n = int(input("Введите количество порций мороженного: "))
k = int(input("Введите количество плиток шоколада: "))

price_ice_cream = 1200
price_chocolate = 3800

total_spent = n * price_ice_cream + k * price_chocolate
print("Мальчик потратил:", total_spent, "руб.")
"""

seventh = """
# 7
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

h = (c ** 2 - ((a - b) / 2) ** 2) ** 0.5
S = (a + b) * h / 2

print("Площадь трапеции:", S)
"""

eighth = """
# 8
speed_motorcycle = 60
speed_bicycle = 15
time = 2

distance = (speed_motorcycle + speed_bicycle) * time
print("Расстояние от города до поселка:", distance, "км")
"""

ninth = """
# 9
money_per_week = 900 / (2 + 4)  # Расчет зарплаты за одну неделю
money1 = money_per_week * 2  # Расчет заработка первого рабочего
money2 = money_per_week * 4  # Расчет заработка второго рабочего

print("Первый рабочий заработал", money1, "рублей")
print("Второй рабочий заработал", money2, "рублей")
"""

work = {
    "id": 2,
    "name": "2️⃣ Самостоятельная работа",
    "task_count": 5,
    "tasks": [first, second, third, fourth, fifth]
}
