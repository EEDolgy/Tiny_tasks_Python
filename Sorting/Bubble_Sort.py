'''Отсортируйте по убыванию методом пузырька одномерный
целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный
и отсортированный массивы.'''

import random

FST = -100
LST = 99
SIZE = 12

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j + 1] > arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

array = [random.randint(FST, LST) for _ in range(SIZE)]

print(array)
bubble_sort(array)
print(array)