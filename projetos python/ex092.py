from datetime import datetime
ano = int(datetime.now().year)
dados = dict()
dados["nome"] = input("Nome: ")
dados["AN"] = int(input("Ano de nascimento: "))
dados["CT"] = int(input("Carteira de trabalho: "))
dados["idade"] = ano - dados["AN"]
vdd = False
if dados["CT"] > 0:
    dados["AC"] = int(input("Ano da contratação: "))
    dados["salario"] = int(input("salário: "))
    dados["AP"] = (dados["idade"] + dados["AC"] + 35) - ano
    vdd = True
print("=*" * 40)
print(f"O nome é: {dados['nome']}")
print(f"O a idade é: {dados['idade']}")
print(f"O ctps tem o valor: {dados['CT']}")
if vdd == True:
    print(f"Foi contratado em {dados['AC']}")
    print(f"Foi salário é {dados['salario']}")
    if dados['idade'] > dados["AP"]:
        print(f"Se aposentou com {dados['AP']} anos")
    else:
        print(f"Vai se aposentar com {dados['AP']} anos")
print("=*" * 40)