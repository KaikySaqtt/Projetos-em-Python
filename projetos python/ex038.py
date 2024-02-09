n1 = int(input('Me fale o primeiro número'))
n2 = int(input('Me fale o segundo número'))
if n1 > n2:
    print('O primero valor é \033[1;97mmaior\033[m!')
elif n2 > n1:
    print('O segundo valor é \033[1;97mmaior\033[m!')
else:
    print('Os dois números são iguais')
