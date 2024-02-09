n1 = float(input('fale a medida em metros: '))
print('A medida de {}m corresponde a:'.format(n1))
dam = n1 / 10
hm = dam / 10
km = hm / 10
dm = int(n1) * 10
cm = dm * 10
mm = cm * 10

print('{}km \n{}hm\n{}dam\n{}dm\n{}cm\n{}mm '.format(km, hm, dam, dm, cm, mm))

