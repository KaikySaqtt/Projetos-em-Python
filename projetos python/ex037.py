valor = int(input('Me fale um número inteiro: '))
print('CALCULADORA PARA CONVERTER')
print('Tecle [1] para binário')
print('Tecle [2] para octal')
print('Tecle [3] para hexadecimal')
escolha = int(input(''))
if escolha == 1:
    print('O {} em binário ficaria: {}'.format(valor, bin(valor)))
elif escolha == 2:
    print('O {} em octal ficaria: {}'.format(valor, oct(valor)))
elif escolha == 3:
    print('O {} em hexadecimal ficaria: {}'.format(valor, hex(valor)))
else:
    print('Seu número foi invalido!')

