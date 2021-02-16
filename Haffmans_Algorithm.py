'''Закодируйте любую строку по алгоритму Хаффмана.'''

from collections import Counter

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def path(self, num=None):
        if self.data is not None:
            return {self.data: num}
        else:
            l = self.left.path('0')
            r = self.right.path('1')
            dct = l
            for key, val in r.items():
                dct[key] = val
            if num is not None:
                for key in dct:
                    dct[key] = num + dct[key]
            return dct

    def __str__(self):
        if self.data is None:
            return f'Node({str(self.left)} {str(self.right)})'
        else:
            return f'Node({self.data})'


inpt_data = input('Введите строку: ')
str_ = Counter(inpt_data)

while len(str_) > 1:
    l = str_.most_common()[-1]
    r = str_.most_common()[-2]
    l_val = l[0] if type(l[0]) is Node else Node(l[0])
    r_val = r[0] if type(r[0]) is Node else Node(r[0])
    node = Node(None, l_val, r_val)
    str_[node] = l[1] + r[1]
    str_[l[0]] = 0
    str_[r[0]] = 0
    str_ += Counter()

dictionary = list(str_)[0].path()
print('Таблица кодировки:')
for key, val in dictionary.items():
    print(f'{key}: {val}')

otpt_data = []
for item in inpt_data:
    otpt_data.append(dictionary[item])

print(f"Закодированная строка: {''.join(otpt_data)}")

