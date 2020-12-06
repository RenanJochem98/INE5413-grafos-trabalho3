class ConjuntoIndependenteMaximal:

    def buscar(vertices):
        # Este algoritmo identifica o conjunto independente maximal
        # Adaptado de https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/independent.html
        c = [0] * len(vertices)
        for vertice in vertices:
            v =  vertice.numero - 1
            c[v] = 1
            for r in vertice.relacoes.values():
                w = r.obterVerticeDestino(vertice).numero - 1
                if c[w] == 1:
                    c[v] = 0
        return c
    
    buscar = staticmethod(buscar)