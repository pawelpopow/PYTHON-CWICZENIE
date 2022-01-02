class Person:

    def __init__(self, name, surname, age, phone, pesel):
        self.name = name
        self.surname = surname
        self.age = age
        self._phone = phone
        self._pesel = pesel

    def introduce_yourself(self):
        print(f"Moje imie to: {self.name} moje nazwisko to: {self.surname}  mam {self.age} lat")
        print(f"Mój numer telefonu: {self._phone}")
        print(f'Moj pesel to: {self._pesel}')


if __name__ == "__main__":
    person = Person(name='Borys', surname='Kozłowski', age=22, phone='604434233', pesel='934723432')
    person2 = Person(name='Ala', surname='Kot', age=20, phone='593645247', pesel='943543121')

    person.introduce_yourself()
    print(person)

    person2.introduce_yourself()
    print(person2)