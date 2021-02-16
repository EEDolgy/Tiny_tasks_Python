'''
https://drive.google.com/file/d/1yhgJNpVSrhXVOHsnP-Sm00BGxhASb8Wb/view?usp=sharing
Посчитать четные и нечетные цифры введенного
 натурального числа. Например, если введено число 34560,
 в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).'''

def func(num):
    if num // 10 == 0:
        if num % 2 == 0:
            return(0, 1)
        else:
            return(1, 0)
    else:
        a = num % 10
        fst, snd = func(num // 10)
        if a % 2 == 0:
            return (fst, snd + 1)
        else:
            return (fst + 1, snd)

num = int(input('Введите натуральное число: '))
odd, even = func(num)
print(f'Количество нечетных цифр в числе равно {odd},'
      f'\n а количество четных - {even}')