
from model.verb import *
class VerbConjugator:
    def __init__(self):
        self.verb_endings = {
            (Person.FIRST, Number.SINGULAR): 'ю',
            (Person.FIRST, Number.PLURAL): 'ем',
            (Person.SECOND, Number.SINGULAR): 'ешь',
            (Person.SECOND, Number.PLURAL): 'ете',
            (Person.THIRD, Number.SINGULAR): 'ет',
            (Person.THIRD, Number.PLURAL): 'ют'
        }

    def conjugate_present(self,id:int, verb: str, definition: str) -> list:
        stem = verb[:-2]
        conjugations = []
        for (person, number), ending in self.verb_endings.items():
            form = stem + ending
            conjugations.append(Verb(
                id=id, form=form,
                                     pos='verb',
                                     definition=definition,
                                     tense=Tense.PRESENT,
                                     verbClass=VerbClass.A,
                                     person=person,
                                     number=number))
        return conjugations