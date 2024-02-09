print('GERADOR DE PA')
print('=' * 13)
pm = int(input('Me fale o primeiro termo: '))
rz = int(input('Agora a razão: '))
c = 0
termo = pm + rz
print('A razão é {} -> '.format(pm), end='')
while c < 9:
    c += 1

    if c <9:
        print(termo, end='-> ')
    else:
        print(termo, end='-> FIM')
    termo += rz
