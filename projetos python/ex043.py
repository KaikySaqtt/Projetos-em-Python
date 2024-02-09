peso = float(input('Fale me seu peso em kg: '))
alt = float(input('Fale me sua altura: '))
imc = peso / pow(alt, 2)
print('com o peso de {}KG e altura de {}m seu IMC é {:.2f}'.format(peso, alt, imc))
if imc < 18.6:
    print('Você está abaixo do peso')
elif imc <= 25:
    print('Você está com o peso ideal')
elif imc <= 30:
    print('Você está com sobrepeso')
elif imc <= 40:
    print('Você está com obesidade')
else:
    print('Você tem obesidade mórbida')
