n1 = float(input('Fale me sua primeira nota: '))
n2 = float(input('Fale me sua segunda nota: '))
m = (n1 + n2) / 2
print('Com {:.2f} e {:.2f} a sua média irar ficar {:.2f}'.format(n1, n2, m))
if m < 5:
    print('Com essa média infelizmente você foi \033[1;31mreprovado\033[m!')
elif m <= 6.9:
    print('Com essa média você vai fica de \033[1;34mrecuperação\033[m!')
elif m == 10:
    print('Meu Deus você tiro a nota \033[97mmáxima\033[m!!!')
else:
    print('Com essa média você \033[1;32mpassou\033[m!')
