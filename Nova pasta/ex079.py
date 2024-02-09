valores = []
i = 0
resp = ''
while True:
    i = int(input('Me diga um número: '))
    if valores.count(i) == 0:
        valores.append(i)
    else:
        print('Esse valor já está na sua lista amigo! não vou o adiconar de novo.')
    resp = str(input('Quer continuar? [S/N]')).upper()
    if resp != 'S':
        break
valores.sort()
print(f'Em ordem do menor para o maior você digtou {valores}')
