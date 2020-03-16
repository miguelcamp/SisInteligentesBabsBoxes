import time
from Boxes import Boxes
nodos=0
def BusqProfundidad(EstInicial, EstSolucion):
    encontre= False
    Camino=[]
    encontre=BusqProfRecursiva(EstInicial, EstSolucion, Camino, encontre)
    return encontre, Camino
def BusqProfRecursiva(EstExplorado, EstSolucion, Camino, encontre):
    if(EstExplorado.cond_terminacion()):
        encontre=True
        EstSolucion.copy(EstExplorado)
        Camino.insert(0,EstExplorado)
    else:
        ReglasAplicables=EstExplorado.encontrar_reglas_aplicables()
        while len(ReglasAplicables)>0 and not encontre:
            R=ReglasAplicables.pop()
            EstNuevo=Boxes()
            EstNuevo.copy(EstExplorado)
            EstNuevo.aplicar_regla(R)
            global nodos
            nodos += 1
            if EstNuevo not in ListEstGen:
                EstNuevo.padre = EstExplorado
                EstExplorado.copy(EstNuevo)
                ListEstGen.insert(0,EstExplorado)
                Estado=Boxes()
                Estado.copy(EstExplorado)
                BusqProfRecursiva(Estado,EstSolucion, Camino, encontre)
        if encontre:
            Camino.insert(0,EstExplorado)

    return encontre

N=6

n=10




EstInicial=Boxes()
EstInicial.leer_entradas("entradas.txt")
EstSolucion=Boxes()
ListEstGen=[EstInicial]
BusqProfundidad(EstInicial, EstSolucion)
print(EstSolucion.stack)
print("Nodos:", nodos)