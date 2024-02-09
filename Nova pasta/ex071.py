print('-=' * 40)
print('Banco cacique')
print('-=' * 40)
cont = 0
cvs = 0
vvs = 0
cv = 0
dv = 0
cvc = 0
ddv = 0
uv = 0
while True:
    vs = int(input('Me fale quanto voce quer sacar: '))
    while True:
        if vs > cvs * 50:
            cvs += 1
        else:
            break
    if vs - cvs * 50 < 0:
        cvs += - 1
    vs = vs - cvs * 50
    if vs >= 20:
        while True:
            if vvs * 20 <= vs:
                vvs += 1
                cont += 1
            else:
                break
    if vs - vvs * 20 < 0:
        vvs += -1
    vs = vs - vvs * 20
    if vs >= 10:
        while True:
            if dv * 10 <= vs:
                dv += 1
            else:
                break
    if vs - dv * 10 < 0:
        dv += -1
    vs = vs - dv * 10
    if vs >= 5:
        while True:
            if cvc * 5 <= vs:
                cvc += 1
            else:
                break
    if vs - cvc * 5 < 0:
        cvc += -1
    vs = vs - cvc * 5
    if vs >= 2:
        while True:
            if ddv * 2 <= vs:
                ddv += 1
            else:
                break
    if vs - ddv * 2 < 0:
        ddv += -1
    if vs == 1:
        uv = 1
    if cvs > 0:
        print(f'Total de notas de R$50 foi {cvs}')
    if vvs > 0:
        print(f'Total de notas de R$20 foi {vvs}')
    if dv > 0:
        print(f'Total de notas de R$10 foi {dv}')
    if cvc > 0:
        print(f'Total de notas de R$5 foi {cvc}')
    if ddv > 0:
        print(f'Total de notas de 2R$ foi {ddv}')
    if uv > 0:
        print(f'Total de moedas de R$1 foi de {uv} ')
    break

