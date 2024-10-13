def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(5, 'honey')
print_params(3, None, False)
print_params(55)
print_params()

print_params(b=25)  #работает
print_params(c=[1, 2, 3])   #работает

values_list = [75, None, 'Текст']
values_dict = {'a':11111, 'b':"Bear", 'c':True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Winne Pooh', 80]
print_params(*values_list_2, 8)  #работает