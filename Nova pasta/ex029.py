vel = int(input('qual sua velocidade? '))
if vel >= 80:
    print('Meu deus quanta velocidade')
    print('O máximo era de 80Km por hora')
    multa = (vel - 80) * 7
    print('Agora voce irar receber uma multa de {}R$'.format(multa))
print('Tenha um ótimo dia e dirija com segurança')