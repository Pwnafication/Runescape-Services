class Person:
    def __init__(self, str_Name, b_IsAlive=True, lst_Children=None):
        self.str_Name = str_Name
        self.IsAlive = b_IsAlive
        self.lst_Children = lst_Children if lst_Children is not None else []

class Monarchy:
    def __init__(self, person_King):
        self.person_King = Person(person_King)
        self.dct_Persons = {self.person_King.str_Name: self.person_King}

    def birth(self, str_ChildName, str_ParentName):
        self.dct_Persons