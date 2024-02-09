n1 = int(input('Me fale o primeiro valor: '))
n2 = int(input('Muito bem, agora o segundo: '))
n3 = int(input('Terceiro: '))
n4 = int(input('E por ultímo o quarto: '))
tn = (n1, n2, n3, n4)
cont = 0
print('Os valores digitados foram: {}'.format(tn))
print(f'O número 9 apareceu {tn.count(9)} vezes')
print(f'Já o 3 apareceu {tn.count(3)} vezes')
for f in range(0,4):
    if tn[f] % 2 == 0:
        cont += 1
print(f'E os pares foram {cont}')