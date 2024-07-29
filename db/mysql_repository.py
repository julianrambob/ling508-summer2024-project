from unittest import case

from db.repository import *
import mysql.connector
from app.noun import Noun

class MysqlRepository(Repository):
    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'mysql', # to run LOCALLY, this should be localhost
            #'host': 'localhost',
            'port': '3306', # to run LOCALLY, this should be 32000
            #'port': '32000',
            'database': 'russian_nouns'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        

    def map_verb_class(self, entry: dict) -> VerbClass:
        verb_class_switcher = {'A': VerbClass.A,
                               'YA': VerbClass.YA,
                               'I': VerbClass.I,
                               'E': VerbClass.E,
                               'TI': VerbClass.TI,
                               'IRR': VerbClass.IRR,
                               }
        verb_class = verb_class_switcher.get(entry.get('verb_class'), None)
        return verb_class

    def map_noun_gender(self, entry: dict) -> Gender:
        noun_gender_switcher = {'neuter': Gender.NEUTER,
                                'masculine': Gender.MASCULINE,
                                'feminine': Gender.FEMININE}
        noun_gender = noun_gender_switcher.get(entry.get('gender'), None)
        return noun_gender

    def map_noun_declension(self, entry: dict) -> Declension:
        noun_declension_switcher = {'first': Declension.FIRST,
                                    'second': Declension.SECOND,
                                    'third': Declension.THIRD,
                                    'undeclined': Declension.UNDECLINED}
        noun_declension = noun_declension_switcher.get(entry.get('declension', None))
        return noun_declension
    
    def map_noun_number(self, entry:dict) -> Number:
        noun_number_switcher = {'singular': Number.SINGULAR,
                                'plural': Number.PLURAL}
        noun_number = noun_number_switcher.get(entry.get('number', None))
        return noun_number
    
    def map_noun_case(self, entry: dict) -> Case:
        noun_case_switcher = {'nominative': Case.NOMINATIVE,
                                    'accusative': Case.ACCUSATIVE,
                                    'genitive': Case.GENITIVE,
                                    'prepositional': Case.PREPOSITIONAL,
                                    'dative': Case.DATIVE,
                                    'instrumental': Case.INSTRUMENTAL}
        noun_case = noun_case_switcher.get(entry.get('case', None))
        return noun_case
    
    def mapper(self, entry: dict) -> Noun:
        noun = Noun(
            form=entry.get('form'),
            pos=entry.get('pos'),
            definition=entry.get('definition'),
            case=self.map_noun_case(entry),
            gender=self.map_noun_gender(entry),
            number=self.map_noun_number(entry),
            declension=self.map_noun_declension(entry)
        )
        return noun


    def load_lexicon2(self) -> list[Noun]:
        sql = 'SELECT * FROM russian_nouns'
        self.cursor.execute(sql)
        entries = [{
            'id': id,
            'form': form,
            'pos': pos,
            'definition': definition,
            'nounCase': nounCase,
            'gender': gender,
            'number': number,
            'declension': declension} for (id, form, pos, definition, nounCase, gender, number, declension) in self.cursor]
        lexicon = [self.mapper(entry) for entry in entries]
        return lexicon
    def load_lexicon(self):
        sql = 'SELECT * FROM nouns'
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        lexicon = []
        for row in results:
            entry = {
                'id': row[0],
                'form': row[1],
                'pos': row[2],
                'definition': row[3],
                'case': row[4],
                'gender': row[5],
                'number': row[6],
                'declension': row[7],
            }
            lexicon.append(entry)
        return lexicon