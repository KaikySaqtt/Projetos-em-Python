
def resumo(nu, a, r):
    print("-" * 20)
    print("       RESUMO       ")
    print("-" * 20)
    metade(nu)
    dobro(nu)
    porcen(nu)
    aument(nu, a)
    reduc(nu, r)
def metade(n):
    print(f'O metade de R${moedas(n)} é R${moedas(n / 2)}')

def dobro(n):
    print(f'O dobro de R${moedas(n)} é R${moedas(n * 2)}')

def porcen(n):
    print(f'10% de R${moedas(n)} é R${moedas(n / 10)}')

def aument(n, au):
    print(f'Com {au}% de aumento de R${moedas(n)} vai para R${moedas(n +((n *au)/100))}')

def reduc(n, re):
    print(f'Com {re}% de desconto de R${moedas(n)} vai para R${moedas(n -((n *re)/100))}')
def moedas(n=0):
    return f"{n:.2f}".replace('.', ',')