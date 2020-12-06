from Vertice import Vertice
from Grafo import Grafo
from Arco import Arco

class GrafoDirigido(Grafo):

    def gerarIdRelacao(self, v1, v2):
        return f'{v1.numero}.{v2.numero}'

    def adicionarRelacao(self, v1, v2, peso):
        id = self.gerarIdRelacao(v1, v2)
        relacao = Arco(id, v1, v2, peso)
        self.relacoes[id] = relacao
        self.vertices[v1.numero - 1].adicionarRelacao(relacao)
        # Verificar se eh necessario adcionar a vertice destino. Sem essa relacao no vertice destino, facilita a organizacao topologica
        self.vertices[v2.numero - 1].adicionarRelacao(relacao)

    def obterTipoGrafo(self):
        return "Grafo dirigido"

    def criarGrafoTransposto(self):
        vertices = list(map(lambda v: Vertice(v.numero, v.rotulo), self.vertices)) # para nao ficar na mesma posicao de memoria
        novoGrafo = GrafoDirigido(vertices)

        for key in self.relacoes:
            arcoAtual = self.relacoes[key]
            novoGrafo.adicionarRelacao(arcoAtual.v2, arcoAtual.v1, arcoAtual.peso)

        return novoGrafo

    def vizinhos(self, v):
        vizinhos = []
        for relacao in self.vertices[v - 1].relacoes.values():
            if relacao.v1.numero == v:
                vizinhos.append(relacao.v2)
            else:
                vizinhos.append(relacao.v1)
        return vizinhos

    def obterVizinhosSaintes(self, v):
        return self.vertices[v - 1].obterVizinhosSaintes()