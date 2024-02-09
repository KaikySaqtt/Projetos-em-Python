frase = input('Me diga uma frase').upper()
pal = frase.split()
junto = ''.join(pal)
t = len(junto)
inv = ''
for c in range(t - 1, -1, -1):
    inv += junto[c]
print('O inverso de {} é {}'.format(junto, inv))
if junto == inv:
    print('É um palindromo')
else:
    print('Não é um palindromo')