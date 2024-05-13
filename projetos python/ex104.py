def isint(nn):
    valor = 0
    ok = False
    while True:
        n = str(input(nn))
        if n.isnumeric():
          valor = int(n)
          ok = True
        else:
            print("\033[0;31m ERRO, número invalido, digite um valido\033[m")
        if ok == True:
            break
    return valor


num = isint('digite um numero')
print(f"o número digitado foi {num}")