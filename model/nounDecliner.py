
from model.noun import *
class NounDecliner:
    def __init__(self):
        self.noun_endings = {
            (Case.NOMINATIVE, Number.SINGULAR): 'а',
            (Case.NOMINATIVE, Number.PLURAL): 'ы',
            (Case.ACCUSATIVE, Number.SINGULAR): 'у',
            (Case.ACCUSATIVE, Number.PLURAL): 'ы',
            (Case.GENITIVE, Number.SINGULAR): 'ы',
            (Case.GENITIVE, Number.PLURAL): '',
            (Case.PREPOSITIONAL, Number.SINGULAR): 'е',
            (Case.PREPOSITIONAL, Number.PLURAL): 'ах',
            (Case.DATIVE, Number.SINGULAR): 'е',
            (Case.DATIVE, Number.PLURAL): 'ам',
            (Case.INSTRUMENTAL, Number.SINGULAR): 'ой',
            (Case.INSTRUMENTAL, Number.PLURAL): 'ами'
        }

    def decline_first(self, id:int, noun: str, definition: str) -> list:
        stem = noun[:-1]
        declined = []
        for (case, number), ending in self.noun_endings.items():
            form = stem + ending
            declined.append(Noun(
                id = id, form = form,
                                     pos = 'noun',
                                     definition = definition,
                                     declension = Declension.FIRST,
                                     case = case,
                                     number = number))
        return declined