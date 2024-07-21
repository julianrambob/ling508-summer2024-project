from app.enum import *
from app.noun import Noun
from app.nounDecliner import NounDecliner

def test_first_declension_rabota():

    lex_entry = Noun(
        form='работа',
        pos='noun',
        definition='worker/laborer',
        declension=Declension.FIRST
    )

    declined = NounDecliner()

    words = declined.decline_first(lex_entry.form, lex_entry.definition)

    expected_forms = [
        ("работаю", Case.NOMINATIVE, Number.SINGULAR),
        ("работаем", Case.NOMINATIVE, Number.PLURAL),
        ("работаешь", Case.ACCUSATIVE, Number.SINGULAR),
        ("работаете", Case.ACCUSATIVE, Number.PLURAL),
        ("работает", Case.GENITIVE, Number.SINGULAR),
        ("работают", Case.GENITIVE, Number.PLURAL),
        ("работаем", Case.PREPOSITIONAL, Number.SINGULAR),
        ("работаете", Case.PREPOSITIONAL, Number.PLURAL),
        ("работаем", Case.DATIVE, Number.SINGULAR),
        ("работаете", Case.DATIVE, Number.PLURAL),
        ("работаем", Case.INSTRUMENTAL, Number.SINGULAR),
        ("работаете", Case.INSTRUMENTAL, Number.PLURAL),
    ]

    assert len(words) == len(expected_forms)

    for i, (form, case, number) in enumerate(expected_forms):
        assert words[i].form == form
        assert words[i].pos == 'noun'
        assert words[i].declension == Declension.FIRST
        assert words[i].case == case
        assert words[i].number == number