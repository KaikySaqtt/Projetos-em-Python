import math
a = float(input('Digite o seu angulo'))
ca = math.radians(a)
con = math.cos(ca)
tan = math.tan(ca)
sen = math.sin(ca)
print('Seus {} graus tem como coseno: {:.2f}'.format(a, con))
print(("como tangente: {:.2f}".format(tan)))
print('E como seno: {:.2f}'.format(sen))
