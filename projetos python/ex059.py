import time
n1 = int(input('Fale o primeiro número: '))
n2 = int(input('Fale o segundo númeoro: '))
resp = 1
while resp != 5:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos número')
    print('[5] Sair')
    print('=== Qual tua opção? ===')
    resp = int(input(''))
    if resp == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))
        print('=' * 20)
        time.sleep(3)
    elif resp == 2:
        m = n1 * n2
        print('{} X {} = {}'.format(n1, n2, m))
        print('=' * 20)
        time.sleep(3)
    elif resp == 3:
        if n1 > n2:
            print('O {} é maior do que o {}'.format(n1, n2))
        elif n2 > n1:
            print('O {} é maior do que o {}'.format(n2, n1))
        else:
            print('Os números são iguais!')
        print('=' * 20)
        time.sleep(3)
    elif resp == 4:
        n1 = int(input('Fale o primeiro número: '))
        n2 = int(input('Fale o segundo númeoro: '))
    elif resp > 5:
        print('Sua opção é invalida, por favor tente de novo')
        print('=' * 20)
        time.sleep(3)
print('Agradeço pelo uso!')
