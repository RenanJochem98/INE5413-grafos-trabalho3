from Vertice import Vertice
from Grafo import Grafo
from GrafoDirigido import GrafoDirigido
from GrafoNaoDirigido import GrafoNaoDirigido
from GrafoBipartido import GrafoBipartido

class LeitorGrafo:

    def lerGrafoDoArquivo(arquivo: str, bipartido: bool = False):
        if arquivo.lower().endswith(".net"):
            return LeitorGrafo.lerGrafoDoArquivoNet(arquivo)
        elif arquivo.lower().endswith(".gr"):
            return LeitorGrafo.lerGrafoDoArquivoGr(arquivo, bipartido)
        else:
            raise Exception("Formato de arquivo desconhecido")
    lerGrafoDoArquivo = staticmethod(lerGrafoDoArquivo)

    def lerGrafoDoArquivoNet(arquivo: str):
        f = open(arquivo, "r", encoding='utf-8')
        linhas = f.readlines()
        f.close()

        vertices = LeitorGrafo.__lerVerticesNet(linhas)
        numeroDeVertices = len(vertices)
        tipoRelacao = linhas[numeroDeVertices + 1].strip().lower()
        grafo = None
        if (tipoRelacao == "*edges"):
            grafo = GrafoNaoDirigido(vertices)
        elif (tipoRelacao == "*arcs"):
            grafo = GrafoDirigido(vertices)
        else:
            raise Exception("Não foi possível identificar o tipo de grafo")

        LeitorGrafo.__lerRelacoesNet(linhas[numeroDeVertices + 2:], grafo)
        return grafo

    lerGrafoDoArquivoNet = staticmethod(lerGrafoDoArquivoNet)

    def __lerVerticesNet(linhas):
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
    __lerVerticesNet = staticmethod(__lerVerticesNet)


    def __lerRelacoesNet(linhas, grafo: Grafo):
        for linha in linhas:
            valores = linha.split(" ")
            v1 = grafo.vertices[int(valores[0]) - 1]
            v2 = grafo.vertices[int(valores[1]) - 1]
            peso = 1
            if (len(valores) >= 3):
                peso = float(valores[2])
            grafo.adicionarRelacao(v1, v2, peso)
    __lerRelacoesNet = staticmethod(__lerRelacoesNet)


    def lerGrafoDoArquivoGr(arquivo: str, bipartido: bool):
        f = open(arquivo, "r", encoding='utf-8')
        linhas = f.readlines()
        f.close()
        
        grafo = None
        for i in range(0, len(linhas)):
            valores = linhas[i].split(" ")
            if valores[0] == "p":
                numVertices = int(valores[2])
                vertices = list(map(lambda v: Vertice(v, str(v)), range(1, numVertices + 1)))
                if valores[1] == "max":
                    grafo = GrafoDirigido(vertices)
                elif valores[1] == "edge":
                    if bipartido:
                        grafo = GrafoBipartido(vertices)
                    else:
                        grafo = GrafoNaoDirigido(vertices)
            elif valores[0] == "a" or valores[0] == "e":
                v1 = grafo.vertices[int(valores[1]) - 1]
                v2 = grafo.vertices[int(valores[2]) - 1]
                peso = 1
                if (len(valores) >= 4):
                    peso = float(valores[3])
                grafo.adicionarRelacao(v1, v2, peso)

        if bipartido:
            grafo.lerParticoes()

        return grafo
    lerGrafoDoArquivoGr = staticmethod(lerGrafoDoArquivoGr)