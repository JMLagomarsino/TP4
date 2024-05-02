a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
x1 = float(input("Ingrese el coeficiente x1: "))
x2 = float(input("Ingrese el coeficiente x2: "))

print(f"\nEl coeficiente a de su ecuación de la recta es: {a}")
print(f"El coeficiente b de su ecuación de la recta es: {b}")
print(f"El coeficiente x1 de su ecuación de la recta es: {x1}")
print(f"El coeficiente x2 de su ecuación de la recta es: {x2}")

y1 = a * x1 + b
y2 = a * x2 + b

print(f"\nPara la siguiente ecuación:y = {a}x + {b}")


print(f"\nDados los siguientes puntos:")
print(f"p1 ({x1}, {y1})")
print(f"P2 ({x2}, {y2})")

distancia = (y2 - y1)
print(f"\nLa distancia entre ellos es: {distancia}")