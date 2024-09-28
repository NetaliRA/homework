my_dict  = {'Nel': 1989, 'Alex': 1988, 'Rid': 1985}
print(my_dict)
print(my_dict['Nel'])
print(my_dict.get('Lana'))
my_dict.update({'Ben': 1983, 'Riana': 1984})
print(my_dict)
a = my_dict.pop('Rid')
print(a)
print(my_dict)
my_set = {5, 4, 7, 5, 4, 8, 5, 4, 9, 'Феху', 'Уруз', 'Феху', 'Иса', 'Гебо', 'Иса', (1,2,5,7,9,2)}
print(my_set)
my_set.add(13)
my_set.add('Лагуз')
# b = ('Лагуз', 13) #можно ли добавлять так элементы, если их несколько и они относятся к разным типам данных, и почему при добавлении, добовляется как кортеж, со скобками?
# my_set.add(b)
for b in range(20,25):
    my_set.add(b)   #попробовала еще такой вариант, подсказали в чате
print(my_set)
my_set.remove(5)
my_set.remove('Феху') #сделала еще раз для другого типа данных, я исследую :)
print(my_set)