cont = 0
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Me fale o pesso da {}° pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('O seu menor peso foi {:.1f}KG e o menor {:.1f}KG'.format(menor, maior))