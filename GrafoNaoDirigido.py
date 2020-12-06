from Grafo import Grafo
from Aresta import Aresta

class GrafoNaoDirigido(Grafo):

    def gerarIdRelacao(self, v1, v2):
        return f'{min(v1.numero, v2.numero)}.{max(v1.numero, v2.numero)}'

    def adicionarRelacao(self, v1, v2, peso):
        id = self.gerarIdRelacao(v1, v2)
        relacao = Aresta(id, v1, v2, peso)
        self.relacoes[id] = relacao
        self.vertices[v1.numero - 1].adicionarRelacao(relacao)
        self.vertices[v2.numero - 1].adicionarRelacao(relacao)

    def obterTipoGrafo(self):
        return "Grafo não-dirigido"

    def vizinhos(self, v):
        vertice = self.vertices[v - 1]
        return list(map(lambda r: r.obterVerticeDestino(vertice), vertice.relacoes.values()))