n1 = int(input('Me fale um número e direi se é ou não primo: '))
ex = n1 - (n1 - 1)
c = 0
for q in range(ex, n1 + 1):
    if n1 % q == 0:
        c += 1
        print('\033[4;32m{}\033[m'.format(q), end=' ')
    else:
        print('\033[1;31m{}\033[m'.format(q), end=' ')
print('')
print('O seu número pode ser divisivel {} vezes!'.format(c))
if c > 2:
    print('{} não é um número primo'.format(n1))
else:
    print('{} é um número primo'.format(n1))
