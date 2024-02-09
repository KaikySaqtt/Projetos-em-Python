print('=========== Lojas Cacique ===========')
valor = int(input('Me diga quanto deu o total de sua compra: '))
print('Como Será a forma de pagamento?')
print('Tecle [1] para pagar à vista')
print('Tecle [2] para pagar à vista no cartão')
print('Tecle [3] para pagar em 2 vezes no cartão')
print('Tecle [4] para pagar em 3 vezes ou mais no cartão')
opc = int(input('Qual sua opção? '))
if opc == 1:
    des = (10 * valor) / 100
    print('Já que você irar pagar à vista irar sair por R${:.2f} pois ganhou um desconto de 10%(R${})'.format(valor - des, des))
elif opc == 2:
    des = (5 * valor) / 100
    print('Já que você irar pagar à vista no cartão irar sair por R${:.2f} pois ganhou um desconto de 5%(R${})'.format(valor - des, des))
elif opc == 3:
    parcela = valor / 2
    print('Parcelando em duas vezes no cartão você terá duas parcelas de R${} sem juros'.format(parcela))
elif opc == 4:
    par = int(input('Em quantas vezes você quer parcelar?'))
    aum = (20 * valor) / 100
    preço = valor + aum
    parcel = preço / par
    print('Já que você irar parcelar em {} vezes terá um juros de 20%(R${}) e o preço final vai para R${} e sua parcela vai ser de R${:.2f}'.format(par, aum, preço, parcel))
else:
    print('A sua opção é invalida!')



