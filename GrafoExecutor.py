from Grafo import Grafo
from GrafoDirigido import GrafoDirigido
from GrafoBipartido import GrafoBipartido
from FluxoMaximo import FluxoMaximo
from EmparelhamentoMaximo import EmparelhamentoMaximo

class GrafoExecutor:

    def buscarFluxoMaximo(self, grafo: GrafoDirigido, s: int, t: int):
        return FluxoMaximo.buscarFluxoMaximo(grafo, s, t)

    def buscarEmparelhamentoMaximo(self, grafo: GrafoBipartido):
        return EmparelhamentoMaximo.buscarEmparelhamentoMaximo(grafo)

    def qtdVertices(self, grafo:Grafo):
        return grafo.qtdVertices()

    def qtdRelacoes(self, grafo:Grafo):
        return grafo.qtdArestas()

    def grau(self, grafo:Grafo,  v):
        return len(grafo.vertices[v - 1].relacoes)

    def rotulo(self, grafo:Grafo, v):
        return grafo.vertices[v - 1].rotulo

    def vizinhos(self, grafo:Grafo, v):
        return grafo.vizinhos(v)

    def haRelacao(self, grafo:Grafo, u, v):
        return grafo.haRelacao(u, v)

    def peso(self, grafo:Grafo, u, v):
        return grafo.peso(u, v, float("inf"))
