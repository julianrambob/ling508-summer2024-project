from app.enum import *
from app.word import Word

class Verb(Word):

    def __init__(self, 
                 form: str, 
                 pos: str, 
                 definition: str,
                 tense: Tense,
                 verbClass: VerbClass,
                 person: Person = None,
                 gender: Gender = None,
                 number: Number = None,
                 ):
        super().__init__(form, pos, definition)
        self.tense = tense
        self.person = person
        self.gender = gender
        self.number = number
        self.verbClass = verbClass