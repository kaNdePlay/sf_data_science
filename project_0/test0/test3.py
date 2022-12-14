from collections import deque

limited = deque(maxlen=3)
print(limited)
 
limited_from_list = deque([1,3,4,5,6,7], maxlen=3)
print(limited_from_list)
print(limited.append(8))
print(limited)

# Посчитаем динамику средней температуры с усреднением
# за каждые последние 7 дней для каждого рассматриваемого дня.
# Для этого воспользуемся очередью с параметром maxlen=7:
temps = [20.6, 19.4, 19.0, 19.0, 22.1,
        22.5, 22.8, 24.1, 25.6, 27.0,
        27.0, 25.6, 26.8, 27.3, 22.5,
        25.4, 24.4, 23.7, 23.6, 22.6,
        20.4, 17.9, 17.3, 17.3, 18.1,
        20.1, 22.2, 19.8, 21.3, 21.3,
        21.9]
days = deque(maxlen=7)
 
for temp in temps:
    # Добавляем температуру в очередь
    days.append(temp)
    # Если длина очереди оказалась равной максимальной длине очереди (7),
    # печатаем среднюю температуру за последние 7 дней
    if len(days) == days.maxlen:
        print(round(sum(days) / len(days), 2), end='; ')
# Напечатаем пустую строку, чтобы завершить действие параметра
# end. Иначе следующая строка окажется напечатанной на предыдущей
print("")
# Как видите, для решения этой задачи очень подошла очередь с ограниченной
# длиной, поскольку нам не приходилось самостоятельно контролировать число
# элементов. Структура данных сама контролировала все технические детали.
#-----------------------------------------------------
#Дан список из кортежей temps. На первом месте в кортеже указан год в виде строки,
# а на втором — средняя температура января в Петербурге в указанном году.

#Необходимо напечатать словарь, в котором ключи — годы, а значения — показатели температуры.
# Ключи необходимо отсортировать в порядке убывания соответствующих им температур.

#Пример входа:
#temps =  [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]
#Пример вывода:
#OrderedDict([('2001', -2.5), ('2000', -4.4), ('2002', -4.4), ('2003', -9.5)])
temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

from collections import OrderedDict

def check(temps):
    temps.sort(key=lambda x: x[1], reverse=True)
    od = OrderedDict(temps)
    od = str(od)
    print(od)
# or
from collections import OrderedDict

def check(temps):
    needed_dict = OrderedDict(reversed(sorted(temps, key=lambda x: x[1])))
    print(needed_dict)