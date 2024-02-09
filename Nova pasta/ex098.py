from time import sleep
def linha():
    print("=-" * 20)
def cont(x, y, z):
    if z < 0:
        z *= -1
    elif z == 0:
        z = 1
        print("irei fazer de um em um pois vc deu 0.")
    if x > y:
        while x > y - z:
            print(x, end=" ")
            sleep(0.5)
            x = x - z
        print("fim")
    elif x < y:
        while x < y + z:
            print(x, end=" ")
            sleep(0.5)
            x = x + z
        print("fim")
    else:
        print("não coloque número iguais")

linha()
print("Contagem de 1 a 10 de um em um ")
cont(1, 10, 1)
linha()
print("Contagem de 10 a 0 de dois em dois ")
cont(10, 0, 2)
print("Agora é sua vez de fazer sua contagem")
i = int(input("Iníco: "))
f = int(input("Final: "))
d = int(input("De quanto em quanto: "))
print(f"Contagem de {i} até {f} de {d} em {d}")
cont(i, f, d)

