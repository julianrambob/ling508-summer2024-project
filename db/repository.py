import abc
from model.noun import Noun


class Repository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load_lexicon(self) -> list[Noun]:
        raise NotImplementedError