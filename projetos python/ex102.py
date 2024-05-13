import math

def fatorial(c, s):
    c = n1
    if s == "S":
        print('{}! = {}X'.format(n1, n1), end= "")
        while c > 1:
            c -= 1
            print(c, end='')
            if c > 1:
                print('X', end='')
    f = math.factorial(n1)
    print(f)

n1 = int(input('Me fale de qual número você quer calcular o fatorial: '))
p = str(input("Quer q mostre a conta[S/N]: ")).upper()
fatorial(n1, p)
