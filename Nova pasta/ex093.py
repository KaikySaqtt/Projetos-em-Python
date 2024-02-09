dados = dict()
dados["nome"] = input("Qual nome do jogador: ")
partis = int(input(f"Quantas partidas {dados['nome']} jogou: "))
cont = 1
gols = list()
total = 0
while True:
    gol = int(input(f"Quantos gols ele fez na {cont} partida: "))
    gols.append(gol)
    total += gol
    if cont == partis:
        break
    cont += 1
dados["gols"] = gols
dados["total"] = total
print(len(gols))
print("=-" * 40)
print(dados)
print("=-" * 40)
for c, d in dados.items():
    print(f"o campo {c} tem valor {d}")
print(f"o jogador {dados['nome']} jogou {partis} partidas")
contd = 1
while True:
    print(f"=> na partida {contd} ele fez {gols[contd - 1]} gols")
    if contd == len(gols):
        break
    contd += 1
print(f"totalizando {dados['total']} gols")
