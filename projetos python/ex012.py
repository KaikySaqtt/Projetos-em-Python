n1 = float(input('Qual o preço de seu produto?'))
d = (n1 * 5)/100
v = n1 - d
print('O produto de valor R$\033[1;97m{}\033[m, na promoção saira por \033[1;34m{:.2f}\033[m pois temos um desconto de 5%(R%{:.2f})'.format(n1, v, d))
