import random
print('\033[1;33mEu o computador pensei em número de 1 a 10\033[m')
resp = int(input('E ai, qual teu palpite? '))
ns = random.randint(1, 10)
cont = 0
while resp != ns:
    if resp > ns:
        resp = int(input('\033[1;91mO número que pensei é menor, e ai, qual teu palpite?\033[m'))
    elif resp < ns:
        resp = int(input('\033[1;91mO número que pensei é maior, e ai, qual teu palpite?\033[m'))
    cont += 1
if resp == ns:
    print('\033[1;32mPárabens você acertou em {} tentativas!\033[m'.format(cont + 1))

