class Rechner():

    def addieren(self, zahl1, zahl2):
        return zahl1 + zahl2

    def subtrahieren(self, zahl1, zahl2):
        return zahl1 - zahl2

    def multiplizieren(self, zahl1, zahl2):
        return zahl1 * zahl2

    def dividieren(self, zahl1, zahl2):
        return zahl1 / zahl2

    def potenzieren(self, zahl1, zahl2):
        return zahl1 ** zahl2

    def dividieren_ohne_rest(self, zahl1, zahl2):
        return zahl1 // zahl2

    def modulo(self, zahl1, zahl2):
        return zahl1 % zahl2

    def rechne(self, zahl1, zahl2, rechenzeichen=None, rechencode=None):
        if rechenzeichen is not None:
            if rechenzeichen == "+":
                return self.addieren(zahl1, zahl2)
            elif rechenzeichen == "-":
                return self.subtrahieren(zahl1, zahl2)
            elif rechenzeichen == "*":
                return self.multiplizieren(zahl1, zahl2)
            elif rechenzeichen == "/":
                return self.dividieren(zahl1, zahl2)
            elif rechenzeichen == "**":
                return self.potenzieren(zahl1, zahl2)
            elif rechenzeichen == "//":
                return self.dividieren_ohne_rest(zahl1, zahl2)
            elif rechenzeichen == "%":
                return self.modulo(zahl1, zahl2)
        elif rechencode is not None:
            if rechencode == 0:
                return self.addieren(zahl1, zahl2)
            elif rechencode == 1:
                return self.subtrahieren(zahl1, zahl2)
            elif rechencode == 2:
                return self.multiplizieren(zahl1, zahl2)
            elif rechencode == 3:
                return self.dividieren(zahl1, zahl2)
            elif rechencode == 4:
                return self.potenzieren(zahl1, zahl2)
            elif rechencode == 5:
                return self.dividieren_ohne_rest(zahl1, zahl2)
            elif rechencode == 6:
                return self.modulo(zahl1, zahl2)
        else:
            return "Fehler"


rechner = Rechner()
print(rechner.addieren(3, 5))
print(rechner.subtrahieren(3, 5))
print(rechner.multiplizieren(3, 5))
print(rechner.dividieren(16, 3))
print(rechner.potenzieren(2, 10))
print(rechner.dividieren_ohne_rest(16, 3))
print(rechner.modulo(16, 3))
print(rechner.rechne(3, 5, "+"))
print(rechner.rechne(3, 5, "-"))
print(rechner.rechne(3, 5, "*"))
print(rechner.rechne(3, 5, "/"))
print(rechner.rechne(3, 5, "**"))
print(rechner.rechne(3, 5, "//"))
print(rechner.rechne(3, 5, "%"))
print(rechner.rechne(3, 5, None, 0))
print(rechner.rechne(3, 5, None, 1))
print(rechner.rechne(3, 5, None, 2))
print(rechner.rechne(3, 5, None, 3))
print(rechner.rechne(3, 5, None, 4))
print(rechner.rechne(3, 5, None, 5))
print(rechner.rechne(3, 5, None, 6))

