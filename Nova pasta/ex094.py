galera = list()
pessoa = dict()
mulheres = list()
soma = 0
while True:
    pessoa.clear()
    pessoa["nome"] = str(input("Nome:"))
    while True:
        pessoa["sexo"] = str(input("Sexo: [M/F]")).upper()[0]
        if pessoa["sexo"] == "F":
            mulheres.append(pessoa["nome"])
        if pessoa["sexo"] in 'MF':
            break
        print('ERRO! Coloque M ou F.')
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input("Quer continuar? [N/S]")).upper()[0]
        if resp in 'NS':
            break
        print("ERRO responda só S e N.")
    if resp == 'N':
        break
print(f"A) Ao todo temos {len(galera)} pessoas cadastradas.")
media = soma / len(galera)
print(f'B) A media de idade é {media:.2f}')
print(f'C) A mulheres são : ', end="")
for p in mulheres:
    print(p, end =" ")
print("")
print("D) Lista de pessoas com idade acima da média: ", end="")
for p in galera:
    if p['idade'] >= media:
        print("    ")
        for k, v in p.items():
            print(f'{k} = {v}; ', end="")
print()
print("<<< ENCERRADO >>>")