class Pracownik:

     def __init__(self, nazwa, placa=0):
        self.nazwa = nazwa
        self.placa = placa
     def dajPodwyzke(self, procent):
        self.placa = self.placa + (self.placa * procent)
     def praca(self):
        print(self.nazwa, "robi nadzienie")
     def __repr__(self):
         return "<Pracownik: nazwa=%s, placa=%s>" % (self.nazwa, self.placa)

class Szef(Pracownik):
     def __init__(self, nazwa):
        Pracownik.__init__(self, nazwa, 50000)
     def praca(self):
        print(self.nazwa, "robi jedzonko")

class Obsluga(Pracownik):

     def __init__ (self, nazwa):
        Pracownik.__init__(self, nazwa, 40000)
     def praca(self):
        print(self.nazwa, "obsluguje klientow")

class PizzaRobot(Szef):

     def __init__(self, nazwa):
        Szef.__init__(self, nazwa)
     def praca(self):
         print(self.nazwa, "robi pizze")