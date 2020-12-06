from Vertice import Vertice
from GrafoBipartido import GrafoBipartido
from queue import Queue

class EmparelhamentoMaximo:

    def buscarEmparelhamentoMaximo(grafo: GrafoBipartido):
        if type(grafo) is not GrafoBipartido:
            raise Exception("A busca pelo emparelhamento máximo funciona apenas com grafos bipartidos.")

        d = [float("inf")] * (grafo.qtdVertices() + 1)
        mate = [0] * (grafo.qtdVertices() + 1)
        m = 0

        while EmparelhamentoMaximo.bfs(grafo, mate, d):
            for verticeX in grafo.X:
                x = verticeX.numero
                if mate[x] == 0:
                    if EmparelhamentoMaximo.dfs(grafo, mate, x, d):
                        m += 1

        return (m, mate[1:])

    def bfs(grafo, mate, d):
        fila = Queue()
        for vertice in grafo.X:
            x = vertice.numero
            if mate[x] == 0:
                d[x] = 0
                fila.put(x)
            else:
                d[x] = float("inf")

        d[0] = float("inf")

        while not fila.empty():
            x = fila.get()
            if d[x] < d[0]:
                verticeX = grafo.vertices[x - 1]
                for aresta in verticeX.relacoes.values():
                    y = aresta.obterVerticeDestino(verticeX).numero
                    if d[mate[y]] == float("inf"):
                        d[mate[y]] = d[x] + 1
                        fila.put(mate[y])

        return d[0] != float("inf")

    def dfs(grafo, mate, x, d):
        if x != 0:
            verticeX = grafo.vertices[x - 1]
            for aresta in verticeX.relacoes.values():
                y = aresta.obterVerticeDestino(verticeX).numero
                if d[mate[y]] == d[x] + 1:
                    if EmparelhamentoMaximo.dfs(grafo, mate, mate[y], d):
                        mate[y] = x
                        mate[x] = y
                        return True

            d[x] = float("inf")
            return False

        return True

    buscarEmparelhamentoMaximo = staticmethod(buscarEmparelhamentoMaximo)
    bfs = staticmethod(bfs)
    dfs = staticmethod(dfs)