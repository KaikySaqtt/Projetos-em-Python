data = int(input('Em que ano você nasceu: '))
idade =  2023 - data
print('Quem nasceu em {} tem {} anos em 2023'.format(data, idade))
if idade == 18:
    print('Seu alistamento séra feito esse ano, Fique esperto!')
elif idade < 18:
    alista = 18 - idade
    print('Faltam {} anos para você se alista!'.format(alista))
    print('Você se alistará no ano {} '.format(alista + 2023))
else:
    print('Você já se alistou pd ficar tranquilo')
