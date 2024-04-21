# задание 1
print("Задание 1")
n = int(input("n = "))
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum += i
print(sum)

n2 = int(input("n = "))
i = 1
sum2 = 0
while i <= n2:
  if i % 2 == 0:
    sum2 += i
  i += 1
print(sum2)
print("")

# задание 2
print("Задание 2")
arr = ['яблоко', 'апельсин', 'кот', 'ток', 'гидроэлектростанция']
max_len = -1
world = ''
for i in arr:
    if len(i) > max_len:
        max_len = len(i)
        world = i
print("Самое длинное слово: " + world)

arr2 = ['яблоко', 'апельсин', 'кот', 'ток', 'гидроэлектростанция']
max_len2 = -1
i2 = 0
world2 = ''
while i2 <= (len(arr2) - 1):
    if len(arr2[i2]) > max_len2:
        max_len2 = len(arr2[i2])
        world2 = arr2[i2]
    i2 += 1
print("Самое длинное слово: " + world2)
print("")

# задание 3
print("Задание 3")
n3 = int(input("Введите число: "))
factorial = 1
for i in range(2, n3+1):
    factorial *= i
print(factorial)
print("")

# задание 4
print("Задание 4")
arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for index, value in enumerate(arr3):
    if (index + 1) % 3 == 0:
        print(f"arr[{index}] = {value}")
print("")

# задание 5
print("Задание 5")
n4 = int(input("n = "))
print(f"Таблица умножения для числа {n4}:")
for i in range(1, 11):
    res = n4 * i
    print(f"{n4} * {i} = {res}")
print("")

# задание 6
print("Задание 6")
num1 = int(input("num = "))
count1 = 0
while num1 != 0:
    num1 //= 10
    count1 += 1
print(f"Количество цифр: {count1}")

num2 = int(input("num = "))
count2 = 0
for i in str(num2):
    if i.isdigit():
        count2 += 1
print(f"Количество цифр: {count2}")
print("")

# задание 7
print("Задание 7")
def is_palindrome(text):
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    length = len(clean_text)
    for i in range(length // 2):
        if clean_text[i] != clean_text[length - i - 1]:
            return False
    return True

text = input("Введите строку = ")
if is_palindrome(text):
    print(f"Строка '{text}' является палиндромом")
else:
    print(f"Строка '{text}' не является палиндромом")
print("")

# задание 8
print("Задание 8")
def has_duplicates(arr):
    duplicates = []
    for i in arr:
        if i in duplicates:
            return True
        duplicates.append(i)
    return False

arr4 = ['яблоко', 'апельсин', 'кот', 'кот', 'гидроэлектростанция']
if has_duplicates(arr4):
    print("Список содержит дубликаты")
else:
    print("Список не содержит дубликатов")
print("")

# задание 9
print("Задание 9")
def remove_duplicates(arr):
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[i] == arr[j]:
                arr.pop(j)
            else:
                j += 1
        i += 1
    return arr

arr5 = ['яблоко', 'апельсин', 'кот', 'кот', 'гидроэлектростанция']
res = remove_duplicates(arr5)
print(f"Массив значений без дубликатов: {res}")

def remove_duplicates(arr):
    for i in range(len(arr)):
        j = i + 1
        while j < len(arr):
            if arr[i] == arr[j]:
                del arr[j]
            else:
                j += 1
    return arr

arr6 = ['яблоко', 'апельсин', 'кот', 'кот', 'гидроэлектростанция']
res2 = remove_duplicates(arr6)
print(f"Массив значений без дубликатов: {res2}")
print("")

# задание 10
print("Задание 10")
def reverse_text(text):
    for i in range(len(text) - 1, -1, -1):
        print(text[i])
text2 = input("Введите строку: ")
reverse_text(text2)
print("")

# задание 11
print("Задание 11")
def show_calendar():
    days_in_month = 31
    start_day = 1
    week_days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    print('\033[91m' + "Пн Вт Ср Чт Пт Сб Вс" + '\033[0m')
    while start_day <= days_in_month:
        for _ in week_days:
            if start_day <= days_in_month:
                print('\033[91m' + "{:2}".format(start_day) + '\033[0m', end=" ")
                start_day += 1
            else:
                print("   ", end=" ")
        print()

show_calendar()
