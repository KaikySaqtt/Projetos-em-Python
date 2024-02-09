valores = list()
maiores = [0]
menores = [0]
maior = 0
menor = 1000000
cont = 0
contm = 0
for c in range(0, 5):
    valores.append(int(input(f'Coloque um valor na posição {c}: ')))
print('=-' * 40)
print(f'Você digitou os valores {valores}')
for v in range(len(valores)):
    if valores[v] >= maior:
        maior = valores[v]
    if valores[v] <= menor:
        menor = valores[v]
y = valores.count(maior)
for e in range(0, 5):
    if maior == valores[e]:
        maiores.append(cont)
    cont += 1
maiores.remove(0)
for w in range(0, 5):
    if menor == valores[w]:
        menores.append(contm)
    contm += 1
menores.remove(0)
print(f'O maior valor digitado foi {maior} e aparece nas posições ', end='')
for d in maiores:
    print(f'{d}... ', end='')
print()
print(f'E o menor valor foi {menor} e aparece nas posições ', end='')
for p in menores:
    print(f'{p}... ', end='')
