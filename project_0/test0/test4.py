
# Дан список кортежей ratings с рейтингами кафе.
# Кортеж состоит из названия и рейтинга кафе.
# Необходимо отсортировать список кортежей по убыванию рейтинга.
# Если рейтинги совпадают, то отсортировать кафе дополнительно по названию
# в алфавитном порядке.
# Получите словарь cafes с упорядоченными ключами из отсортированного списка,
# где ключи — названия кафе, а значения — их рейтинг.
ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
          ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
          ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]
# Отсортируйте список ratings по убыванию рейтинга. Для кафе
# с одинаковым рейтингом отсортируйте кортежи по названию.
ratings.sort(key=lambda x: (-x[1], x[0]))
# Сохраните данные с рейтингом в словарь cafes, где ключами являются
# названия кафе, а значениями - их рейтинг.
from collections import OrderedDict
cafes = OrderedDict(ratings)

# 4.10
#Напишите функцию task_manager, которая принимает список задач для
# нескольких серверов. Каждый элемент списка состоит из кортежа
# (<номер задачи>, <название сервера>, <высокий приоритет задачи>).
#Функция должна создавать словарь и заполнять его задачами по следующему
# принципу: название сервера — ключ, по которому хранится очередь
# задач для конкретного сервера.
# Если поступает задача без высокого приоритета
# (последний элемент кортежа — False),
# добавить номер задачи в конец очереди.
# Если приоритет высокий, добавить номер в начало.
#Для словаря используйте defaultdict, для очереди — deque.
#Функция возвращает полученный словарь с задачами.
tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

from collections import deque, defaultdict

def task_manager(tasks):
    servers = defaultdict(deque)
    for task in tasks:
        if task[-1]:
            servers[task[1]].appendleft(task[0])
        else:
            servers[task[1]].append(task[0])
    return servers
print(task_manager(tasks))


import numpy as np

mystery = np.array([[-13586,  15203,  28445, -27117,  -1781, -17182, -18049],
       [ 25936, -30968,  -1297,  -4593,   6451,  15790,   7181],
       [ 13348,  28049,  28655,  -6012,  21762,  25397,   8225],
       [ 13240,   7994,  32592,  20149,  13754,  11795,   -564],
       [-21725,  -8681,  30305,  22260, -17918,  12578,  29943],
       [-16841, -25392, -17278,  11740,   5916,    -47, -32037]],
      dtype=np.int16)

# В переменную elem_5_3 сохраните элемент из 5 строки и 3 столбца:
elem_5_3 = mystery[4, 2]

# В переменную last сохраните элемент из последней строки последнего столбца
last = mystery[-1, -1]

# В переменную line_4 сохраните строку 4
line_4 = mystery[3]

# В переменную col_2 сохраните предпоследний столбец
col_2 = mystery[:, -2]

# Из строк 2-4 (включительно) получите столбцы 3-5 (включительно)
part = mystery[1:4, 2:5]

# Сохраните в переменную rev последний столбец в обратном порядке
rev = mystery[::-1, -1]

# Сохраните в переменную trans транспонированный массив
trans = mystery.transpose()