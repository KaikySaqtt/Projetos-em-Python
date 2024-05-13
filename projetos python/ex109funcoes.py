def metade(n, f):
    if f is True:
        print(f'O metade de R${moedas(n)} é R${moedas(n/2)}')
    else:
        print(f'O metade de n é {(n / 2)}')

def dobro(n, f):
    if f is True:
        print(f'O dobro de R${moedas(n)} é R${moedas(n*2)}')
    else:
        print(f'O dobro de {n} é {(n * 2)}')
def porcen(n, f):
    if f is True:
        print(f'10% de R${moedas(n)} é R${moedas(n/10)}')
    else:
        print(f'10% de {n} é {(n / 10)}')

def moedas(n = 0):
    return f"{n:.2f}".replace('.',  ',')
