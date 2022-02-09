class People:


    def __init__(self, name, surname, birth_year, pesel):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self._pesel = pesel

class Man(People):

    def __init__(self, name, surname, birth_year, pesel,):
        super().__init__(name, surname, birth_year, pesel)




if __name__ == '__main__':
    peopla = People()

