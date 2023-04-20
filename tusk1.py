# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 3 2 3 7 5
# Ввод: 3


amountOfNumbers = int(input("Enter NUM: "))
count = 0
SearchNumX = int(input("Enter X:" ))
for i in range(amountOfNumbers):
    nums = int(input("Enter nums: "))
    if SearchNumX == nums:
        count+=1
        i+=1
print("count X = ", count)