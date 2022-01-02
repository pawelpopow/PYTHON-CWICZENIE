from object_oriented_programming.programming import Wykladowca, Student

if __name__ == '__main__':
    w = Wykladowca('Mrs. Shrividya', 40, 30000)
    s = Student('Swaroop', 25, 75)

    # print(# wypisuje pustą linię)

    osoby = [w, s]
    for osoba in osoby:
        osoba.powiedz() # działa zarówno dla Wykładowców, jak i Studentów