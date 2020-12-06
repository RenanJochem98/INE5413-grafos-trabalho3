from abc import ABC, abstractmethod
from Vertice import Vertice
from Aresta import Aresta
from Arco import Arco

class Grafo(ABC):

    def __init__(self, vertices):
        self.vertices = vertices # tipo vetor
        self.relacoes = {}

    @abstractmethod
    def gerarIdRelacao(self, v1: Vertice, v2: Vertice):
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

    def haRelacao(self, u: int, v: int):
        return self.vertices[u - 1].ehVizinhoDe(self.vertices[v - 1])

    def obterRelacao(self, u: int, v: int):
        return self.relacoes[self.gerarIdRelacao(self.vertices[u - 1], self.vertices[v - 1])]

    def peso(self, u: int, v: int, pesoSeNaoExistirRelacao: float):
        idRelacao = self.gerarIdRelacao(self.vertices[u - 1], self.vertices[v - 1])
        relacao = self.relacoes[idRelacao] if idRelacao in self.relacoes else None
        return relacao.peso if relacao != None else pesoSeNaoExistirRelacao

    def mostrarGrafo(self):
        print(self.obterTipoGrafo())
        for v in self.vertices:
            print(str(v.numero) + ": " + ", ".join(map(lambda r: str(r.obterVerticeDestino(v).numero if r.ehVerticeOrigem(v) else r.obterVerticeOrigem(v).numero), v.relacoes.values())))