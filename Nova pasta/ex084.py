nomes = list()
dados = list()
nomegordo = list()
nomemagro = list()
nome = str
pme = float
pm = float
pm = 0.0
pme = 0
cont = 0
while True:
    nome = input('Nome: ')
    dados.append(nome)
    peso = float(input('Peso: '))
    dados.append(peso)
    nomes.append(dados[:])
    dados.clear()
    if peso >= pm:
        if peso == pm:
            nomegordo.append(nome)
        else:
            pm = peso
            nomegordo.clear()
            nomegordo.append(nome)
    if cont == 0:
        pme = peso
        nomemagro.clear()
        nomemagro.append(nome)
    if peso <= pme:
        if peso == pme:
            nomemagro.append(nome)
        else:
            pme = peso
            nomemagro.clear()
            nomemagro.append(nome)

    cont += 1
    resp = input('Quer continuar?')
    if resp == 'n' or resp == 'não':
        break
print(f'Você registrou {cont} pessoas')
print(f"O maior peso foi {pm} o de {nomegordo}")
print(f"O menor peso foi {pme} o de {nomemagro}")

