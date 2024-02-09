from random import randint
ns = (randint(1, 10), randint(1, 10), randint(1,10), randint(1, 10), randint(1, 10))
print('Os números sorteados foram: ', end='')
for c in ns:
    print(c, end=' ')
print('')
print(f'O nosso menor valor foi {min(ns)}')
print(f'O nosso maior valor foi {max(ns)}')