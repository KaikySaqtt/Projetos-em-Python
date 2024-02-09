aluno = dict()
aluno['nome'] = input("Nome: ")
aluno['média'] = int(input('Média: '))

if aluno["média"] < 5:
    aluno['aprov'] = "Reprovado"
elif aluno['média'] < 7:
    aluno['aprov'] = "Recuperação"
else:
    aluno['aprov'] = "Aprovado"
print(f'Nome do aluno: {aluno["nome"]}')
print(f'A média de {aluno["nome"]} foi {aluno["média"]}')
print(f'ele foi {aluno["aprov"]}')
