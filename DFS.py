import time
from NodoReinas import NodoReinas
nodos=0
def BusqProfundidad(EstInicial, EstSolucion):
    encontre= False
    Camino=[]
    nodos = 0
    encontre=BusqProfRecursiva(EstInicial, EstSolucion, Camino, encontre)
    return encontre, Camino
def BusqProfRecursiva(EstExplorado, EstSolucion, Camino, encontre):
    if(EstExplorado.condTerminacion()):
        encontre=True
        EstSolucion.copy(EstExplorado)
        Camino.insert(0,EstExplorado)
    else:
        ReglasAplicables=EstExplorado.EncontrarReglasAplicables()
        while len(ReglasAplicables)>0 and not encontre:
            R=ReglasAplicables.pop()
            EstNuevo=NodoReinas(N)
            EstNuevo.copy(EstExplorado)
            EstNuevo.AplicarRegla(R)
            global nodos
            nodos += 1
            if EstNuevo not in ListEstGen:
                EstNuevo.padre=EstExplorado
                EstExplorado.copy(EstNuevo)
                ListEstGen.insert(0,EstExplorado)
                Estado=NodoReinas(N)
                Estado.copy(EstExplorado)
                BusqProfRecursiva(Estado,EstSolucion, Camino, encontre)
        if encontre:
            Camino.insert(0,EstExplorado)

    return encontre

N=8


EstInicial=NodoReinas(N)
EstSolucion=NodoReinas(N)
ListEstGen=[EstInicial]
BusqProfundidad(EstInicial, EstSolucion)
print(EstSolucion.posiciones)
print("Nodos:", nodos)