from time import sleep
def maior(*num):
    print("=-" * 20)
    print("analisando os valores passados...")
    sleep(3)
    print(f"{num} foram os valores informados {len(num)} números")
    sleep(0.8)
    maior = 0
    for c in num:
        if c > maior:
            maior = c
    print(f"O maior valor foi {maior}")
maior(3, 4, 2, 0, 2)
maior(1, 0, 4, 6, 2)
maior(1, 5)
maior(1)



