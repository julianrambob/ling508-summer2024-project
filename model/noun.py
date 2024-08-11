from model.enum import *
from model.word import Word
class Noun(Word):

    def __init__(self,
                 form: str,
                 pos: str,
                 definition: str,
                 base_form: str,
                 noun_case: Case = None,
                 gender: Gender = None,
                 number: Number = None,
                 declension: Declension = None):
        super().__init__(form, pos, definition)
        self.base_form = base_form
        self.noun_case = noun_case
        self.gender = gender
        self.number = number
        self.declension = declension

    def get_fields(self) -> dict:
        fields = {
            'form': self.form,
            'pos': self.pos,
            'base_form': self.base_form,
            'case': self.noun_case,
            'gender': self.gender,
            'number': self.number,
            'declension': self.declension
        }
        return fields
