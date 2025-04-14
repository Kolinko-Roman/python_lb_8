# Завдання 1

text = input("Введіть рядок: ")
vowels = 'аеєиіїоуюяАЕЄИІЇОУЮЯ'
vowel_list = [ch for ch in text if ch in vowels]
print(f"Кількість голосних: {len(vowel_list)}")
print("Голосні букви:", vowel_list)


# Завдання 2 

list1 = list(map(int, input("Введіть числа для списку 1 через пробіл: ").split()))
list2 = list(map(int, input("Введіть числа для списку 2 через пробіл: ").split()))

result = sorted(set(list1 + list2))
print("Результуючий список:", result)


# Завдання 3
from collections import Counter

text = input("Введіть текст: ")
frequency = Counter(text)
unique_symbols = [char for char, count in frequency.items() if count == 1]

print("Частота символів:")
for char, count in frequency.items():
    print(f"'{char}': {count}")

print("Унікальні символи:", unique_symbols)
