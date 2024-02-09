print('GERADOR DE PA')
print('=' * 13)
pm = int(input('Me fale o primeiro termo: '))
rz = int(input('Agora a razão: '))
c = 0
termo = pm + rz
print('A razão é {} -> '.format(pm), end='')
g = 0
while c < 9:
    c += 1

    if c <9:
        print(termo, end='-> ')
    else:
        print(termo, end='-> FIM')
    termo += rz
    g = termo - rz
r = 1
co = 0
print('')
while r != 0:
    print('')
    co = 0
    r = int(input('Quantas vezes mais você quer: '))
    while co < r:
        co += 1
        if co < r:
            print(termo, end='-> ')
        else:
            print(termo, end='-> FIM')
        termo += rz
        g = termo - rz
print('')
print('Obrigado por utilizar nosso programa!')
