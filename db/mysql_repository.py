from unittest import case
from model.enum import *
from db.repository import *
import mysql.connector
from model.noun import Noun
from model.nounDecliner import NounDecliner

class MysqlRepository(Repository):
    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            #'host': 'mysql', # to run LOCALLY, this should be localhost
            'host': 'localhost',
            #'port': '3306', # to run LOCALLY, this should be 32000
            'port': '32000',
            'database': 'russian_nouns'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except ReferenceError:
            pass
        except Exception as e:
            print(f"Error in __del__: {e}")
        

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
        noun_declension_switcher = {'1': Declension.FIRST,
                                    '2': Declension.SECOND,
                                    '3': Declension.THIRD,
                                    '4': Declension.UNDECLINED}
        noun_declension = noun_declension_switcher.get(entry.get('declension', None))
        return noun_declension
    
    def map_noun_number(self, entry:dict) -> Number:
        noun_number_switcher = {'1': Number.SINGULAR,
                                '2': Number.PLURAL}
        noun_number = noun_number_switcher.get(entry.get('number', None))
        return noun_number
    
    def map_noun_case(self, entry: dict) -> Case:
        noun_case_switcher = {'1': Case.NOMINATIVE,
                                    '2': Case.ACCUSATIVE,
                                    '3': Case.GENITIVE,
                                    '4': Case.PREPOSITIONAL,
                                    '6': Case.DATIVE,
                                    '5': Case.INSTRUMENTAL}
        noun_case = noun_case_switcher.get(entry.get('case', None))
        return noun_case
    
    def mapper(self, entry: dict) -> Noun:
        noun = Noun(
            form=entry.get('form'),
            pos=entry.get('pos'),
            definition=entry.get('definition'),
            base_form=entry.get('base_form'),
            noun_case=self.map_noun_case(entry),
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
            'base_form': base_form,
            'definition': definition,
            'nounCase': nounCase,
            'gender': gender,
            'number': number,
            'declension': declension} for (id, form, pos, definition, base_form, nounCase, gender, number, declension) in self.cursor]
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
                'base_form': row[4],
                'case': row[5],
                'gender': row[6],
                'number': row[7],
                'declension': row[8],
            }
            lexicon.append(entry)
        return lexicon

    def insert_noun(self, noun: Noun) -> int:
        sql = (
            "INSERT INTO nouns (form, pos, definition, base_form, nounCase, gender, number, declension)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )

        self.cursor.execute(sql,
                            (noun.form,
                             noun.pos,
                             noun.definition,
                             noun.base_form,
                             noun.noun_case,
                             noun.gender,
                             noun.number,
                             noun.declension.value))
        self.connection.commit()
        return self.cursor.lastrowid

    def insert_noun_decliner(self, decliner: NounDecliner):

        declined_forms = decliner.get_noun_forms()
        for form in declined_forms:
            self.insert_noun(form)


    def drop_nouns(self):
        sql = 'DELETE FROM nouns'
        self.cursor.execute(sql)
        self.connection.commit()

    def get_details(self, form: str):
        sql = "SELECT form, pos, definition, base_form, nounCase, gender, number, declension FROM nouns WHERE form = %s"
        self.cursor.execute(sql, (form,))
        result = self.cursor.fetchone()
        return result
