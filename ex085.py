
numeros = [[], []]
for c in range(1, 8):
    resp = int(input(f'Fale o {c}o numero'))
    if resp%2 == 0:
        numeros[0].append(resp)
    else:
        numeros[1].append(resp)
ordemi = sorted(numeros[1])
ordemp = sorted(numeros[0])
print(f"Valores impares foram {ordemi}")
print(f"Valores pares foram {ordemp}")
