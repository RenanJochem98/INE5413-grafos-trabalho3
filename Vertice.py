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
