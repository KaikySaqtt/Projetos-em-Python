matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
c = 0
maior = 0
pares = 0
terceira = 0
maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l] [c] = int(input(f"fale o valor de ({l}, {c})"))
        if c == 2:
            terceira += matriz [l] [c]
        if l == 1:
            if matriz [l] [c] > maior:
                maior = matriz [l] [c]
        if matriz [l] [c] % 2 == 0:
            pares += matriz [l] [c]

for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print("")
print(f"A soma de todos os pares foi {pares}")
print(f"A soma dos valores da terceira coluna foi {terceira}")
print(f"O maior número da segunda linha foi {maior}")
