import time
from Boxes import Boxes

start = time.time()

#Inicializando variables
best=0
NodosVisitados=0
#Estados y Listas Iniciales
EstInicial= Boxes()
EstInicial.leer_entradas("entradas.txt")

Est_solucion=Boxes()
MejorSolucion=Boxes()
Camino=[]
cola=[]
ListEstGenerados={EstInicial}
cola.append(EstInicial)
EstInicial.padre=None

encontre= False
ReglaAplicable=[]

while(len(cola)>0 ):
    Est_Expl=Boxes()
    Est_Expl.copy(cola.pop())
    ReglaAplicable=Est_Expl.encontrar_reglas_aplicables()
    while len(ReglaAplicable)!=0 :
        R=ReglaAplicable.pop()
        NodosVisitados+=1
        Est_Nuevo=Boxes()
        Est_Nuevo.copy(Est_Expl)
        Est_Nuevo.aplicar_regla(R)

        ##Si (No (Buscar (E_Nuevo, ListEstGen)))
        if Est_Nuevo not in ListEstGenerados:
            ##Padre (E_Nuevo) 🡨 Est_Expl
            Est_Nuevo.padre=Est_Expl
            ##Si (Cond_Term (E_Nuevo), entonces
            if Est_Nuevo.cond_terminacion():
                Est_solucion.copy(Est_Nuevo)
                if Est_solucion.max_cajas>MejorSolucion.max_cajas :
                    MejorSolucion.copy(Est_solucion)
                ##ConstruirCamino (E_Nuevo) 🡪 Cam
                encontre=True
            else:
                ListEstGenerados.add(Est_Nuevo)
                cola.append(Est_Nuevo)

end = time.time()
print("Estado Inicial: ",EstInicial.boxlist)
print("Tiempo:",end - start)
print("Maximo numero de cajas en la pila: ",MejorSolucion.max_cajas)
print("Mejor Solucion: ", MejorSolucion.stack)


