num = int(input("Introduza o primeiro valor: "))
num2 = int(input("Introduza o segundo valor: "))
num3 = int(input("Introduza o terceiro valor: "))

if num > num2 and num > num3:
    maximo = num
elif num2 >= num and num2 >= num3:
    maximo = num2
else:
    maximo = num3

print(f"O valor máximo entre os 3 é: {maximo}")