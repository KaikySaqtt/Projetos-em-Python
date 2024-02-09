import random
from time import sleep
print('=-' * 20)
print('Adivinhe qual número eu estou pensando')
print('Dica: è de 0 a 5')
print('=-' * 20)
ns = random.randint(0, 5)
resp = int(input('E ai? Qual é o número?'))
print('Conferindo...')
sleep(3)
if resp == ns:
    print('Droga você acertou!')
else:
    print('HAHAHA você errou noob eu pensei em {} não no {} não era óbvio?'.format(ns, resp))
    

