class Set:

    def __init__(self, value = []): # konstruktor
        self.data = []  # zarządza listą
        self.concat(value)

    def intersect(self, other):  # other jest dowolną sekwencją
        res = []  # self jest przedmiotem
        for x in self.data:
            if x in other:  # wskazuje wspólne pozycje
                res.append(x)
            return Set(res)  # zwraca nowy Set

    def union(self, other):  # other jest dowolną sekwencją
        res = self.data[:]  # kopia danej listy
        for x in other:  # dodawanie pozycji do other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):  # value: list, Set...
        for x in value:  # usuwa duplikaty
            if not x in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)  # len(self)

    def __getitem__(self, key):
        return self.data[key]  # self[i]

    def __and__(self, other):
        return self.intersect(other)  # self & other

    def __or__(self, other):
        return self.union(other)  # self | other

    def __repr__(self):
        return 'Set:' + self.data  # print