first = """
# 1
sum_ = 0
for _ in range(10):
    num = int(input("Введите число: "))
    sum_ += num

print("Сумма чисел:", sum_)
"""

second = """
# 2
words = []

for i in range(6):
    word = input("Введите слово: ")
    words.append(word)

reversed_words = words[::-1]
print("Слова в обратном порядке: ", reversed_words)
"""

third = """
# 3
numbers = []

for i in range(5):
    number = int(input("Введите число: "))
    numbers.append(number)

print("Наименьшее число:", min(numbers))
"""

fourth = """
# 4
numbers = []

for i in range(5):
    number = int(input("Введите число: "))
    numbers.append(number)

print("Четные числа:")
for number in numbers:
    if number % 2 == 0:
        print(number)
"""

fifth = """
# 5
numbers = []
result = 1

for i in range(5):
    number = int(input("Введите число: "))
    numbers.append(number)

for i in range(len(numbers)):
    result *= numbers[i]

print("Произведение:", result)
"""

sixth = """
# 6
words = []

for i in range(5):
    word = input("Введите слово: ")
    words.append(word)

words.sort()

print("Слова в алфавитном порядке:")
for word in words:
    print(word)
"""

seventh = """
# 7
numbers = []

for i in range(5):
    number = int(input("Введите число: "))
    numbers.append(number)

max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print("Наибольший элемент:", max_number)
"""

eighth = """
# 8
lst = input("Введите элементы списка через пробел: ").split()

if len(lst) > 0:
    lst[0], lst[-1] = lst[-1], lst[0]

print(lst)
"""

ninth = """
# 9
import random

numbers = random.sample(range(-10, 10), 10)
max_abs = 0

for num in numbers:
    if abs(num) > max_abs:
        max_abs = abs(num)

print("Максимальное по модулю число в списке:", max_abs)
print(numbers)
"""

tenth = """
# 10
import random

numbers = random.sample(range(-10, 10), 10)

sum_ = 0
count = 0

for num in numbers:
    if num > 0:
        sum_ += num
        count += 1

if count > 0:
    average = sum_ / count
    print("Среднее арифметическое положительных элементов:", average)
else:
    print("В списке нет положительных элементов.")
"""

work = {
    "id": 2,
    "name": "2️⃣ Самостоятельная работа",
    "task_count": 7,
    "tasks": [first,
              second,
              third,
              fourth,
              fifth,
              sixth,
              seventh,
              eighth,
              ninth,
              tenth]
}
