valores = []
pares = []
impares = []
i = 0
resp = ''
while True:
    i = int(input('Me diga um número: '))
    if valores.count(i) == 0:
        valores.append(i)
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    else:
        print('Esse valor já está na sua lista amigo! não vou o adiconar de novo.')
    resp = str(input('Quer continuar? [S/N]')).upper()
    if resp != 'S':
        break
print(f'A lista completa é: {valores}')
print(f'A lista dos pares é: {pares}')
print(f'A lista dos impares é: {impares}')
