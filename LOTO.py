"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import random

class Card:
    num_list = [el for el in range(1, 91)]

    def __init__(self, name):
        self.name = name
        self.data = [Card.add_spaces(Card.form_line()) for _ in range(3)]

    @classmethod
    def form_line(cls):
            numbers = cls.num_list.copy()
            line = []
            for i in range(5):
                var = numbers[:i-4] if i < 4 else numbers
                num = random.choice(var)
                line.append(num)
                numbers = [el for el in numbers if el > num]
            for el in line:
                cls.num_list.remove(el)
            return line

    @staticmethod
    def add_spaces(lst):
        places = [el for el in range(9)]
        for i in range(4):
                var = places[:i-3] if i < 3 else places
                place = random.choice(var)
                lst.insert(place, ' ')
                places = [el for el in places if el > place]
        return lst

    def __str__(self):
        result = 'Карточка ' + self.name + '\n'
        result += '-' * 22 + '\n'
        result += '\n'.join(' '.join(map(str, el)) for el in self.data) + '\n'
        result += '-' * 22
        return result

    def contains(self, item):
        for line in self.data:
            result = True if item in line else False
            if result:
                return True
        return False

    def is_empty(self):
        for line in self.data:
            for item in line:
                if type(item) == int:
                    return False
        return True

    def delete(self, num):
        for line in self.data:
            for i, item in enumerate(line):
                if item == num:
                    line[i] = '-'
                    break

class Game:
    num_list = [el for el in range(1, 91)]

    def __init__(self, player1, player2):
        self.card1 = Card(player1)
        self.card2 = Card(player2)
        self.turn = 1
        self.num_count = len(Game.num_list)

    def __str__(self):
        result = '\n' + f'Новый бочонок: {self.current_barrel} (осталось {self.num_count})\n'
        result += str(self.card1) + '\n' + str(self.card2)
        return result

    def new_barrel(self):
        self.current_barrel = random.choice(Game.num_list)
        self.num_count -= 1
        Game.num_list.remove(self.current_barrel)

    def choice(self, answ):
        answ = answ.lower()
        if answ == 'y':
            if self.card1.contains(self.current_barrel):
                self.card1.delete(self.current_barrel)
                return True
            else:
                return False
        elif answ == 'n':
            if self.card1.contains(self.current_barrel):
                return False
            else:
                return True

    def computer_choice(self):
        mistake = random.randint(0, 100)
        if self.card2.contains(self.current_barrel) and mistake >= 2:
                self.card2.delete(self.current_barrel)

game = Game('Human', 'Computer')
while True:
    game.new_barrel()
    print(game)
    answ = input('Зачеркнуть цифру? (y/n)')
    game.computer_choice()
    result = game.choice(answ)
    if not result:
        print('Вы проиграли, компьютер победил!')
        break
    if game.card1.is_empty() and not game.card2.is_empty():
        print('Вы обедили, компьютер проиграл!')
        break
    elif not game.card1.is_empty() and game.card2.is_empty():
        print('Вы проиграли, компьютер победил!')
        break
    elif game.card1.is_empty() and game.card2.is_empty():
        print('Ничья!')
        break