
from app.enum import *
from app.verb import Verb
from app.verbConjugator import VerbConjugator

def test_present_rabotat():
    lex_entry = Verb(
        form='работать',
        pos='verb',
        definition='to work',
        tense=Tense.PRESENT,
        verbClass=VerbClass.FIRST
    )

    conjugator = VerbConjugator()

    words = conjugator.conjugate_present(lex_entry.form, lex_entry.definition)

    rabotat_conjugations = [
        ("работаю", Person.FIRST, Number.SINGULAR),
        ("работаем", Person.FIRST, Number.PLURAL),
        ("работаешь", Person.SECOND, Number.SINGULAR),
        ("работаете", Person.SECOND, Number.PLURAL),
        ("работает", Person.THIRD, Number.SINGULAR),
        ("работают", Person.THIRD, Number.PLURAL)
    ]

    assert len(words) == len(rabotat_conjugations)

    for i, (surface, person, number) in enumerate(rabotat_conjugations):
        assert words[i].form == surface
        assert words[i].person == person
        assert words[i].number == number
        assert words[i].tense == Tense.PRESENT
        assert words[i].verbClass == VerbClass.FIRST

