'''Сформировать из введенного числа обратное по порядку
входящих в него цифр и вывести на экран. Например,
если введено число 3486, надо вывести 6843'''

def reverse(num):
    if num // 10 == 0:
        return str(num)
    return str(num % 10) + reverse(num // 10)

num = int(input('Введите натуральное число: '))
num = reverse(num)
print(num)