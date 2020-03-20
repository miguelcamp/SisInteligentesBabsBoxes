def AlgoritmoGenetico(P, Tam):
    P.generar(Tam)
    Pc = 0.7
    P.funcion_adaptacion()
    converge = False
    while not Converge:
        N = P.calcular_numero_cruces(Pc)
        for x in range(N):
            I1, I2 = P.seleccionar()
            D1, D2 = P.cruzar(I1, I2)
            D1 = mutar(D1)
            D2 = mutar(D2)
            aplicar_fa(D1)
            aplicar_fa(D2)
            insertar()
        P = Union(Pi, PDi)
        if P.converge():
            converge= True
        else:
            reducir(P)
    return x