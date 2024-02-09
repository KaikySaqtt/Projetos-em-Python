print('=' * 20)
print('     \033[1;32m10 TERMOS DE UMA PA\033[m     ')
print('=' * 20)
pm = int(input('Me diga seu primeiro termo: '))
rz = int(input('Me diga a sua razão: '))
d = (rz * 10) + pm
for s in range(pm, d, rz):
     print(s, end=' ->')
print('Acabou')

