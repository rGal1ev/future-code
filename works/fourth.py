first = """
# 1
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A >= B:
    print("Ошибка входных данных! Число A должно быть меньше числа B")
    exit()

# Переменная для хранения количества чисел
N = 0

# Перебираем все числа от A до B включительно
for i in range(A, B+1):
    print(i)
    N += 1

print("Количество чисел:", N)
"""

second = """
# 2
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

N = B - A - 1  # количество чисел между A и B

for i in range(B-1, A, -1):
    print(i)

print("Количество чисел:", N)
"""

third = """
# 3
A = float(input("Введите вещественное число A: "))
N = int(input("Введите целое положительное число N: "))

result = 1
for _ in range(N): # _ Означает, что мы игнорируем итерируемое значение
    result *= A

print(A, "в степени", N, "равно", result)
"""

fourth = """
# 4
A = float(input("Введите вещественное число A: "))
N = int(input("Введите целое положительное число N: "))

for i in range(1, N+1):
    result = A ** i
    print(result)
"""

fifth = """
# 5
A = float(input("Введите вещественное положительное число A: "))

N = 1
summ = 1.0

while summ <= A:
    N += 1
    summ += 1/N

print("Наименьшее целое число N:", N)
print("Сумма 1 + 1/2 + ··· + 1/N:", summ)
"""

sixth = """
# 6
n = int(input("Введите целое число N: "))

result = 1

for i in range(1, n+1):
    result *= i

print("Произведение чисел от 1 до", n, "равно", result)
"""

seventh = """
# 7
N = int(input("Введите число N: "))

result = 1
for i in range(2, N+1):
    result *= 1/i

print("Результат:", result)
"""

eighth = """
# 8
n = int(input("Введите число N: "))

sum_of_squares = 0
for i in range(1, n+1):
    sum_of_squares += i**2

print("Сумма квадратов чисел от 1 до", n, "равна", sum_of_squares)
"""

ninth = """
# 9
N = int(input("Введите число N: "))
sum_s = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        sum_s += i ** 2
    else:
        sum_s += i ** 3

print("Сумма S квадратов четных и кубов нечетных чисел от 1 до", N, "равна:", sum_s)
"""

tenth = """
#10
N = int(input("Введите значение N: "))

for i in range(1, N+1):
    if i % 5 == 0:
        print(i)
"""

work = {
    "id": 4,
    "name": "4️⃣ Самостоятельная работа",
    "task_count": 5,
    "tasks": [first, second, third, fourth, fifth]
}
