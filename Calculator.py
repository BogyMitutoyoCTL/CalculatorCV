class Calculator():
    def calculate(self, value1, value2, operator):
        if operator == "+":
            return value1 + value2
        elif operator == "-":
            return value1 - value2
        elif operator == "*":
            return value1 * value2
        elif operator == "/":
            return value1 / value2
        else:
            raise RuntimeError("Wrong calculator operator")


calculator = Calculator()
assert 8 == calculator.calculate(3, 5, "+")
assert -2 == calculator.calculate(3, 5, "-")
assert 15 == calculator.calculate(3, 5, "*")
assert 0.6 == calculator.calculate(3, 5, "/")

if __name__ == "__main__":
    print("Please run Main.")
