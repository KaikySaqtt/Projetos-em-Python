sal = float(input('Qual seu salário?: '))
if sal <= 1250:
    aumento = sal + ((15 * sal)/100)
    print('O seu salário de {}R$ vai para {}R$'.format(sal, aumento))
else:
    aumento = sal + ((10 * sal)/100)
    print('O seu salário de {}R$ vai para {}R$'.format(sal, aumento))
