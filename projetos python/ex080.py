valores = []
maior = 0
menor = 100000
for e in range(0, 5):
    i = int(input('Digite um valor:'))
    if e == 0:
        valores.append(i)
        menor = i
        maior = i
        print('Valor adicionado no final da lista')
    elif i < menor:
        menor = i
        valores.insert(0, menor)
        print('Valor adicionado na posição 0')
    elif i > maior:
        maior = i
        valores.append(maior)
        print('Valor adicionado no final da lista')
    elif (i > menor) and (i < maior):
        if len(valores ) > 2:
            if i > valores[2]:
                valores.insert(3, i)
                print('Valor adicionado na posição 3')
            elif i > valores[1]:
              valores.insert(2, i)
              print('Valor adicionado na posição 2')
            elif i > menor:
                valores.insert(1, i)
                print('Valor adicionado na posição 1')

        else :
            valores.insert(1, i)
            print('Valor adicionado na posição 1')
print(f'Essa é sua lista sem valores repitidos: {valores}')