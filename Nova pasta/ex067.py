while True:
    print('=' * 24)
    tab = int(input('Quer ver a tabuada de qual valor: '))
    if tab < 0:
        break
    for i in range(1, 11):
        vezes = tab * i
        print(f'{tab} X {i} = {vezes}')
