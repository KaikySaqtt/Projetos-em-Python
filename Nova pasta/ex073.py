times = ('Botafogo', 'Flamengo', 'Gremio', 'São Paulo', 'Fluminense', 'Palmeiras', 'RB-Bragantino', 'Athletico-PR', 'Fortaleza', 'Cruzeiro', 'Internacional', 'Atlético-MG', 'Cuiabá', 'Santos', 'Bahia', 'Goiás', 'Coritiba', 'Vasco da Gama', 'América-MG')
print('=-' * 120)
co = 0
ca = 0
cr = 0
print('Essa é a tabela do brasileirão', end=': ')
for c in times:
    if co < 18:
        print(c, end=', ')
    else:
        print(c)
    co += 1
print('=-' * 120)

print('Os primeros são', end=': ')
for f in range(0, 5):
    if ca < 5:
        print((times[f]), end=', ')
    else:
        print(times[f])
    ca += 1
print('')
print('=-' * 120)
print('Os quatro ultimo são', end=': ')
for g in range(-4, 0):
    if cr < 3:
        print((times[g]), end=', ')
    else:
        print(times[g])
    cr += 1
print('')
print('=-' * 120)
print('Em ordem alfabética fica: ', sorted(times))

print('=-' * 120)
print(f'O {times[5]} está na sexta posição! e eu n gosto disso!')
