from app.enum import *
from app.noun import *
class VerbConjugator:
    def __init__(self):
        self.verb_endings = {
            (Case.NOMINATIVE, Number.SINGULAR): 'ю',
            (Case.NOMINATIVE, Number.PLURAL): 'ем',
            (Case.ACCUSATIVE, Number.SINGULAR): 'ешь',
            (Case.ACCUSATIVE, Number.PLURAL): 'ете',
            (Case.GENITIVE, Number.SINGULAR): 'ет',
            (Case.GENITIVE, Number.PLURAL): 'ют',
            (Case.PREPOSITIONAL, Number.SINGULAR): 'ешь',
            (Case.PREPOSITIONAL, Number.PLURAL): 'ете',
            (Case.DATIVE, Number.SINGULAR): 'ешь',
            (Case.DATIVE, Number.PLURAL): 'ете',
            (Case.INSTRUMENTAL, Number.SINGULAR): 'ешь',
            (Case.INSTRUMENTAL, Number.PLURAL): 'ете'
        }

    def conjugate_present(self, verb: str, definition: str) -> list:
        stem = verb[:-2]
        conjugations = []
        for (person, number), ending in self.verb_endings.items():
            form = stem + ending
            conjugations.append(Verb(form=form,
                                     pos='verb',
                                     definition=definition,
                                     tense=Tense.PRESENT,
                                     verbClass=VerbClass.A,
                                     person=person,
                                     number=number))
        return conjugations