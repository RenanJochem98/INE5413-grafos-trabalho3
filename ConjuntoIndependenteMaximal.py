class ConjuntoIndependenteMaximal:

    def buscar(vertices):
        # Este algoritmo identifica o conjunto independente maximal
        # Adaptado de https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/independent.html
        c = [0] * len(vertices)
        for i, vertice in enumerate(vertices):
            c[i] = 1
            for r in vertice.relacoes.values():
                w = ConjuntoIndependenteMaximal.buscarPosicaoDoVerticeNaLista(r.obterVerticeDestino(vertice).numero, vertices)
                if w > -1 and c[w] == 1:
                    c[i] = 0
        return c
    
    def buscarVertices(vertices):
        ig = ConjuntoIndependenteMaximal.buscar(vertices)
        resultado = []
        for i, c in enumerate(ig):
            if c == 1:
                resultado.append(vertices[i])
        return resultado

    def buscarPosicaoDoVerticeNaLista(numeroDoVertice, vertices):
        if len(vertices) >= numeroDoVertice and vertices[numeroDoVertice - 1].numero == numeroDoVertice:
            return numeroDoVertice - 1

        for i, vertice in enumerate(vertices):
            if vertice.numero == numeroDoVertice:
                return i
                
        return -1

    buscar = staticmethod(buscar)
    buscarVertices = staticmethod(buscarVertices)
    buscarPosicaoDoVerticeNaLista = staticmethod(buscarPosicaoDoVerticeNaLista)