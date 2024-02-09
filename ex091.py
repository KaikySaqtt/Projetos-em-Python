import random
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1': random.randint(1,6),
    'jogador2': random.randint(1,6),
    'jogador3': random.randint(1,6),
    'jogador4': random.randint(1,6),
}
print('Os valores sorteados foram:')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(0.8)
raking = []
raking = sorted(jogo.items(),  key=itemgetter(1), reverse=True)
for i, v in enumerate(raking):
    print(f'{i + 1} lugar: {v[0]} com {v[1]}.')
    sleep(1)
    
    