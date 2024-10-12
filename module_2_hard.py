import random
def get_key():
    num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers = list(range(3, 21))
    key = random.choice(numbers)
    return key

def get_code(n):
    dict = {3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645, 10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867, 14: 1611325212343114105968, 15: 1214114232133124115106978, 16: 1317115262143531341251161079, 17: 11621531441351261171089, 18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910, 20: 13141911923282183731746416515614713812911}
    code = dict.get(n)
    return code

n = get_key()
print('Пароль:', n)

num1 = list(range(1, n))
num2 = list(range(1, n))
pairs = []
result = ''

for i in num1:
    for j in num2:
        m1 = i
        m2 = j
        if m1 >= m2:
            continue
        else:
            aliquot = n % (m1 + m2)
            if aliquot == 0:
                pairs.append([m1, m2])
                result = result + str(m1) + str(m2)
print('Пары чисел', *pairs)
print('Введите пароль', result )
