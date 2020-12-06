from Relacao import Relacao

class Vertice:

    def __init__(self, numero, rotulo):
        self.numero = numero
        self.rotulo = rotulo
        self.relacoes = {}

    def adicionarRelacao(self, relacao: Relacao):
        self.relacoes[relacao.id] = relacao

    def apagarTodasRelacoes(self):
        self.relacoes = {}

    def obterVizinhosSaintes(self):
        saintes = []

        for relacao in self.relacoes.values():
            if relacao.ehVerticeOrigem(self):
                saintes.append(relacao.obterVerticeDestino(self))
        
        return saintes

    def ehVizinhoDe(self, v):
        for relacao in self.relacoes.values():
            if relacao.v1.numero == v or relacao.v2.numero == v:
                return True
        return False