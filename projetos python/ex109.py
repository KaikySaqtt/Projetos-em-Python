import ex109funcoes

num = float(input("Digite o preço: "))
formate = input("Quer formatado? [S/N]").upper()
if formate == "S":
    formate = True
else:
    formate = False
ex109funcoes.metade(num, formate)
ex109funcoes.dobro(num, formate)
ex109funcoes.porcen(num, formate)