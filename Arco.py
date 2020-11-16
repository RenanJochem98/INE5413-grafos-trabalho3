from Relacao import Relacao
from Vertice import Vertice

class Arco(Relacao):

    def obterVerticeDestino(self, verticeOrigem: Vertice):
        if (verticeOrigem.numero != self.v1.numero):
            raise Exception('O vértice de origem informado não corresponde ao vértice de origem do arco')
        return self.v2

    def obterVerticeOrigem(self, verticeDestino: Vertice):
        if (verticeDestino.numero != self.v2.numero):
            raise Exception('O vértice de destino informado não corresponde ao vértice de destino do arco')
        return self.v1

    def ehVerticeOrigem(self, vertice:Vertice):
        return vertice.numero == self.v1.numero
