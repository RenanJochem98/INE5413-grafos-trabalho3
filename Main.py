# from Grafo import Grafo
from GrafoExecutor import GrafoExecutor
from GrafoDirigido import GrafoDirigido
from GrafoNaoDirigido import GrafoNaoDirigido
from LeitorGrafo import LeitorGrafo

# g = Grafo()
# arquivo = "arquivos-teste/manha_ord_topologica.net"
# arquivo = "arquivos-teste/ord_topologica.net"
# arquivo = "arquivos-teste/fortemente_contexo_aula.net"
arquivo = "arquivos-teste/kruskal.net"
# arquivo = "arquivos-teste/tcc_completo.net"
# arquivo = "arquivos-teste/agm_tiny_aresta.net"
# arquivo = "arquivos-teste/agm_tiny_arco.net"
global grafo
grafo = LeitorGrafo.lerGrafoDoArquivo(arquivo)
exec = GrafoExecutor()

def solicitarOpcao(texto, min, max, maxTentativas = 3):
    tentativas = 1
    while tentativas <= maxTentativas:
        try:
            opcao = int(input(texto))
            if opcao >= min and opcao <= max:
                return opcao
            else:
                raise Exception()
        except:
            print("Opção inválida. Digite um valor entre " + str(min) + " e " + str(max))

        tentativas += 1

    return min - 1

def solicitarVertice(texto="Digite o número do vertice: "):
    try:
        v = solicitarOpcao(texto, 1, exec.qtdVertices(g))
        if v > 0:
            return v
        else:
            print("Você não digitou um vértice válido")
    except Exception as ex:
        print(ex)
        return 0

def carregarArquivo():
    arquivoPadrao = "grafo.teste.net"
    arquivo = input("Digite o nome do arquivo (em branco carrega " + arquivoPadrao + "): ")
    try:
        if arquivo == "":
            arquivo = arquivoPadrao
        global grafo
        grafo = LeitorGrafo.lerGrafoDoArquivo(arquivo)
        print("Arquivo " + arquivo + " carregado com sucesso.")
    except Exception as ex:
        print("Não foi possível ler o arquivo!")
        print(ex)

def mostrarGrafo():
    try:
        print('Mostrando o grafo:')
        grafo.mostrarGrafo()
    except Exception as ex:
        print(ex)


def mostrarQtdVertices():
    numVertices = exec.qtdVertices(grafo)
    print("O grafo tem " + str(numVertices) + " vertices.")

def mostrarQtdRelacoes():
    numRelacoes = exec.qtdRelacoes(grafo)
    print("O grafo tem " + str(numRelacoes) + " arestas.")

def verGrau():
    v = solicitarVertice()
    if v > 0:
        grau = exec.grau(grafo, v)
        print(f'Grau do vértice {v}:', grau)

def verRotulo():
    v = solicitarVertice()
    if v > 0:
        rotulo = exec.rotulo(grafo, v)
        print(f'Rótulo do vértice {v}:', rotulo)

def verVizinhos():
    v = solicitarVertice()
    if v > 0:
        vizinhos = exec.vizinhos(grafo, v)
        print(f'Vizinhos do vértice {v}:', ", ".join(map(lambda v: str(v.numero), vizinhos)))

def verificarSeHaRelacao():
    v = solicitarVertice("Digite o número do primeiro vértice: ")
    u = solicitarVertice("Digite o número do segundo vértice: ")
    if v > 0 and u > 0:
        haRelacao = exec.haRelacao(grafo, u, v)
        nao = "" if haRelacao else " não"
        print(f'O vértice {v}{nao} possui uma relacao para {u}')


# lista com funcoes que serao executadas
acoes = [
    {"texto": "Carregar um arquivo", "funcao": carregarArquivo},
    {"texto": "Mostrar o grafo", "funcao": mostrarGrafo},
    {"texto": "Ver a quantidade de Vértices", "funcao": mostrarQtdVertices},
    {"texto": "Ver a quantidade de Relacoes", "funcao": mostrarQtdRelacoes},
    {"texto": "Grau do vértice", "funcao": verGrau},
    {"texto": "Rótulo do vértice", "funcao": verRotulo},
    {"texto": "Vizinhos do vértice", "funcao": verVizinhos}
]

user_input = -1
while user_input != 0:

        print()
        print("Menu: ")
        for i, acao in enumerate(acoes):
            print(str(i + 1) +" - " + acao["texto"])
        print("0 - Finalizar o programa")
        print()

        user_input = solicitarOpcao("Digite a opção desejada: ", 0, len(acoes))
        print()
        if user_input > 0:
            acoes[user_input - 1]["funcao"]()
            print()
            input('Pressione ENTER para continuar...')
        else:
            user_input = 0

# fim while
print()
print("Programa finalizado")
