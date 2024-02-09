itens = ('Lapiz', 'Caneta', 'Jóia', 'Batom', 'Mouse', 'Boneco')
preços = (1.90, 2.00, 250.90, 2.00, 38.89, 34.76)
print('-' * 40)
print('         Listagem de preço       ')
print('-' * 40)
cont = 0
for c in itens:
    print(f'{c:.<30}R${preços[cont]:.2f}')
    cont +=1
print('-' * 40)