students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]

from collections import defaultdict
groups = defaultdict(list)

for student, group in students:
    groups[group].append(student)
print(groups)
print()
print(groups[3])
print()
print(groups[2021])
print()
print(groups)