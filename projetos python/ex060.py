import math
n1 = int(input('Me fale de qual número você quer calcular o fatorial: '))
c = n1
print('Calculando o fatorial de {}, {}! = {}X'.format(n1, n1, n1), end='')
while c > 1:
    c -= 1
    print(c, end='')
    if c > 1:
        print('X', end='')
f = math.factorial(n1)
print('= ', f)



