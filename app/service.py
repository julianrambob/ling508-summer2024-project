import app.util
from db.mysql_repository import MysqlRepository
from model.enum import *
from model.nounDecliner import NounDecliner
import random

class Service:
    def __init__(self):
        self.repo = MysqlRepository()

    def convert_to_cyrillic(self, text) -> str:
        return app.util.convert_to_cyrillic(text)
    def is_cyrillic(self, text) -> bool:
        return app.util.is_cyrillic(text)

    def add_noun(self, nominative_form: str, definition: str, gender_int: int) -> str:
        gender = Gender(gender_int)
        decliner = NounDecliner(nominative_form, definition, gender)
        self.repo.insert_noun_decliner(decliner)
        return nominative_form

    def get_all_nouns(self):
        return self.repo.load_lexicon()

    #Currently unused get_noun() could be used for a search feature or to prevent duplicate entries in the database
    def get_noun(self, form: str):
        return self.repo.get_details(form)
    def get_random_noun(self):
        nouns = self.repo.load_lexicon()
        if not nouns:
            return None
        return random.choice(nouns)
    def refresh_database(self):
        self.repo.drop_nouns()


    def get_noun_details(self, form: str):
        return self.repo.get_details(form)
    def get_case_name(self, noun: dict) -> str:
        noun_case = self.repo.map_noun_case(noun)
        case_names = {
            Case.NOMINATIVE: 'Nominative',
            Case.ACCUSATIVE: 'Accusative',
            Case.GENITIVE: 'Genitive',
            Case.PREPOSITIONAL: 'Prepositional',
            Case.DATIVE: 'Dative',
            Case.INSTRUMENTAL: 'Instrumental'
        }
        return case_names.get(noun_case, 'Unknown Case')

    def get_number_name(self, noun: dict) -> str:
        number = self.repo.map_noun_number(noun)
        number_names = {
            Number.SINGULAR: 'Singular',
            Number.PLURAL: 'Plural'
        }
        return number_names.get(number, 'Unknown Number')