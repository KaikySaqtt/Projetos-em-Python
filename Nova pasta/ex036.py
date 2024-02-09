casav = int(input('Me fale o valor da casa: '))
sal = int(input('OK, agora me diga seu salario: '))
ano = int(input('E em quantos anos você pretende pagar: '))
prest = casav / (ano * 12)
saltrinta = (30 * sal) / 100
print('A sua parcela ira ficar R${:.2f} por mês'.format(prest))
if prest > saltrinta:
    print('Já que que você ganha {} a prestação irar ficar trinta porcento a cima do seu salario'.format(sal))
    print('Então terei que \033[1;97mnegalo\033[m!')
else:
    print('Já que você ganha R${} e a parcela vai fica R${:.2f} \033[1;97meu vou te consceder o emprestimo!\033[m'.format(sal, prest))
