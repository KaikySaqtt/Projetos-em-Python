contm = 0
conth = 0
contmm = 0
while True:
    print('=' * 40)
    print('CADASTRE UMA PESSOA!')
    print('=' * 40)
    idade = int(input('Idade: '))
    sexo = input('Sexo[M/F]: ').upper()
    if idade > 17:
        contm += 1
    if idade < 20 and sexo == 'F':
        contmm += 1
    if sexo == 'M':
        conth += 1
    resp = input('Quer continuar? [S/N]: ').upper()
    if resp != 'S':
        break
print(f'Total de pessoas maiores de idade é: {contm}.')
print(f'Temos {conth} homens no sistema.')
print(f'E na somátoria ficamos com {contmm} mulheres que tem menos de vinte anos.')