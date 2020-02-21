import time
from NodoReinas import NodoReinas
##N Reinas
start = time.time()

best=0
N=20
NodosVisitados=0
##Búsq_Amplitud (EstInicial)🡪 Encontré, E_solución, Camino
EstInicial= NodoReinas(N)
Est_solucion=NodoReinas(N)
Camino=[]
##CrearCola () 🡪 cola
cola=[]
##CrearLista (EstInicial) 🡪 ListEstGenerados
ListEstGenerados={EstInicial}
##Poner_a_la_Cola (EstInicial, cola)
cola.append(EstInicial)
##Padre (EstInicial) 🡨 nulo
EstInicial.padre=None
#Encontré 🡨 No
encontre= False
ReglaAplicable=[]
##Mientras (NO (Vacía (cola))) y No (Encontré)), hacer
while(len(cola)>0 and not encontre):
    Est_Expl=NodoReinas(N)
    Est_Expl.copy(cola.pop())##Sacar_de_Cola (cola) 🡪 Est_Expl
    ReglaAplicable=Est_Expl.EncontrarReglasAplicables() ##ReglaAplicable 🡨 EncontrarReglaAplicable (Est_Expl)
    ##Mientras (ReglaAplicable no sea Ø) y No (Encontré)), hacer:
    while len(ReglaAplicable)!=0 and not encontre:
        ##SacarRegla (ReglaAplicable) 🡪 R
        R=ReglaAplicable.pop()
        ##E_Nuevo 🡨 Aplicar (R, Est_Expl)
        NodosVisitados+=1
        Est_Nuevo=NodoReinas(N)
        Est_Nuevo.copy(Est_Expl)
        Est_Nuevo.AplicarRegla(R)
        if R[1]>best:
            best=R[1]
            print ("New Best:",Est_Nuevo.posiciones)
        ##Si (No (Buscar (E_Nuevo, ListEstGen)))
        if Est_Nuevo not in ListEstGenerados:
            ##Padre (E_Nuevo) 🡨 Est_Expl
            Est_Nuevo.padre=Est_Expl
            ##Si (Cond_Term (E_Nuevo), entonces
            if Est_Nuevo.condTerminacion():
                print("Solucion")
                print(Est_Nuevo.posiciones)
                ##E_solución 🡨 E_Nuevo
                Est_solucion.copy(Est_Nuevo)
                ##ConstruirCamino (E_Nuevo) 🡪 Cam
                ##Encontré 🡨 Si
                encontre=True
            ##C/c  Insertar (E_Nuevo, ListEstGenerados)
            else:
                ListEstGenerados.add(Est_Nuevo)
                ##Poner_a_la_Cola (E_Nuevo, cola)
                cola.append(Est_Nuevo)
##Terminar devolviendo Encontré, E_solución, Cam

end = time.time()
print("Tiempo:",end - start)
print("Nodos visitados:",NodosVisitados)
Est_solucion.posiciones