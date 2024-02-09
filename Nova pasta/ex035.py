print('=-=' * 20)
print('Analisador de Triangulos')
print('=-=' * 20)
s1 = int(input('Fale o primeiro segmento'))
s2 = int(input('Fale o segundo segmento'))
s3 = int(input('Fale o terceiro segmento'))
if s1 + s2 > s3:
    print('Sim é possivel forma um triangulo')
else:
    print('Não é possivel formar um triangulo')
