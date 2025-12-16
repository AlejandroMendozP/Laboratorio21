import math

class Figura:
    def area(self):
        pass

    def perimetro(self):
        pass

    def mostrar_datos(self):
        print(f"Área: {self.area():.2f}")
        print(f"Perímetro: {self.perimetro():.2f}")

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.altura = altura

    def area(self):
        return (self.lado1 * self.altura) / 2

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio