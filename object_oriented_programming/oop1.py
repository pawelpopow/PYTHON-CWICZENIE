from object_oriented_programming.oop import Osoby

if __name__ == "__main__":

    # main()
    osoby = Osoby(imie='Borys', nazwisko='Kozłowski', wiek=22, telefon='604434233')
    osoby2 = Osoby(imie='Ala', nazwisko='Kot', wiek=20, telefon='593645247')



    osoby.przedstaw_sie()
    print(osoby)

    osoby2.przedstaw_sie()
    print(osoby)





    # Jestem Jan Nowak. Mam 48 lat.
    # Jestem Adam Mickiewicz. Mam 220 lat.
    # Jestem Adam Mickiewicz. Mam 221 lat.
    # Wiek Adama sprzed urodzin: 220
    # Jestem Stanisław Witkiewicz. Mam 133 lat.