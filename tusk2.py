# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8

import random
quantity = int(input('Enter amount elements: '))
array = [random.randint(0, 9) for i in range(quantity)]
print(array, end = " ")
element = int(input(f'\nEnter X: '))
minimal = near = 10
for i in range(0, len(array)):
  diff = abs(element - array[i])
  if diff < minimal:
    minimal = diff
    near = array[i]
print(f'Ближайшее по значению число - {near}')