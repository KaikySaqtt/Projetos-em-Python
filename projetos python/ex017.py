import math
c1 = float(input('Fale o primeiro cateto'))
c2 = float(input('Fale o outro'))
soma = math.pow(c1, 2) + math.pow(c2, 2)
raiz = math.sqrt(soma)
print('A hipotenusa sera: {:.2f}'.format(raiz))

