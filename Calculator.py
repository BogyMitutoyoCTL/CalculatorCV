class Calculator():

    def add(self, zahl1, zahl2):
        return zahl1 + zahl2

    def subtract(self, zahl1, zahl2):
        return zahl1 - zahl2

    def multiply(self, zahl1, zahl2):
        return zahl1 * zahl2

    def divide(self, zahl1, zahl2):
        return zahl1 / zahl2

    def calculate(self, zahl1, zahl2, operator):
        if operator == "+":
            return self.add(zahl1, zahl2)
        elif operator == "-":
            return self.subtract(zahl1, zahl2)
        elif operator == "*":
            return self.multiply(zahl1, zahl2)
        elif operator == "/":
            return self.divide(zahl1, zahl2)
        else:
            raise RuntimeError("Wrong calculator operator")


calculator = Calculator()
assert 8 == calculator.add(3, 5)
assert -2 == calculator.subtract(3, 5)
assert 15 == calculator.multiply(3, 5)
assert 16/3 == calculator.divide(16, 3)
assert 8 == calculator.calculate(3, 5, "+")
assert -2 == calculator.calculate(3, 5, "-")
assert 15 == calculator.calculate(3, 5, "*")
assert 0.6 == calculator.calculate(3, 5, "/")

if __name__ == "__main__":
    print("Please run Main.")
