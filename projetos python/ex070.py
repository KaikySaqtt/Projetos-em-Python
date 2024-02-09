print('=-' * 40)
print('LOJA SUPER BARATÃO!')
print('=-' * 40)
np = ''
pcm = 0
mb = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
soma = float(0)
while True:
    nom = input('Nome do produto: ')
    preço = float(input('Preço: '))
    if preço > 1000.00:
        pcm += 1
    if preço < mb:
        mb = preço
        np = nom
    soma += preço
    resp = input('Quer continuar?: [N/S]').upper()
    if resp != 'S':
        break
print(f'O total da compra foi R${soma}')
print(f'Temos {pcm} produtos que custaram a cima de R$1000.00')
print(f'O produto mais barato foi {np} que custou R${mb}')

