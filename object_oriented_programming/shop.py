from object_oriented_programming.work import Obsluga, PizzaRobot


class Klient:

     def __init__(self, nazwa):
        self.nazwa = nazwa

     def zamowienie(self, obsluga):
        print(self.nazwa, "zamawia u", obsluga)

     def placic(self, obsluga):
        print(self.nazwa, "placi za pozycje do", obsluga)

class Piec:

     def piecze(self):
        print("piec piecze")

class PizzaSklep:

     def __init__(self):

         self.obsluga = Obsluga('Pat') # osadza inne obiekty
         self.szef = PizzaRobot ('Bob') # robot o imieniu bob
         self.piec = Piec()

     def zamowienie(self, nazwa):

        klient = Klient(nazwa) # uaktywnia inne obiekty
        klient.zamowienie(self.obsluga)  # zamówienia klientów u obsługi
        self.szef.praca()
        self.piec.piecze()
        klient.placic(self.obsluga)

