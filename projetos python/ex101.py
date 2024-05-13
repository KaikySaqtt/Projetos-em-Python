def voto(an):
    aa = 2024
    idade: int = (an - aa) * -1
    if idade < 16:
        print(f"com {idade} anos o voto é proibido.")
    elif idade < 18 or idade > 65:
        print(f"com {idade} anos o voto é opcional.")
    else:
        print(f"com {idade} anos o voto é obrigatório.")

x = int(input("qual ano de seu nascimento: "))
voto(x)
