f = 0
nomes = ('PYTHON', 'MOUSE', 'CELULAR', 'ESTUDAR', 'DECLINIO', 'ARLONG', 'PLANTA')
for c in nomes:
    print(f'Na palavra {c} temos de vogal: ', end='')
    for f in range(0, len(c)):
        if c[f] == 'A':
            print('a', end=' ')
        if c[f] == 'E':
            print('e', end=' ')
        if c[f] == 'I':
            print('i', end=' ')
        if c[f] == 'O':
            print('o', end=' ')
        if c[f] == 'U':
            print('u', end=' ')
    print()
