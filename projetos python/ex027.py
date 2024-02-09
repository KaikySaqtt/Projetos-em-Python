nome = input('Fale seu nome: ')
separado = nome.split()
teste = len(separado)
ultimo = teste - 1
print('Primeiro nome: {}'.format(separado[0]))
print('Ultimo nome: {}'.format(separado[ultimo]))

