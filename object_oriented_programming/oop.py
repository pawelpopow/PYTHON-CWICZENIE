class Osoba:

    def __init__(self, imie, nazwisko, wiek, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self._telefon = telefon

    def przedstaw_sie(self):
        # print(f"Jestem {self.imie} {self.nazwisko}. Mam {self.wiek} lat.")
        # print(f"Moj telefon to {self._telefon}")
        # print(f"Moje imie to {self.imie}")
        print(f"Moje imie to: {self.imie} moje nazwisko to: {self.nazwisko}  mam {self.wiek} lat")
        print(f"Mój numer telefonu: {self._telefon}")

    # def urodziny(self):
    #     wiek_przed = self.wiek
    #     self.wiek += 1
    #     return wiek_przed


    # def main():
        # tworzymy dwa obiekty klasy Osoba
        # Jan = Osoba("Jan", "Nowak", 48)
        # Adam = Osoba("Adam", "Mickiewicz", 220)

        # wywołujemy metodę przedstaw_sie() na każdym z nich
        # Jan.przedstaw_sie()
        # Adam.przedstaw_sie()
        #
        # wiek_Adama_przed = Adam.urodziny()
        # Adam.przedstaw_sie()
        # print(f"Wiek Adama sprzed urodzin: {wiek_Adama_przed}")

        # odwołujemy się do pól, modyfikujemy je
        # Jan.imie = "Stanisław"
        # Jan.nazwisko = "Witkiewicz"
        # Jan.wiek = 133
        #
        # Jan.przedstaw_sie()


if __name__ == "__main__":

    # main()

    osoba = Osoba(imie='Kazimierz', nazwisko='Nowak', wiek=20, telefon='604434233')
    osoba2 = Osoba(imie='Asia', nazwisko='Jankowska', wiek=26, telefon='593645247')

    osoba.przedstaw_sie()
    print(osoba)

    osoba2.przedstaw_sie()
    print(osoba2)





    # Jestem Jan Nowak. Mam 48 lat.
    # Jestem Adam Mickiewicz. Mam 220 lat.
    # Jestem Adam Mickiewicz. Mam 221 lat.
    # Wiek Adama sprzed urodzin: 220
    # Jestem Stanisław Witkiewicz. Mam 133 lat.
