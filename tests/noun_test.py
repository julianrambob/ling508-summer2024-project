from model.enum import *
from model.noun import Noun
from model.nounDecliner import NounDecliner

def test_first_declension_rabota():

    declined = NounDecliner()

    words = declined.decline_first(0,'работа', 'worker/laborer')

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

    assert len(words) == len(expected_forms)

    for i, (form, case, number) in enumerate(expected_forms):
        assert words[i].form == form
        assert words[i].pos == 'noun'
        assert words[i].declension == Declension.FIRST
        assert words[i].case == case
        assert words[i].number == number