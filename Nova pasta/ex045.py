import random
import time
print('=-=' * 20)
print('\033[1;34mJOKEMPO\033[m')
print('=-=' * 20)
print('Suas opções são:')
print('[1] para Pedra')
print('[2] para Papel')
print('[3] para Tesoura')
opc = int(input('E ai qual vai ser? '))
print('Jo')
time.sleep(1)
print('KEM')
time.sleep(1)
print('PO')
time.sleep(1)
ns = random.randint(0,2)
opx = ['Pedra', 'Papel', 'Tesoura']
comp = opx[ns]
opr = opc - 1
opcr = opx[opr]
print('=-=' * 20)
print('O computador escolheu {}'.format(comp))
print('O jogador escolheu {}'.format(opcr))
print('=-=' * 20)
if ns == 0 and opr == 1:
    print('Parabéns você \033[1;32mganhou\033[m!')
elif ns == 0 and opr == 2:
    print('HAHAHA Você perdeu \033[1;31mlooser\033[m!')
elif ns == 1 and opr == 0:
    print('HAHAHA Você perdeu \033[1;31mlooser\033[m!')
elif ns == 1 and opr == 2:
    print('Parabéns você \033[1;32mganhou\033[m!')
elif ns == 2 and opr == 1:
    print('HAHAHA Você perdeu \033[1;31mlooser\033[m!')
elif ns == 2 and opr == 0:
    print('Parabéns você \033[1;32mganhou\033[m!')
else:
    print('Nossa parece que empatamos!')
