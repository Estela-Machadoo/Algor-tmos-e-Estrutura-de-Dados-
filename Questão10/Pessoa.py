from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, cpf):
        self._cpf = cpf  

    @abstractmethod
    def marcarPresenca(self):
        pass


















