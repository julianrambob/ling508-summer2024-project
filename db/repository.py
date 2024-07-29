import abc
from app.enum import *
from app.noun import Noun


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_lexicon(self) -> list[Noun]:
        raise NotImplementedError