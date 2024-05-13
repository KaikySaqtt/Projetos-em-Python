def notas(*n, sit = False):
    r = dict()
    nume = list(n)
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r['média'] = sum(n)/len(n)

    if sit == True:
        if r['média'] >= 7:
            r["situação"] = "boa"
        elif r['média'] >= 5:
            r["situação"] = "razoavel"
        else:
            r["situação"] = "ruim"
    return r


nu = notas(5.3, 3.2, 5.1, 2.5, sit = True)
print(nu)


