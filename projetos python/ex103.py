
def jogador(nome= "<desconhecido>", gols=0):
    if type(gols) == str:
        gols = 0
    if nome =="":
        nome = "<desconhecido>"
    print(f"o jogador {nome} fez {gols} gol(s)")


name = str(input("Qual nome do jogador? "))
gol = input("quantos gols ele fez? ")

jogador(name, gol)
