from abc import ABC, abstractmethod
from Vertice import Vertice
from Aresta import Aresta
from Arco import Arco

class Grafo(ABC):

    def __init__(self, vertices):
        self.vertices = vertices # tipo vetor
        self.relacoes = {}

    @abstractmethod
    def gerarIdRelacao(self, v1, v2):
        pass

    @abstractmethod
    def obterTipoGrafo(self):
        pass

    @abstractmethod
    def adicionarRelacao(self, v1: Vertice, v2: Vertice, peso: float):
        pass

    def qtdVertices(self):
        return len(self.vertices)

    def qtdArestas(self):
        return len(self.relacoes)

    def grau(self, v: int):
        return len(self.vizinhos(v))

    def vizinhos(self, v: int):
        pass

    def mostrarGrafo(self):
        print(self.obterTipoGrafo())
        for v in self.vertices:
            print(str(v.numero) + ": " + ", ".join(map(lambda r: str(r.obterVerticeDestino(v).numero), v.relacoes.values())))
