nome = ''
idade = int(0)
sexo = ''
me = 0
m = 0
i = 0
mi = 0
nm = ''
fi = 0
cont = 0
for c in range(1,5):
    print('---{}° pessoa---'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    m += idade
    me = idade / c
    if sexo == 'M' or sexo == 'm':
        i = idade
        if idade > i:
            mi = idade
            nm = nome
        if c == 1:
            mi = idade
            nm = nome
    if sexo == 'f' or sexo == 'F':
        fi = idade
        if fi < 21:
            cont += 1
print('A média de idade do seu grupo ficou em {}'.format(me))
print('O homem mais velho tem {} anos e se chama {}'.format(mi, nm))
print('Temos {} mulheres com menos de 20 anos'.format(cont))







