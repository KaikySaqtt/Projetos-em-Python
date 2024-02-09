nome = input('Frase aqui: ')
nomeA = nome.upper().strip()
A = nomeA.count('A')
onde = nomeA.find('A') + 1
ondeu = nomeA.rfind('A') + 1
print('Em sua frasse temos {} a'.format(A))
print('O primeiro a está na posição {}'.format(onde))
print('E o ultimo está na posição {}'.format(ondeu))


