class Robot:
    u'''Reprezentuje robota, z nazwą.'''

    # Zmienna klasy pokazująca liczbę robotów
    populacja = 0

    def __init__(self, nazwa):
        u'''Inicjalizuje dane.'''
        self.nazwa = nazwa
        print('(Inicjalizacja %s)' % self.nazwa)

        # Kiedy nowy robot jest tworzony, zwiększamy
        # licznik populacji o 1
        Robot.populacja += 1

    def __del__(self):
        u'''Umieram.'''
        print('%s jest niszczony!' % self.nazwa)

        Robot.populacja -= 1

        if Robot.populacja == 0:
            print('%s był ostatnim robotem.' % self.nazwa)
        else:
            print('Postały %d roboty.' % Robot.populacja)

    def przywitajSie(self):
        u'''Powitanie robota.

        Tak, one naprawdę to potrafią.'''
        print('Melduję się, moi panowie nazywają mnie %s.' % self.nazwa)

    def jakDuzo():
        u'''Wypisuje aktualną populację.'''
        print('Mamy %d roboty.' % Robot.populacja)
    jakDuzo = staticmethod(jakDuzo)