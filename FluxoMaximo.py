from Vertice import Vertice
from GrafoDirigido import GrafoDirigido
from queue import Queue

class FluxoMaximo:

    def buscarFluxoMaximo(grafo: GrafoDirigido, s: int, t: int):
        if type(grafo) is not GrafoDirigido:
            raise Exception("Busca do fluxo máximo funciona apenas com grafos dirigidos.")
        
        novoGrafo = FluxoMaximo.inserirVerticesArtificiaisSeNecessario(grafo)
        
        f = dict(map(lambda r: ((r.v1.numero - 1, r.v2.numero - 1), 0), novoGrafo.relacoes.values()))
        p = FluxoMaximo.buscarCaminhoAumentante(novoGrafo, s, t, f)
        fluxoMaximo = 0
        while p != None:
            cf = min(map(lambda x: novoGrafo.obterRelacao(x[1] + 1, p[ x[0] + 1 ] + 1).peso, enumerate(p[:-1])))
            for i in range(0, len(p) - 1):
                u = p[i]
                v = p[i + 1]
                f[(u, v)] += cf

            fluxoMaximo += cf
            p = FluxoMaximo.buscarCaminhoAumentante(novoGrafo, s, t, f)

        return fluxoMaximo
    
    def inserirVerticesArtificiaisSeNecessario(grafo: GrafoDirigido):
        vertices = list(map(lambda v: Vertice(v.numero, v.rotulo), grafo.vertices))
        mairoNumVertice = max(map(lambda v: v.numero, vertices))
        novoGrafo = GrafoDirigido(vertices)

        for key in grafo.relacoes:
            if key not in novoGrafo.relacoes:
                arcoAtual = grafo.relacoes[key]
                novoGrafo.adicionarRelacao(arcoAtual.v1, arcoAtual.v2, arcoAtual.peso)

                idArcoRetorno = grafo.gerarIdRelacao(arcoAtual.v2, arcoAtual.v1)
                if idArcoRetorno in grafo.relacoes:
                    mairoNumVertice = mairoNumVertice + 1
                    vertice = Vertice(mairoNumVertice, "Artificial " + str(mairoNumVertice))
                    novoGrafo.vertices.append(vertice)
                    novoGrafo.adicionarRelacao(arcoAtual.v2, vertice.numero, arcoAtual.peso)
                    novoGrafo.adicionarRelacao(vertice.numero, arcoAtual.v1, arcoAtual.peso)

        return novoGrafo

    def buscarCaminhoAumentante(grafo: GrafoDirigido, s: int, t: int, f: dict):
        # utiliza o número de vértices para inicializar os itens dos arrays com os valores default
        visitados = [False] * grafo.qtdVertices()
        ancestrais = [None] * grafo.qtdVertices()

        # define os valores para o vértice inicial
        visitados[s - 1] = True

        # inicializa a fila que é utilizada para a busca em largura, adicionando o índice do array que guarda os vértices no grafo
        fila = Queue()
        fila.put(s - 1)

        while not fila.empty():
            u = fila.get()

            vizinhos = grafo.obterVizinhosSaintes(u + 1)
            # o método obterVizinhosSaintes() recebe o número do vértice, portando precisa somar 1 ao índice do array
            for verticeDestino in vizinhos:
                # passa por cada vizinho e verifica se o mesmo ainda não foi visitado e se há fluxo residual
                v = verticeDestino.numero - 1
                capacidade = grafo.peso(u + 1, v + 1, 0)
                fluxo = f[(u, v)]
                cf = capacidade - fluxo
                
                if (not visitados[v]) and (cf > 0):
                    # marca o vizinho como visitado e seta seu ancestral
                    visitados[v] = True
                    ancestrais[v] = u

                    # se chegou ao vertice destino, monta o caminho aumentante e o retorna
                    if v == (t - 1):
                        p = [t - 1]
                        w = t - 1
                        while w != (s - 1):
                            w = ancestrais[w]
                            p.insert(0, w)
                        return p

                    # adiciona o vértice na fila para visitar seus vizinhos
                    fila.put(v)

        return None

    inserirVerticesArtificiaisSeNecessario = staticmethod(inserirVerticesArtificiaisSeNecessario)
    buscarFluxoMaximo = staticmethod(buscarFluxoMaximo)
    buscarCaminhoAumentante = staticmethod(buscarCaminhoAumentante)