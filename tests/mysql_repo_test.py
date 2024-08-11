from db.mysql_repository import *
from model.enum import *

repo = MysqlRepository()

noun_entry1 = {
    'id': 1,
    'form': 'дом',
    'pos': 'noun',
    'definition': 'house',
    'case': 'nominative',
    'gender': 'masculine',
    'number': 'singular',
    'declension': 'first'
}

noun_entry2 = {
    'id': 2,
    'form': 'работу',
    'pos': 'noun',
    'definition': 'worker/laborer',
    'case': 'accusative',
    'gender': 'feminine',
    'number': 'singular',
    'declension': 'first'
}
def test_get_details():
    dets1 = repo.get_details('работу')
    dets2 = repo.get_details('mmm')
    assert dets1 is not None
    assert dets2 is None
    assert Case(int(dets1['case'])) == Case.ACCUSATIVE

'''
def test_map_noun_gender():
    ng = repo.map_noun_gender(noun_entry1)
    assert ng == Gender.MASCULINE
    ng = repo.map_noun_gender(noun_entry2)
    assert ng == Gender.FEMININE

def test_map_noun_declension():
    nd = repo.map_noun_declension(noun_entry1)
    assert nd == Declension.FIRST
    nd = repo.map_noun_declension(noun_entry2)
    assert nd == Declension.FIRST

def test_map_noun_number():
    nn = repo.map_noun_number(noun_entry1)
    assert nn == Number.SINGULAR
    nn = repo.map_noun_number(noun_entry2)
    assert nn == Number.SINGULAR

def test_map_noun_case():
    nc = repo.map_noun_case(noun_entry1)
    assert nc == Case.NOMINATIVE
    nc = repo.map_noun_case(noun_entry2)
    assert nc == Case.ACCUSATIVE


def test_mapper():
    noun = repo.mapper(noun_entry2)
    assert noun.form == 'работу'
    assert noun.pos == 'noun'
    assert noun.definition == 'worker/laborer'
    assert noun.noun_case == Case.ACCUSATIVE
    assert noun.gender == Gender.FEMININE
    assert noun.number == Number.SINGULAR
    assert noun.declension == Declension.FIRST

    noun = repo.mapper(noun_entry1)
    assert noun.form == 'дом'
    assert noun.pos == 'noun'
    assert noun.definition == 'house'
    assert noun.noun_case == Case.NOMINATIVE
    assert noun.gender == Gender.MASCULINE
    assert noun.number == Number.SINGULAR
    assert noun.declension == Declension.FIRST

def test_load_lexicon():
    lexicon = repo.load_lexicon()
    print()
    print('Lexicon size: ' + str(len(lexicon)))
    assert len(lexicon) >= 4
'''