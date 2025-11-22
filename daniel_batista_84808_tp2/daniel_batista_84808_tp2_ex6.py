lado1 = float(input("Introduza o comprimento do primeiro lado: "))
lado2 = float(input("Introduza o comprimento do segundo lado: "))

area = lado1 * lado2

print(f"Área = {area:.2f}")

if lado1 == lado2:
    print("É um quadrado")
else:
    print("É um retângulo")
