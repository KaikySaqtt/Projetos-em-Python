n1 = int(input('Fale o primeiro número: '))
n2 = int(input('Fale o segundo número: '))
n3 = int(input('Fale o terceiro número: '))
maior = n1
if n2> n1 and n2> n3:
    maior = n2
if n3 > n1 and n3> n2:
    maior = n3

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('Seu menor valor é: {}'.format(menor))
print('Seu maior valor é: {}'.format(maior))

