from Vertice import Vertice
from Grafo import Grafo
from GrafoDirigido import GrafoDirigido
from GrafoNaoDirigido import GrafoNaoDirigido

class LeitorGrafo:

    def lerGrafoDoArquivo(arquivo: str):
        f = open(arquivo, "r", encoding='utf-8')
        linhas = f.readlines()
        f.close()

        vertices = LeitorGrafo.__lerVertices(linhas)
        numeroDeVertices = len(vertices)
        tipoRelacao = linhas[numeroDeVertices + 1].strip().lower()
        grafo = None
        if (tipoRelacao == "*edges"):
            grafo = GrafoNaoDirigido(vertices)
        elif (tipoRelacao == "*arcs"):
            grafo = GrafoDirigido(vertices)
        else:
            raise Exception("Não foi possível identificar o tipo de grafo")

        LeitorGrafo.__lerRelacoes(linhas[numeroDeVertices + 2:], grafo)
        return grafo
    lerGrafoDoArquivo = staticmethod(lerGrafoDoArquivo)

    def __lerVertices(linhas):
        numeroDeVertices = int(linhas[0].split(" ")[1])
        vertices = []
        for i in range(1, numeroDeVertices + 1):
            linha = linhas[i]
            posicaoEspaco = linha.index(" ")
            numeroVertice = int(linha[0:posicaoEspaco])
            posicaoInicioRotulo = posicaoEspaco + 2
            posicaoFimRotulo = len(linha) - 2
            rotulo = linha[posicaoInicioRotulo:posicaoFimRotulo]
            vertices.append(Vertice(numeroVertice, rotulo))
        return vertices

    __lerVertices = staticmethod(__lerVertices)


    def __lerRelacoes(linhas, grafo: Grafo):
        for linha in linhas:
            valores = linha.split(" ")
            v1 = grafo.vertices[int(valores[0]) - 1]
            v2 = grafo.vertices[int(valores[1]) - 1]
            peso = 1
            if (len(valores) >= 3):
                peso = float(valores[2])
            grafo.adicionarRelacao(v1, v2, peso)
    __lerRelacoes = staticmethod(__lerRelacoes)
