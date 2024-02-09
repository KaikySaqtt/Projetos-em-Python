print('-' * 13)
print('Sequencia de Fibonacci')
print('-' * 13)
n = int(input('Quantos termo você que mostrar?'))
print('~' * 13)
n1 = 0
n2 = 1
if n < 1:
    print('Número inválido!')
elif n == 1:
    print('{}'.format(n1), end='')
elif n == 2:
    print('{} -> {}'.format(n1, n2), end='')
else:
    print('{} -> {}'.format(n1, n2), end='')
c = 2
while c < n:
    c += 1
    n3 = n1 + n2
    print(' -> {}'.format(n3), end='')
    n1 = n2
    n2 = n3
print(' FIM')
print('~' * 13)
