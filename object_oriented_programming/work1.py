from object_oriented_programming.work import PizzaRobot, Pracownik, Szef, Obsluga

if __name__ == "__main__":
    bob = PizzaRobot('bob') # utworzenie robota o nazwie bob
    print(bob) # uruchomienie odziedziczonej __repr__
    bob.dajPodwyzke(0.20) # podwyższenie pensji boba o 20%
    print(bob);
    for klasa in Pracownik, Szef, Obsluga, PizzaRobot:
         obj = klasa(klasa.__name__)
         obj.praca()