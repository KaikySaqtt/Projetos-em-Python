ari = str(input('Digite sua expresão: '))
cont = 0
contd = 0
for c in range(len(ari)):
    if ari[c] == '(':
        cont += 1
    elif ari[c] == ')':
        contd += 1
if cont == contd:
    print('Essa expresão pode ser resolvida!')
else:
    print('Expressão invalida')

