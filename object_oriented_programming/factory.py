def factory(aClass, *args):                          # krotka varargs
     return apply(aClass, args)                      # wywołanie aClass

class Mielonka:

    def doit(self, message):
        print(message)

class Osoba:
    def __init__(self, nazwa, praca):
        self.nazwa = nazwa
        self.praca = praca

 if __name__ == '__main__':

    object1 = factory(Mielonka)                      # utworzenie Mielonka
    object2 = factory(Osoba, "Guido", "guru")        # utworzenie Osoba