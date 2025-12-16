import geometria

figuras = [
    geometria.Rectangulo(4, 5),
    geometria.Triangulo(6, 4, 5, 3),
    geometria.Circulo(3)
]

for figura in figuras:
    print(type(figura).__name__)
    figura.mostrar_datos()