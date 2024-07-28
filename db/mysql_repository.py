from db.repository import *
import mysql.connector

class MysqlRepository(Repository):
    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            #'host': 'db', # to run LOCALLY, this should be localhost
            'host': 'localhost',
            #'port': '3306', # to run LOCALLY, this should be 32000
            'port': '32000',
            'database': 'russian'
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
        noun_gender = noun_gender_switcher.get(entry.get('noun_gender'), None)
        return noun_gender

    def map_noun_declension(self, entry: dict) -> Declension:
        noun_declension_switcher = {'first': Declension.FIRST,
                                    'second': Declension.SECOND,
                                    'third.': Declension.THIRD,
                                    'undeclined': Declension.UNDECLINED}
        noun_declension = noun_declension_switcher.get(entry.get('noun_declension', None))
        return noun_declension
