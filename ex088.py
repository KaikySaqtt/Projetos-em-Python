print("-" * 40)
print("          JOGO MEGA SENA")
print("-" * 40)
virgem = []
jogos = list()
import time
import random
vezes = int(input("Quantos jogos você quer "))
ale: int= random.randint(0, 60)
print(f"=-=-=-=-=- Sorteando {vezes} jogos =-=-=-=-=-")
for c in range(0, vezes):
    for i in range(0, 6):
        virgem.append(ale)
        ale: int = random.randint(0, 60)
    jogos.append(virgem[:])
    virgem.clear()
tam = len(jogos)
for d in range(0, tam):
    print(f"Jogo {d + 1}: {jogos[d]} ")
    time.sleep(0.5)
print("-=-= BOA SORTE -=-=")
