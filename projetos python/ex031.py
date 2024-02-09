distancia = float(input('Me fale o quanto de km você irar percorer: '))
if distancia < 200:
    preco = distancia * 1/2
    print('Sua viajem vai custa {:.2f}R$'.format(preco))
else:
    preco = distancia * 0.45
    preco2 = distancia * 1 / 2
    print('Opa, você tera um desconto por que irar percorer mais de 200KM!')
    print('Em vez de pagar {} com 0,50 por KM'.format(preco2))
    print('Você vai pagar só {} pois a tarifa cai para 0,45!'.format(preco))

