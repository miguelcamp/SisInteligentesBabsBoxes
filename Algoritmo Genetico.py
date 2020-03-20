from AGSimple import AGSimple
import time
import random

iteraciones = 0
def AlgoritmoGenetico(tam):
    P = AGSimple()
    P.generar(tam)
    P.funcion_adaptacion()
    converge = False
    global iteraciones
    iteraciones = 0
    probabilidad_cruce = 0.7
    while not converge:
        N = P.calcular_numero_cruces(probabilidad_cruce)
        PDi=[]
        for x in range(N):
            I1, I2 = P.seleccionar_par()
            D1, D2 = P.cruzar(I1, I2)
            D1.mutar()
            D2.mutar()
            D1.calcular_fitness()
            D2.calcular_fitness()
            PDi.append(D1)
            PDi.append(D2)
        for each in PDi:
            P.insertar(each)
        if P.converge():
            converge= True
        else:
            P.reducir(tam)
            iteraciones += 1

    return P.cromosoma_mas_optimo()

def AlgoritmoGeneticoSinCruces(tam):
    P = AGSimple()
    P.generar(tam)
    P.funcion_adaptacion()
    converge = False
    global iteraciones
    iteraciones = 0
    probabilidad_cruce = 0.7
    while not converge:
        N = P.calcular_numero_cruces(probabilidad_cruce)
        PDi=[]
        cromosoma = random.choice(P.cromosomas)
        cromosoma.mutar()
        for each in PDi:
            P.insertar(each)
        if P.converge():
            converge= True
        else:
            P.reducir(tam)
            iteraciones += 1

    return P.cromosoma_mas_optimo()


def correr_n_veces(n):
    suma_tiempo = 0
    suma_iteraciones = 0
    for i in range (n):
        start = time.time()
        mejor = AlgoritmoGenetico(100)
        end = time.time()
        duration = end - start
        #print(mejor.genes)
        suma_tiempo+= duration
        suma_iteraciones+=iteraciones
        print("Tiempo", i + 1, ": ", round(duration, 4))
        print("Iteraciones: ", iteraciones)
    print("Promedio Tiempo: ", suma_tiempo/n)
    print("Promedio Iteraciones: ", suma_iteraciones/n)

def correr_n_veces_sin_cruces(n):
    suma_tiempo = 0
    suma_iteraciones = 0
    for i in range (n):
        start = time.time()
        mejor = AlgoritmoGenetico(100)
        end = time.time()
        duration = end - start
        #print(mejor.genes)
        suma_tiempo+= duration
        suma_iteraciones+=iteraciones
        print("Tiempo", i + 1, ": ", round(duration, 4))
        print("Iteraciones: ", iteraciones)
    print("Promedio Tiempo: ", suma_tiempo/n)
    print("Promedio Iteraciones: ", suma_iteraciones/n)

correr_n_veces_sin_cruces(20)
#correr_n_veces(20)