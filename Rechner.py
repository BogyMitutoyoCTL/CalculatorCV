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
assert 8 == rechner.addieren(3, 5)
assert -2 == rechner.subtrahieren(3, 5)
assert 15 == rechner.multiplizieren(3, 5)
assert 16/3 == rechner.dividieren(16, 3)
assert 1024 == rechner.potenzieren(2, 10)
assert 5 == rechner.dividieren_ohne_rest(16, 3)
assert 1 == rechner.modulo(16, 3)
assert 8 == rechner.rechne(3, 5, "+")
assert -2 == rechner.rechne(3, 5, "-")
assert 15 == rechner.rechne(3, 5, "*")
assert 0.6 == rechner.rechne(3, 5, "/")
assert 243 == rechner.rechne(3, 5, "**")
assert 0 == rechner.rechne(3, 5, "//")
assert 3 == rechner.rechne(3, 5, "%")
assert 8 == rechner.rechne(3, 5, None, 0)
assert -2 == rechner.rechne(3, 5, None, 1)
assert 15 == rechner.rechne(3, 5, None, 2)
assert 0.6 == rechner.rechne(3, 5, None, 3)
assert 243 == rechner.rechne(3, 5, None, 4)
assert 0 == rechner.rechne(3, 5, None, 5)
assert 3 == rechner.rechne(3, 5, None, 6)
print(__name__)
if __name__ == "__main__":
    print("Bitte Main ausführen.")
