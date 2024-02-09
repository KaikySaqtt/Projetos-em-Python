dados = []
resp = ""
while True:
    dado = []
    nome = str(input("Nome:"))
    dado.append(nome)
    nota = int(input("Nota 1:"))
    dado.append(nota)
    notad = int(input("Nota 2:"))
    dado.append(notad)
    m = (nota + notad) / 2
    dado.append(m)
    dados.append(dado.copy())
    dado.clear()
    resp = str(input("Quer continuar? [S/N]"))
    if resp.lower() == "n":
        break

print("No. NOME    MÉDIA")
print("-------------------")
for c, dado in enumerate(dados):
     print(f"{c} {dado[0]} {dado[3]}")
while True:
    aluno = int(input("Mostrar as notas de qual aluno?(999 encerra o programa)"))
    if aluno == 999:
        break
    else:
        print(f"as notas de {dados[aluno] [0]} são {dados[aluno] [1]} e {dados[aluno] [2]}")
print("<<<< VOLTE SEMPRE >>>>")
