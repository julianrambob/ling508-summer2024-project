from model.enum import *
from model.word import Word
class Noun(Word):

    def __init__(self,
                 id: int,
                 form: str,
                 pos: str,
                 definition: str,
                 case: Case = None,
                 gender: Gender = None,
                 number: Number = None,
                 declension: Declension = None):
        super().__init__(id, form, pos, definition)
        self.case = case
        self.gender = gender
        self.number = number
        self.declension = declension

    def get_fields(self) -> dict:
        fields = {
            'id': self.id,
            'form': self.form,
            'pos': self.pos,
            'case': self.case,
            'gender': self.gender,
            'number': self.number,
            'declension': self.declension
        }
        return fields
