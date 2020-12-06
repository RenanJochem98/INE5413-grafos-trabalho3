from GrafoNaoDirigido import GrafoNaoDirigido
from Aresta import Aresta
from ConjuntoIndependenteMaximal import ConjuntoIndependenteMaximal

class GrafoBipartido(GrafoNaoDirigido):

    def __init__(self, vertices):
        super().__init__(vertices)
        self.X = []
        self.Y = []

    def obterTipoGrafo(self):
        return "Grafo bipartido"

    def lerParticoes(self):
        ig = ConjuntoIndependenteMaximal.buscar(self.vertices)
        for i, c in enumerate(ig):
            if c == 1:
                self.X.append(self.vertices[i])
            else:
                self.Y.append(self.vertices[i])