s1 = int(input('Me diga seu primeiro segmento'))
s2 = int(input('Me diga seu segundo segmento'))
s3 = int(input('Me diga seu terceiro segmento'))
if s3 > (s2 + s1):
    print('Você não pode formar um triangulo')
elif s1 == s2 and s1 == s3:
    print('Você pode formar um triangulo, e ele será um triangulo equilátero')
elif s1 == s2 and s1 != s3 or s3 == s1 and s3 != s2 or s2 == s3 and s2 != s1:
    print('Você pode formar um triangulo, e ele será um triangulo isóceles')
else:
    print('Você pode formar um triangulo, e ele será escaleno')

