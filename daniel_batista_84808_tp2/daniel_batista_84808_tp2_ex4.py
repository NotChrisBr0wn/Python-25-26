#p = 2pi*R A = pi * r^2
import math

raio = float(input("Introduza o valor do raio da circunferência: "))

perimetro = 2*math.pi*raio
area = math.pi*(raio)**2

print(f"Perímetro circunferência={perimetro:.2f} | Area circunferência={area:.2f}")