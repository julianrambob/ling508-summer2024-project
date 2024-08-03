from enum import Enum

class Case(Enum):
    NOMINATIVE = 1
    ACCUSATIVE = 2
    GENITIVE = 3
    PREPOSITIONAL = 4
    INSTRUMENTAL = 5
    DATIVE = 6


class Gender(Enum):
    MASCULINE = 1
    FEMININE = 2
    NEUTER = 3


class Number(Enum):
    SINGULAR = 1
    PLURAL = 2


class Person(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3


class Tense(Enum):
    PRESENT = 1
    IMPERFECT = 2
    FUTURE = 3
    PERFECT = 4
    PAST = 5


class Voice(Enum):
    ACTIVE = 1
    PASSIVE = 2

class VerbClass(Enum):
    A = 1
    YA = 2
    I = 3
    E = 4
    TI = 5
    IRR = 6

class Declension(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    UNDECLINED = 4