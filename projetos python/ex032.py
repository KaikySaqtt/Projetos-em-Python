from datetime import datetime
ano = int(input('Fale um ano e direi se ele é bissexto, e se quiser ver o atual digite 0 '))
data = datetime.now()
anoatual = data.year
if ano == 0:
    ano = datetime.today().year

if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('Seu ano {} é bissexto'.format(ano))
else:
    print('Seu ano {} não é bissexto'.format(ano))



