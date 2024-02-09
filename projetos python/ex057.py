n = str(input('Me fale seu sexo ')).strip().upper()[0]
while n not in 'MmFm':
    n = str(input('Sexo ainda não registrado em meu sistema, informe ou masculino ou feminino!')).strip().upper()[0]
if n == 'M' or n == 'F':
    if n == 'M':
        print('Seu sexo é masculino, foi registrado em nosso sistema!')
    else:
        print('Seu sexo é femino, foi registrado em nosso sistema!')
