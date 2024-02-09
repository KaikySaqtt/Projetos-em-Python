import random
a1 = input('Fale o primeiro aluno')
a2 = input('Fale o segundo aluno')
a3 = input('Fale o terceiro aluno')
a4 = input('Fale o quarto aluno')
lista = [a1, a2, a3, a4]
ns = random.randint(1, 4)
print('O aluno ganhador foi {} Parabens!'.format(lista[ns]))

