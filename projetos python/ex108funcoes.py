def metade(n):
    print(f'O metade de R${moedas(n)} é R${moedas(n/2)}')


def dobro(n):
    print(f'O dobro de R${moedas(n)} é R${moedas(n*2)}')


def porcen(n):
    print(f'10% de R${moedas(n)} é R${moedas(n/10)}')


def moedas(n = 0):
    return f"{n:.2f}".replace('.',  ',')
