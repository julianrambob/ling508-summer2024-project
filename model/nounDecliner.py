from model.enum import *
from model.noun import *


class NounDecliner:
    def __init__(self, nominative_form: str, definition: str, gender: Gender):

        # This data structure takes always nominative endings for plural accusative nouns but first declension plural nouns might share accusative endings with genitive, not nominative.
        # This issue could be addressed by adding the ability for the user to manually add plural accusative endings.
        self.noun_endings_first_a = {
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

        self.noun_endings_first_ya = {
            (Case.NOMINATIVE, Number.SINGULAR): 'я',
            (Case.NOMINATIVE, Number.PLURAL): 'и',
            (Case.ACCUSATIVE, Number.SINGULAR): 'ю',
            (Case.ACCUSATIVE, Number.PLURAL): 'и',
            (Case.GENITIVE, Number.SINGULAR): 'и',
            (Case.GENITIVE, Number.PLURAL): 'ь',
            (Case.PREPOSITIONAL, Number.SINGULAR): 'е',
            (Case.PREPOSITIONAL, Number.PLURAL): 'ях',
            (Case.DATIVE, Number.SINGULAR): 'е',
            (Case.DATIVE, Number.PLURAL): 'ям',
            (Case.INSTRUMENTAL, Number.SINGULAR): 'ей',
            (Case.INSTRUMENTAL, Number.PLURAL): 'ями'
        }

        self.noun_endings_first_iya = {
            (Case.NOMINATIVE, Number.SINGULAR): 'ия',
            (Case.NOMINATIVE, Number.PLURAL): 'ии',
            (Case.ACCUSATIVE, Number.SINGULAR): 'ию',
            (Case.ACCUSATIVE, Number.PLURAL): 'ии',
            (Case.GENITIVE, Number.SINGULAR): 'ии',
            (Case.GENITIVE, Number.PLURAL): 'ий',
            (Case.PREPOSITIONAL, Number.SINGULAR): 'ии',
            (Case.PREPOSITIONAL, Number.PLURAL): 'иях',
            (Case.DATIVE, Number.SINGULAR): 'ии',
            (Case.DATIVE, Number.PLURAL): 'иям',
            (Case.INSTRUMENTAL, Number.SINGULAR): 'ией',
            (Case.INSTRUMENTAL, Number.PLURAL): 'иями'
        }


        self.nominative_form = nominative_form
        self.definition = definition
        self.gender = gender
        self.noun_forms = self.decline_first(nominative_form, definition, gender)
    def decline_first(self, noun: str, definition: str, gender: Gender) -> list:

        declined = []

        if noun[-1] == 'я':
            if noun[-2] == 'и':
                stem = noun[:-2]
                endings = self.noun_endings_first_iya
            else:
                stem = noun[:-1]
                endings = self.noun_endings_first_ya
        else:
            stem = noun[:-1]
            endings = self.noun_endings_first_a

        for (case, number), ending in endings.items():
            form = stem + ending
            declined.append(
                Noun(form=form, pos='noun', definition=definition, base_form=self.nominative_form, declension=Declension.FIRST, noun_case=case.value, gender=gender.value,
                     number=number.value))
        return declined

    def get_noun_forms(self):
        return self.noun_forms