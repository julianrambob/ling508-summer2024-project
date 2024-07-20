from app.enum import *
class Noun:

    def __init__(self,
                 case: Case,
                 person: Person,
                 gender: Gender,
                 number: Number,
                 declension: Declension):
        self.case = case
        self.person = person
        self.gender = gender
        self.number = number
        self.declension = declension