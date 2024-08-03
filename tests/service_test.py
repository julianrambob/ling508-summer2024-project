from db.mysql_repository import *
from app.service import *

service = app.service.Service()
repo = MysqlRepository()

#tests for use case 1
def test_is_cyrillic():

    assert service.is_cyrillic('собака') == True
    assert service.is_cyrillic('hello') == False

def test_parse_noun_dom():
    noun_info = service.parse_noun('дом')
    assert noun_info['form'] == 'дом'
    assert noun_info['case'] == 'nominative'
    assert noun_info['gender'] == 'masculine'
    assert noun_info['number'] == 'singular'
    assert noun_info['definition'] == 'house'

#test for use case 2
def test_convert_cyrillic():
    service = app.service.Service()
    assert service.convert_to_cyrillic('rabotoyi') == 'работой'
    assert service.convert_to_cyrillic('privyet rabotnik!') == 'привет работник!'
    assert service.is_cyrillic(service.convert_to_cyrillic('dom')) == True

#test for use case 3
def test_generate_forms():
    forms = service.generate_forms('работа')

    expected_forms = [
        ("работа", Case.NOMINATIVE, Number.SINGULAR),
        ("работы", Case.NOMINATIVE, Number.PLURAL),
        ("работу", Case.ACCUSATIVE, Number.SINGULAR),
        ("работы", Case.ACCUSATIVE, Number.PLURAL),
        ("работы", Case.GENITIVE, Number.SINGULAR),
        ("работ", Case.GENITIVE, Number.PLURAL),
        ("работе", Case.PREPOSITIONAL, Number.SINGULAR),
        ("работах", Case.PREPOSITIONAL, Number.PLURAL),
        ("работе", Case.DATIVE, Number.SINGULAR),
        ("работам", Case.DATIVE, Number.PLURAL),
        ("работой", Case.INSTRUMENTAL, Number.SINGULAR),
        ("работами", Case.INSTRUMENTAL, Number.PLURAL)
    ]

    assert len(forms) == len(expected_forms)

    for i, (form, case, number) in enumerate(expected_forms):
        assert forms[i].form == form
        assert forms[i].pos == 'noun'
        assert forms[i].declension == Declension.FIRST
        assert forms[i].case == case
        assert forms[i].number == number