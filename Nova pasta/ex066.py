cont = soma = 0
while True:
    n1 = int(input('Me diga um número(Caso o número 999 for digitado pararemos o programa): '))
    if n1 == 999:
        break
    soma += n1
    cont += 1
print(f'A soma de seus {cont} números deu {soma}')
