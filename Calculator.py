class Calculator:
    def calculate(self, value1: int, value2: int, operator: str) -> str:
        if operator == "+":
            return str(value1 + value2)
        elif operator == "-":
            return str(value1 - value2)
        elif operator == "*":
            return str(value1 * value2)
        elif operator == "/":
            if value2 > 0:
                result = value1 / value2 * 100
                result = int(result)
                result = result / 100
                return str(result)
            else:
                return "Error"
        else:
            raise RuntimeError("Wrong calculator operator")

    def get_term_from_numbers(self, number1, operator, number2) -> str:

        if number1 is None:
            string = ""

        else:
            string = str(number1)

            if operator is None:
                pass

            else:
                string += " "
                string += operator
                string += " "

                if number2 is None:
                    pass

                else:
                    result = self.calculate(number1, number2, operator)
                    string += str(number2)
                    string += " = "
                    string += result

        return string
