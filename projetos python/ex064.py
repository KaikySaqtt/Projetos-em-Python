cont = 0
soma = 0
c = 0
while c != 999:
    c = int(input('Me fale um número: '))
    cont += 1
    soma += c
print('Você digitou {} números e a soma de todos foi {}.'.format(cont - 1, soma - 999))