soma = 0
cont = 0
for c in range(0, 501):
    resto = c % 2
    restod = c % 3

    if resto != 0 and restod == 0:
        soma = soma + c
        cont = cont + 1
print('A soma desse {} números foi igual é = {}'.format(cont, soma))
print('Acabou')

