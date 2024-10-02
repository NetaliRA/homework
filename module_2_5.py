def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(*[value])
    return matrix
n = int(input('Напишите количество строк в матрице '))
m = int(input('Напишите количество столбцов в матрице '))
value = int(input('Напишите значение матрицы '))

matrix = get_matrix(n, m, value)
if n <= 0:
    print(n)
elif m <=0:
    print(m)
else:
    print()
    for i in matrix:
        print(*i)