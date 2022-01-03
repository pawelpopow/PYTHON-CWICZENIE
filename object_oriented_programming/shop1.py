from object_oriented_programming.shop import PizzaSklep

if __name__ == "__main__":

     scena = PizzaSklep()  # tworzenie kompozycji
     scena.zamowienie('Homer') # symulacja zamówienia Homera
     print('...')
     scena.zamowienie('Shaggy') # symulacja zamówienia Shaggy