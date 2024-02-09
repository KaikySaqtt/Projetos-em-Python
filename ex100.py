from random import randint
def sorteio(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))

    print("Sorteando 5 valores da lista ", end="")
    for c in lista:
        print(c, end=" ")
    print("PRONTO!")
def sp(x):
    ps = 0
    for c in x:
        if c % 2 == 0:
            ps += c
    print("Somando os valores pares de ", end="")
    for c in x:
        print(c, end=" ")
    print(f"temos {ps}")
num = list()
sorteio(num)
sp(num)

