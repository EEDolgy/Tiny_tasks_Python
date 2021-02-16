'''Написать программу сложения и умножения двух
положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция,
элементы которой — цифры числа. Например, пользователь
ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].'''

from  collections import deque

NUMS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def sum_(a, b):
    rslt = deque()
    if len(a) < len(b):
        a, b = b, a
    lngth_diff = len(a) - len(b)
    for i in range(len(b)):
        eggs = NUMS[a[-i-1]] + NUMS[b[-i-1]]
        if len(rslt) == i:
            if eggs < 16:
                rslt.appendleft(NUMS[eggs])
            else:
                rslt.appendleft(NUMS[eggs - 16])
                rslt.appendleft('1')
        else:
            if eggs < 15:
                rslt[0] = NUMS[eggs + 1]
            elif eggs == 15:
                rslt[0] = '0'
                rslt.appendleft('1')
            else:
                rslt[0] = NUMS[eggs - 16 + 1]
                rslt.appendleft('1')
    if lngth_diff > 0:
        for i in range(lngth_diff):
            if len(rslt) == len(b) + i:
                rslt.appendleft(a[lngth_diff - i - 1])
            else:
                spam = NUMS[a[lngth_diff - i - 1]] + 1
                if spam < 16:
                    rslt[0] = NUMS[spam]
                else:
                    rslt[0] = '0'
                    rslt.appendleft('1')
    return rslt

def mult_(a, b):

    def single_mult(c, n):
        res = deque('0')
        for _ in range(n):
            res = sum_(res, c)
        return res

    rslt = deque(['0'])
    if len(a) < len(b):
        a, b = b, a

    for i, item in enumerate(b, 1):
        eggs = single_mult(a, NUMS[item])
        for _ in range(len(b) - i):
            eggs.append('0')
        rslt = sum_(rslt, eggs)

    return rslt

print('Введите два числа в шеснадцатиричной системе для сложения и умножения')
a = deque(input('Введите первое число: '))
b = deque(input('Введите второе число: '))

print(f'Сумма введенных чисел равна {sum_(a, b)}')
print(f'Произведение введенных чисел равно {mult_(a, b)}')