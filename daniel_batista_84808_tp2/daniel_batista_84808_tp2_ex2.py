import random
import math

a = random.randint(0,10)
b = random.randint(5,20)
c = random.randint(5,20)

if a == 0:
    print("Não existem equações de 2ª grau para a=0")
else:
    raiz = b**2-4*a*c
    if raiz < 0:
        print("Não existem raízes reais.")
    else:
        x1 = -b + math.sqrt((b**2-4*a*c)) / (2*a)
        x2 = -b - math.sqrt((b**2-4*a*c)) / (2*a)
        print(f"Os valores de x são: X1={x1:.2f} X2={x2:.2f}")
