first = """
# 1
string = input("Введите строку: ")
count = string.count('а')

if count == 1:
    index = string.index('а')
    print(f"Индекс буквы 'а': {index}")
elif count >= 2:
    first_index = string.index('а')
    last_index = string.rindex('а')
    print(f"Индекс первого появления 'а': {first_index}")
    print(f"Индекс последнего появления 'а': {last_index}")
"""

second = """
# 2
string = input("Введите строку с двумя 'a': ")

first_a = string.index('а')
last_a = string.rindex('а')

new_string = string[:first_a] + string[last_a + 1:]
print("Результат:", new_string)
"""

third = """
# 3
s = input("Введите строку: ")

first_a = s.index("а")
last_a = s.rindex("а")

substring = s[first_a+1:last_a]
reversed_substring = substring[::-1]

result = s[:first_a+1] + reversed_substring + s[last_a:]
print("Результат:", result)
"""

fourth = """
# 4
string = input("Введите строку символов: ")

comma_dash = False
dash_comma = False

for i in range(len(string) - 1):
    if string[i] == ',' and string[i+1] == '-':
        comma_dash = True
        break

    elif string[i] == '-' and string[i+1] == ',':
        dash_comma = True
        break

if comma_dash:
    print("В строке есть запятая и тире, идущие друг за другом")
elif dash_comma:
    print("В строке есть тире и запятая, идущие друг за другом")
else:
    print("В строке нет запятой и тире, идущих друг за другом")
"""

fifth = """
# 5
string = input("Введите строку: ")

length = len(string)
half_length = length // 2

first_half = string[:half_length]
second_half = string[half_length:]

count_first_half = first_half.count('!')
count_second_half = second_half.count('!')

if count_first_half > count_second_half:
    print('Больше восклицательных знаков в первой половине строки')
elif count_second_half > count_first_half:
    print('Больше восклицательных знаков во второй половине строки')
else:
    print('Одинаковое количество восклицательных знаков в обеих половинах строки')
"""

sixth = """
# 6
string = input("Введите строку: ")

count = 0
max_count = 0

for char in string:
    if char == 'а':
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0

print("Наибольшее число букв «а», идущих подряд:", max_count)
"""

seventh = """
# 7
string = input()

# третий символ
print(string[2])

# предпоследний символ
print(string[-2])

# первые пять символов
print(string[:5])

# всё, кроме последних двух символов
print(string[:-2])

# символы с четными индексами
print(string[::2])

# символы с нечетными индексами
print(string[1::2])

# символы в обратном порядке
print(string[::-1])

# символы через один в обратном порядке
print(string[::-2])

# длина строки
print(len(string))
"""

eighth = """
# 8
string = input("Введите строку: ")
words = string.split()
word_count = len(words)

print("Количество слов в строке:", word_count)
"""

ninth = """
# 9
string = input("Введите строку: ")

half = len(string) // 2
if len(string) % 2 == 1:
    half += 1

new_string = string[half:] + string[:half]
print(new_string)
"""

tenth = """
# 10
words = input("Введите два слова: ").split()
reversed_words = words[::-1]
result = " ".join(reversed_words)
print(result)
"""

eleventh = """
# 11
s = input()

first_index = s.find('f')
last_index = s.rfind('f')

if first_index == last_index:
    if first_index != -1:
        print(first_index)
else:
    print(first_index, last_index)
"""

twelfth = """
# 12
s = input()
count = 0

for i in range(len(s)):
    if s[i] == "f":
        count += 1
        if count == 2:
            print(i)
            break

if count == 1:
    print(-1)
elif count == 0:
    print(-2)
"""

thirteenth = """
# 13
string = input("Введите строку: ")

first_h_index = string.index('h')
last_h_index = string.rindex('h')

new_string = string[:first_h_index] + string[last_h_index + 1:]
print(new_string)
"""

fourteenth = """
# 14
string = input("Введите строку: ")

first_h_index = string.find('h')
last_h_index = string.rfind('h')

reversed_substring = string[first_h_index+1:last_h_index][::-1]

result = string[:first_h_index+1] + reversed_substring + string[last_h_index:]
print("Результат:", result)
"""

fifteenth = """
# 15
string = input("Введите строку: ")

new_string = string.replace("1", "one")
print("Новая строка:", new_string)
"""

work = {
    "id": 1,
    "name": "1️⃣ Самостоятельная работа",
    "task_count": 5,
    "tasks": [first,
              second,
              third,
              fourth,
              fifth,
              sixth,
              seventh,
              eighth,
              ninth,
              tenth,
              eleventh,
              twelfth,
              thirteenth,
              fourteenth,
              fifteenth]
}
