soma = 0
for c in range(0,6):
    n1 = int(input('Me fale o número'))
    if n1 % 2 == 0:
        soma = soma + n1
print('A soma de seus números pares é {}'.format(soma))
