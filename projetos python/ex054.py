conm = 0
conme = 0
for c in range(1, 8, 1):
    nas = int(input('em que ano a {}° pessoa nasceu'.format(c)))
    idade = 2023 - nas
    if idade>17:
        conm += 1
    else:
        conme += 1
print('Temos {} pessoas maiores de idade'.format(conm))
print('Temos também {} pessoas que são menores de idade'.format(conme))
