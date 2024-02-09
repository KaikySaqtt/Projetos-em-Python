dados = dict()
cont = 1
gols = list()
geral = list()
total = 0
c = 0
while True:
    dados.clear()
    dados["nome"] = input("Qual nome do jogador: ")
    partis = int(input(f"Quantas partidas {dados['nome']} jogou: "))
    for c in range(0, partis):
        gol = int(input(f"Quantos gols ele fez na {c + 1} partida: "))
        gols.append(gol)
        total += gol
    dados['gols'] = gols.copy()
    dados['total'] = total
    gols.clear()
    total = 0
    c = 0

    resp = input("quer continuar? ").lower()
    geral.append(dados.copy())
    if resp == "n":
        break
    elif resp == "s":
        cont += 1
    else:
        print("letra n identificada, entenderei como sim.")
print("=-" * 40)
print("-------------------------------------")

for d in range(0, len(geral)):
    print(f"Cod:{d} Nome:{geral[d]['nome']: ^1} gols:{geral[d]['gols']} total:{geral[d]['total']}")
print("-------------------------------------")
while True:
    jogador = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if jogador == 999:
        break
    print(f"-- Levantamento do jogador {geral[jogador]['nome']}")
    g: int = 1
    for f in geral[jogador]['gols']:
        print(f"na partida {g} fez {f} gols")
        g += 1
    g = 1

