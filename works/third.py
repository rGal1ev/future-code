first = """
# 1
num = int(input("Введите число: "))

if num >= 0:
    result = num - 10
else:
    result = num + 10

print("Результат:", result)
"""

second = """
# 2
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
product = num1 * num2

if product < 0:
    product *= -2
    print("Произведение отрицательно, умножаем на -2:", product)
else:
    product *= 3
    print("Произведение положительно, увеличиваем в 3 раза:", product)
"""

third = """
# 3
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if (num1 + num2) % 2 == 0:
    result = num1 * num2
    print("Произведение чисел:", result)
else:
    result = num1 / num2
    print("Частное чисел:", result)
"""

fourth = """
# 4
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if num1 > num2:
  difference = num1 - num2
else:
  difference = num2 - num1

print("Результат:", difference)
"""

fifth = """
# 5
number = int(input("Введите число: "))

if number > 10:
    result = number / 2
else:
    result = number * 5

print("Результат:", result)
"""

sixth = """
# 6
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

summa = num1 + num2

if summa > 100:
    summa = summa / 2
else:
    summa = summa * 2

print("Результат: ", summa)
"""

seventh = """
# 7
number = int(input("Введите двухзначное число: "))

digit1 = number // 10
digit2 = number % 10

sum_of_digits = digit1 + digit2

if sum_of_digits % 2 == 0:
    result = number + 2
else:
    result = number - 2

print("Результат:", result)
"""

eighth = """
# 8
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник может существовать")
else:
    print("Треугольник не может существовать")
"""

ninth = """
# 9
number = int(input("Введите целое число: "))

if number > 0:
    result = number + 20
else:
    result = number - 5

print("Полученное число:", result)
"""

tenth = """
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

sum = num1 + num2

if sum % 5 == 0:
    result = sum + 1
else:
    result = sum - 2

print("Результат:", result)
"""

work = {
    "id": 5,
    "name": "3️⃣ Самостоятельная работа",
    "task_count": 5,
    "tasks": [first, second, third, fourth, fifth]
}
