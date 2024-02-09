numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', "oito", 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezeseis', 'dezesete','dezoito','dezenove', 'vinte')
resp = 0
while True:
    resp = int(input('Fale um número de um a vinte e lhe direi seu extenso: '))
    if resp > 20 or resp < 0:
        print('Número invalido tente novamente')
    else:
        print(f'Você digitou o número {numeros[resp]}')
        break