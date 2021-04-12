from abc import ABC, abstractmethod


class Task(ABC):
    _output = None

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def output(self):
        pass
