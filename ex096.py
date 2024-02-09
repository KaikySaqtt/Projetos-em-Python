def area(x, y):
    area = x * y
    print(f"o seu terreno de {x}m² por {y}m² tem uma área de {area}m²")
print("-" * 19)
print(" Controle de terreno ")
print("-" * 19)
lg = float(input("largura em metros: "))
cp = float(input("Comprimento em metros: "))
area(lg, cp)