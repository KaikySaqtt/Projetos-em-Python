n1 = int(input('Fale o numero da tabuada: '))
print('=' * 20)
v = 0
for i in range(10):
    v = v + 1
    print('{} X {} = {}'.format(n1, v, n1 * v))
print('=' * 20)

