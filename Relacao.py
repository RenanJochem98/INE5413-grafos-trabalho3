from abc import ABC, abstractmethod

class Relacao(ABC):

    def __init__(self, id, v1, v2, peso):
        self.id = id
        self.v1 = v1
        self.v2 = v2
        self.peso = peso

    @abstractmethod
    def obterVerticeDestino(self, verticeOrigem):
        pass

    @abstractmethod
    def obterVerticeOrigem(self, verticeDestino):
        pass

    @abstractmethod
    def ehVerticeOrigem(self, vertice):
        pass