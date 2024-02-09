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
print(f'Você digitou {len(valores)} números sem repetição')
valores.sort(reverse=True)
print(f'Em ordem do maior para o menor fica {valores}')
if 5 in valores:
    print('Temos o número 5')
else:
    print('Não temos o número 5')