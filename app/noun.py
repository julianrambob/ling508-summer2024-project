from app.enum import *
from app.word import Word
class Noun(Word):

    def __init__(self,
                 form: str,
                 pos: str,
                 definition: str,
                 case: Case = None,
                 gender: Gender = None,
                 number: Number = None,
                 declension: Declension = None):
        super().__init__(form, pos, definition)
        self.case = case
        self.gender = gender
        self.number = number
        self.declension = declension