import app.util
import db.mysql_repository
import model.nounDecliner
from model.nounDecliner import NounDecliner
from app.util import *

class Service:
    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()

    def convert_to_cyrillic(self, text) -> str:
        return app.util.convert_to_cyrillic(text)
    def is_cyrillic(self, text) -> bool:
        return app.util.is_cyrillic(text)
    def getNounEndings(self):
        self.repo.drop_nouns()
        #self.repo.
    def parse_noun(self, noun:str) -> dict:
        result = self.repo.get_details(noun)
        return result

    def generate_forms(self, noun:str) -> list:
        parsed_noun = self.parse_noun(noun)
        forms = model.nounDecliner.NounDecliner()
        return forms.decline_first(parsed_noun['id'], noun, parsed_noun['definition'])
