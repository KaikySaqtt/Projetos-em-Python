n1 = float(input('Largura da parede: '))
n2 = float(input('Altura da parede: '))
d = n1 * n2
m = d / 2
print('Sua parede tem dimensão de \033[1;32m{}X{}\033[m ou seja a area é \033[4;36m{}\033[m'.format(n1, n2, d))
print('Sua parede irar precisa de {}L para ser pintada'.format(m))
