import time
from Boxes import Boxes
NodosVisitados=0
class ListaTabu:
    def __init__(self, n):
        self.lista_estados = []
        self.tam_tabu = n

    def actualizar(self):
        for each in self.lista_estados:
            each[1] -= 1
            if each[1] == 0:
                del each

        while len(self.lista_estados) > self.tam_tabu:
            del self.lista_estados[0]

    def insertar(self, estado):
        self.lista_estados.append([estado, 10])

    def estado_existe(self, estado):
        existe = False
        for each in self.lista_estados:
            if each[0] == estado:
                existe = True
        return False


def busqueda_tabu(estado, num_iter):
    global NodosVisitados
    NodosVisitados = 0
    est_actual = Boxes()
    est_candidato = Boxes()
    est_nuevo = Boxes()
    est_mejor_por_ahora= Boxes()
    est_actual.copy(estado)
    lista_tabu = ListaTabu(10)
    lista_tabu.insertar(estado)
    est_mejor_por_ahora.copy(est_actual)
    valor_ant = est_actual.calcular_heuristica()
    j = 1
    exito = False
    while not est_actual.cond_terminacion() and j <= num_iter:
        reglas_aplicables=est_actual.encontrar_reglas_aplicables()
        tam = len(reglas_aplicables)
        num = 0
        for i in range(tam):
            R = reglas_aplicables[i]
            est_nuevo.copy(est_actual)
            est_nuevo.aplicar_regla(R)
            NodosVisitados+=1
            valor = calcular_h(est_nuevo)
            if not lista_tabu.estado_existe(est_nuevo):
                if valor > est_mejor_por_ahora.calcular_heuristica():
                    est_mejor_por_ahora.copy(est_nuevo)
                    num = i
                elif valor>valor_ant or tam == 1:
                    est_candidato.copy(est_nuevo)
                    num = 0
                    valor_ant = valor
        if num == 0:
            est_mejor_por_ahora.copy(est_candidato)
            pass
        lista_tabu.actualizar()
        lista_tabu.insertar(est_mejor_por_ahora)
        est_actual.copy(est_mejor_por_ahora)
        j += 1
    if est_actual.cond_terminacion():
        exito = True
        print(est_actual.stack)
    return est_mejor_por_ahora


def calcular_h(estado):
    h = estado.calcular_heuristica()
    return h


start = time.time()
millis = int(round(time.time() * 1000))

#Inicializando variables
#Estados y Listas Iniciales
EstInicial= Boxes()
EstInicial.leer_entradas("entradas.txt")
Est_solucion=Boxes()
MejorSolucion=Boxes()

Est_solucion = busqueda_tabu(EstInicial, 100)

end = time.time()
millis_end = int(round(time.time() * 1000))
print("Estado Inicial: ",EstInicial.boxlist)
print("Tiempo(ms):", end-start)
print("Mejor Numero de Cajas: ", Est_solucion.calcular_heuristica())
print("Mejor Solucion: ", Est_solucion.stack)
print("Nodos Visitados:", NodosVisitados)

