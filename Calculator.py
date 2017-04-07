class Calculator:
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

    def get_term_from_numbers(self, number1, operator, number2, delete: bool):

        if number1 is None:
            string = ""

        else:
            string = str(number1)

            if operator is None:
                pass

            else:
                string += " "
                string += operator

                if number2 is None:
                    pass

                else:
                    result = self.calculate(number1, number2, operator)
                    string += str(number2)
                    string += " = "
                    string += result

        return string


calculator = Calculator()
assert 8 == calculator.calculate(3, 5, "+")
assert -2 == calculator.calculate(3, 5, "-")
assert 15 == calculator.calculate(3, 5, "*")
assert 0.6 == calculator.calculate(3, 5, "/")

if __name__ == "__main__":
    print("Please run Main.")
