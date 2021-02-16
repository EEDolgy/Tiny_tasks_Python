'''Отсортируйте по возрастанию методом слияния одномерный
вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и
отсортированный массивы.'''

import random

MAX = 50
SIZE = 12

def merge_sort(arr):
    # print('*' * 50)
    # print(f'We checked {arr}')
    sz = len(arr)
    if sz < 2:
        # print(f'returning {arr}')
        return arr
    elif sz == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        # print(f'returning {arr}')
        return arr
    else:
        half = int(sz / 2 if sz % 2 == 0 else (sz + 1) / 2)
        spam = []
        # print(f'Let us consider {arr[0:half]} and {arr[half:sz]}')
        left = merge_sort(arr[0:half])
        right = merge_sort(arr[half:sz])
        # print(f'We considered {arr[0:half]} and {arr[half:sz]}')
        # print(f'Now they are {left} and {right}')
        for _ in range(sz):
            if left and right:
                if left[0] < right[0]:
                    spam.append(left[0])
                    left = left[1:]
                else:
                    spam.append(right[0])
                    right = right[1:]
            else:
                if left:
                    spam.extend(left)
                else:
                    spam.extend(right)
                break
        # print(f'returning {spam}')
        return spam

array = [(random.random() * MAX) for _ in range(SIZE)]

print(list(map(lambda x: round(x, 2), array)))
array = merge_sort(array)
print(list(map(lambda x: round(x, 2), array)))