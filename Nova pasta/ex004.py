v = input("fale algo")
print('o tipo primitivo dele é {}'.format(type(v)))
print('só tem espaços?: {}'.format(v.isspace()))
print('é um numero?: {}'.format(v.isnumeric()))
print('é do alfabeto?: {}'.format(v.isalpha()))
print('é alfanumérico?: {}'.format(v.isalnum()))
print('esta em maisuclo?: {}'.format(v.isupper()))
print('está em minusculas?: {}'.format(v.islower()))
print('está capitalizado?: {}'.format(v.istitle()))