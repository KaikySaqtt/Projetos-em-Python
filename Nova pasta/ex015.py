d = int(input('Por quantos dia o senhor(a) alugou o carro?: '))
k = float(input('Quantos Kms foram rodados?: '))
dp = 60 * d
kp = k * 0.15
tp = float(dp) + kp
print('Já que o senhor(a) ficou com o carro por {} dia vai ter que pagar R${} pelos os dia e já que andou {}Kms vai te que pagar mais R${:.2f} pelos Kms ou seja irar pagar na somátoria: R${} '.format(d, dp, k, kp, tp))



