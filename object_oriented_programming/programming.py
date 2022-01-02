class SchoolMember:
    u'''Reprezentuje człowieka związanego z uczelnią.'''
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
        print('(Inicjalizacja SchoolMember: %s)' % self.imie)

    def powiedz(self):
        u'''Opowiedz o sobie.'''
        print('Imię:"%s" Wiek:"%s"' % (self.imie, self.wiek),)

class Wykladowca(SchoolMember):
    u'''Reprezentuje wykładowcę.'''
    def __init__(self, imie, wiek, pensja):
        SchoolMember.__init__(self, imie, wiek)
        self.pensja = pensja
        print('(Inicjalizacja Wykladowcy: %s)' % self.imie)

    def powiedz(self):
        SchoolMember.powiedz(self)
        print('Pensja: "%d"' % self.pensja)

class Student(SchoolMember):
    '''Reprezentuje studenta.'''
    def __init__(self, imie, wiek, oceny):
        SchoolMember.__init__(self, imie, wiek)
        self.oceny = oceny
        print('(Inicjalizacja Studenta: %s)' % self.imie)

    def powiedz(self):
        SchoolMember.powiedz(self)
        print('Oceny: "%d"' % self.oceny)