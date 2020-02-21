import time
from Boxes import Boxes
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
            EstNuevo=Boxes(N)
            EstNuevo.copy(EstExplorado)
            EstNuevo.AplicarRegla(R)
            global nodos
            nodos += 1
            if EstNuevo not in ListEstGen:
                EstNuevo.padre=EstExplorado
                EstExplorado.copy(EstNuevo)
                ListEstGen.insert(0,EstExplorado)
                Estado=Boxes(N)
                Estado.copy(EstExplorado)
                BusqProfRecursiva(Estado,EstSolucion, Camino, encontre)
        if encontre:
            Camino.insert(0,EstExplorado)

    return encontre

N=6


EstInicial=Boxes(N)
EstSolucion=Boxes(N)
ListEstGen=[EstInicial]
BusqProfundidad(EstInicial, EstSolucion)
print(EstSolucion.posiciones)
print("Nodos:", nodos)