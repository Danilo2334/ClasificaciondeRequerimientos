class Calculadora:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2


if __name__ == "__main__":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    calculadora = Calculadora(num1, num2)

    print("Suma:", calculadora.suma())
    print("Resta:", calculadora.resta())
    print("Multiplicación:", calculadora.multiplicacion())
    print("División:", calculadora.division())
