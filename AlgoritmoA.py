
def busqueda_A(E_Ini, CReglas):
    EX = False
    Cam = None
    E_Ini.padre = None
    ABIERTOS = []
    ABIERTOS.append([E_Ini, E_Ini.f()])
    CERRADOS = []
    while len(ABIERTOS) != 0 and EX is False:
        Est_Act = Sacar_EstadoMF(ABIERTOS)
        CERRADOS.append(Est_Act)
        if (Est_Act.Cond_Term()):
            Cam = ConstruirCamino(Est_Act)
            EX = True
        else:
            RA= Reglas_aplicables(Est_Act)
            while len(RA) != 0:
                R = SacarRegla(RA)
                Est_Gen = Aplicar(R, Est_Act)
                if Est_Gen no

    pass
    return EX, Cam
