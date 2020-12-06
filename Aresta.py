from Relacao import Relacao
from Vertice import Vertice

class Aresta(Relacao):

    def obterVerticeDestino(self, verticeOrigem: Vertice):
        if (self.v1.numero == verticeOrigem.numero):
            return self.v2
        elif (self.v2.numero == verticeOrigem.numero):
            return self.v1
        else:
            raise Exception('O vértice de origem informado não faz parte da aresta')

    def obterVerticeOrigem(self, verticeDestino: Vertice):
        if (self.v1.numero == verticeDestino.numero):
            return self.v2
        elif (self.v2.numero == verticeDestino.numero):
            return self.v1
        else:
            raise Exception('O vértice de destino informado não faz parte da aresta')

    def ehVerticeOrigem(self, vertice:Vertice):
        return True
