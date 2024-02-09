cont = 0
menor = 100
maior = 0
c = ''
soma = 0
while c != 'N':
    n1 = int(input('Me fale um número: '))
    c = str(input('Quer continuar [S/N]')).upper()
    cont += 1
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
    soma += n1
m = soma / cont
print('Você digitou {} números e a média deles foi {:.2f}'.format(cont, m))
print('O maior valor entre eles foi {}, já o menor foi {}.'.format(maior, menor))
