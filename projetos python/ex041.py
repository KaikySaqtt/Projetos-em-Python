data = int(input('Em que ano você nasceu: '))
idade = 2023 - data
print('O atleta tem {} anos'.format(idade))
if idade < 10:
    print('Classificação: Mirim')
elif idade < 15:
    print('Classificação: Infantil')
elif idade < 20:
    print('Classificação: Junior')
elif idade < 26:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')
