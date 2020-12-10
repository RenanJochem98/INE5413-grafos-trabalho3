# from Grafo import Grafo
from GrafoExecutor import GrafoExecutor
from GrafoDirigido import GrafoDirigido
from GrafoNaoDirigido import GrafoNaoDirigido
from LeitorGrafo import LeitorGrafo

# g = Grafo()
# arquivo = "arquivos-teste/manha_ord_topologica.net"
# arquivo = "arquivos-teste/ord_topologica.net"
# arquivo = "arquivos-teste/fortemente_contexo_aula.net"
# arquivo = "arquivos-teste/kruskal.net"
# arquivo = "arquivos-teste/tcc_completo.net"
# arquivo = "arquivos-teste/agm_tiny_aresta.net"
# arquivo = "arquivos-teste/agm_tiny_arco.net"
# arquivo = "arquivos-teste/fluxo_maximo/db5.gr"
# arquivo = "arquivos-teste/emparelhamento_maximo/pequeno.gr"
# arquivo = "arquivos-teste/pequenas/karate.net"
# arquivo = "arquivos-teste/caminho_minimo/fln_pequena.net"
# arquivo = "arquivos-teste/coloracao_minima/maquinas.net"

global grafo
grafo = None
#grafo = LeitorGrafo.lerGrafoDoArquivo(arquivo, True)
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
        v = solicitarOpcao(texto, 1, exec.qtdVertices(grafo))
        if v > 0:
            return v
        else:
            print("Você não digitou um vértice válido")
    except Exception as ex:
        print(ex)
        return 0

def carregarArquivo():
    _carregarArquivo(False)

def carregarGrafoBipartido():
    _carregarArquivo(True)

def _carregarArquivo(bipartido: bool):
    arquivoPadrao = "arquivos-teste/grafo.teste.net" if not bipartido else "arquivos-teste/emparelhamento_maximo/pequeno.gr"
    arquivo = input("Digite o nome do arquivo (em branco carrega " + arquivoPadrao + "): ")
    try:
        if arquivo == "":
            arquivo = arquivoPadrao
        global grafo
        grafo = LeitorGrafo.lerGrafoDoArquivo(arquivo, bipartido)
        print("Arquivo " + arquivo + " carregado com sucesso.")
    except Exception as ex:
        print("Não foi possível ler o arquivo!")
        print(ex)

def verificarSeCarregouArquivo():
    if grafo == None:
        raise Exception("Você precisa carregar um arquivo de grafo antes de continuar!")

def mostrarGrafo():
    verificarSeCarregouArquivo()
    print('Mostrando o grafo:')
    grafo.mostrarGrafo()

def mostrarQtdVertices():
    verificarSeCarregouArquivo()
    numVertices = exec.qtdVertices(grafo)
    print("O grafo tem " + str(numVertices) + " vertices.")

def mostrarQtdRelacoes():
    verificarSeCarregouArquivo()
    numRelacoes = exec.qtdRelacoes(grafo)
    print("O grafo tem " + str(numRelacoes) + " arestas.")

def verGrau():
    verificarSeCarregouArquivo()
    v = solicitarVertice()
    if v > 0:
        grau = exec.grau(grafo, v)
        print(f'Grau do vértice {v}:', grau)

def verRotulo():
    verificarSeCarregouArquivo()
    v = solicitarVertice()
    if v > 0:
        rotulo = exec.rotulo(grafo, v)
        print(f'Rótulo do vértice {v}:', rotulo)

def verVizinhos():
    verificarSeCarregouArquivo()
    v = solicitarVertice()
    if v > 0:
        vizinhos = exec.vizinhos(grafo, v)
        print(f'Vizinhos do vértice {v}:', ", ".join(map(lambda v: str(v.numero), vizinhos)))

def verificarSeHaRelacao():
    verificarSeCarregouArquivo()
    v = solicitarVertice("Digite o número do primeiro vértice: ")
    u = solicitarVertice("Digite o número do segundo vértice: ")
    if v > 0 and u > 0:
        haRelacao = exec.haRelacao(grafo, u, v)
        nao = "" if haRelacao else " não"
        print(f'O vértice {v}{nao} possui uma relacao para {u}')

def encontrarFluxoMaximo():
    verificarSeCarregouArquivo()
    s = solicitarVertice("Digite o número do vértice de origem (s): ")
    t = solicitarVertice("Digite o número do vértice de destino (t): ")
    if s > 0 and t > 0:
        print("Buscando fluxo máximo entre s =", s, "e t =", t)
        fluxoMaximo = exec.buscarFluxoMaximo(grafo, s, t)
        print('Fluxo máximo:', fluxoMaximo)

def encontrarEmparelhamentoMaximo():
    verificarSeCarregouArquivo()
    print("Buscando emparelhamento máximo")
    emparelhamentoMax = exec.buscarEmparelhamentoMaximo(grafo)
    print('emparelhamentoMax:', emparelhamentoMax)

def encontrarColoracaoMinima():
    verificarSeCarregouArquivo()
    print("Buscando coloração mínima")
    coloracaoMinima = exec.buscarColoracaoMinima(grafo)
    print('coloracaoMinima:', coloracaoMinima)

# lista com funcoes que serao executadas
acoes = [
    {"texto": "Carregar um arquivo", "funcao": carregarArquivo},
    {"texto": "Carregar arquivo de Grafo BIPARTIDO", "funcao": carregarGrafoBipartido},
    {"texto": "Mostrar o grafo", "funcao": mostrarGrafo},
    {"texto": "Ver a quantidade de Vértices", "funcao": mostrarQtdVertices},
    {"texto": "Ver a quantidade de Relacoes", "funcao": mostrarQtdRelacoes},
    {"texto": "Grau do vértice", "funcao": verGrau},
    {"texto": "Rótulo do vértice", "funcao": verRotulo},
    {"texto": "Vizinhos do vértice", "funcao": verVizinhos},
    {"texto": "Buscar Fluxo Máximo", "funcao": encontrarFluxoMaximo},
    {"texto": "Buscar Emparelhamento Máximo", "funcao": encontrarEmparelhamentoMaximo},
    {"texto": "Buscar Coloração Mínima", "funcao": encontrarColoracaoMinima}
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
            try:
                acoes[user_input - 1]["funcao"]()
            except Exception as ex:
                print(ex)

            print()
            input('Pressione ENTER para continuar...')
        else:
            user_input = 0

# fim while
print()
print("Programa finalizado")
