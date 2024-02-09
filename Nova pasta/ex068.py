import random
contv = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR!')
print('=-' * 20)
spi = ''
while True:
    n1 = int(input('Me diga um número: '))
    pi = str(input('Você quer par ou impar? [P/I]: ')).upper()
    cn = random.randint(1, 10)
    rd = cn + n1
    if rd % 2 == 0:
        spi = 'PAR'
    else:
        spi = 'IMPAR'
    print('Você jogou {} e eu {}. Total é igual á {} e é {}'.format(n1, cn, rd, spi))
    print('-' * 40)
    if pi == 'P':
        if rd % 2 == 0:
            print('VOCÊ GANHOU, QUE RAIVA!')
            contv += 1
        else:
            print('VOCÊ PERDEU! HAHAHA')
            print('=-' * 20)
            print('GAMER OVER!, Você ganhou {} vezes'.format(contv))
            break

    elif pi == 'I':
        if rd % 2 != 0:
            print('VOCÊ GANHOU, QUE RAIVA!')
            contv += 1
        else:
            print('VOCÊ PERDEU! HAHAHA')
            print('=-' * 20)
            print('GAMER OVER!, Você ganhou {} vezes'.format(contv))
            break
