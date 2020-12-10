from Vertice import Vertice
from GrafoNaoDirigido import GrafoNaoDirigido
from queue import Queue
from ConjuntoIndependenteMaximal import ConjuntoIndependenteMaximal

class ColoracaoMinima:

    def buscar(grafo: GrafoNaoDirigido):
        if type(grafo) is not GrafoNaoDirigido:
            raise Exception("A busca pela coloração mínima funciona apenas com grafos não-dirigidos.")

        vertices = sorted(map(lambda v: v.numero, grafo.vertices), reverse=True)
        powerset = list(sorted(ColoracaoMinima.powerset(vertices), key=ColoracaoMinima.f))[1:]
        t = 2 ** len(vertices)
        x = [0] * t

        for subconjunto in powerset:
            s = ColoracaoMinima.f(subconjunto)
            x[s] = float("inf")
            verticesSubgrafo = list(map(lambda v: grafo.vertices[v - 1], subconjunto))
            verticesIG = ConjuntoIndependenteMaximal.buscarVertices(verticesSubgrafo)
            i = ColoracaoMinima.f(ColoracaoMinima.subtrairConjunto(subconjunto, verticesIG))
            if (x[i] + 1) < x[s]:
                x[s] = x[i] + 1

        return x[t - 1]


    def powerset(s):
        # Fonte https://stackoverflow.com/a/1482320
        x = len(s)
        masks = [1 << i for i in range(x)]
        for i in range(1 << x):
            yield [ss for mask, ss in zip(masks, s) if i & mask]

    def f(subconjunto):
        r = 0
        for vertice in subconjunto:
            r += 2 ** (vertice - 1)
        return r

    def subtrairConjunto(conjunto, subtrair):
        resultado = []
        numerosSubtrair = list(map(lambda v: v.numero, subtrair))
        for item in conjunto:
            if item not in numerosSubtrair:
                resultado.append(item)
        return resultado

    f = staticmethod(f)
    subtrairConjunto = staticmethod(subtrairConjunto)
    powerset = staticmethod(powerset)
    buscar = staticmethod(buscar)