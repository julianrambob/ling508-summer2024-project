import abc
from app.enum import *
from app.word import Word


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_lexicon(self) -> list[Word]:
        raise NotImplementedError