from unittest import case
from model.enum import *
from db.repository import *
import mysql.connector
from model.noun import Noun

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
            id=entry.get('id'),
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

    def insert_first_declension(self, noun) -> None:
        sql = ("INSERT INTO russian_nouns "
               "(id, form, pos, definition, nounCase, gender, number, declension) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        self.cursor.execute(sql, (id, noun.form, noun.pos, noun.definition,noun.case, noun.gender, noun.number, noun.declension))

    def insert_noun_decliner(self, nounEndings: list[Noun]) -> None:
        for noun in nounEndings:
            fields = noun.get_fields()
            self.insert_first_declension(fields)

    def drop_nouns(self):
        sql = 'DROP TABLE IF EXISTS nouns'
        self.cursor.execute(sql)
        self.connection.commit()
    def get_details(self, form:str) -> dict:
        sql = "SELECT id, form, pos, definition, nounCase, gender, number, declension FROM nouns WHERE form = %s"
        self.cursor.execute(sql, (form,))
        entry = self.cursor.fetchone()
        if entry:
            id, form, pos, definition, case, gender, number, declension = entry
            return {'id': id, 'form': form, 'pos': pos, 'definition': definition, 'case': case, 'gender': gender, 'number': number, 'declension': declension}
        else:
            return None