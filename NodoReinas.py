class NodoReinas:
    def __init__(self, n):
        # Fila de Reina para cada columna
        self.N = n
        self.padre = None
        self.posiciones = []
        for i in range(self.N):
            self.posiciones.append(0)

    def copy(self, origin):
        self.N = origin.N
        self.padre = origin.padre
        self.posiciones = origin.posiciones.copy()

    def numReinas(self):
        for i in range(len(self.posiciones)):
            if self.posiciones[i] == 0:
                return i
        return self.N

    def esPosicionLibre(self, ColExpl, FilExpl):
        res = True
        if int(self.posiciones[ColExpl - 1]) > 0:  # Misma Columna
            res = False
        for col in range(ColExpl):  # Itera sobre cada columna hasta la explorada sin incluirla
            if int(self.posiciones[col]) == FilExpl:  # Misma Fila
                res = False
            if FilExpl == int(self.posiciones[col]) - (ColExpl - 1 - col) and self.posiciones[
                col] != 0:  # Diagonal hacia abajo
                res = False
            if FilExpl == int(self.posiciones[col]) + (ColExpl - 1 - col) and self.posiciones[
                col] != 0:  # Diagonal hacia arriba
                res = False
        return res

    def EncontrarReglasAplicables(self):
        R = []
        # Si hay menos de N reinas:
        if self.numReinas() < self.N:
            FilExpl = 1
            ColExpl = self.numReinas() + 1
            EspacioEncontrado = False
            while (FilExpl <= self.N):
                # EspacioEncontrado=self.esPosicionLibre(FilExpl,ColExpl)
                if self.esPosicionLibre(ColExpl, FilExpl):
                    R.append([1, ColExpl, FilExpl])
                FilExpl += 1
        return R

    def AplicarRegla(self, R):
        if (R[0] == 1):
            self.posiciones[R[1] - 1] = R[2]

    def esPosicionLibreDebug(self, FilExpl, ColExpl):
        res = str(FilExpl) + "," + str(ColExpl)
        if int(self.posiciones[ColExpl - 1]) > 0:  # Misma Col
            res = "Col"
        for col in range(ColExpl):
            if int(self.posiciones[col]) == FilExpl:  # Misma Fila
                res = "Fila"
            if FilExpl == int(self.posiciones[col]) - (ColExpl - 1 - col) and self.posiciones[col] != "0":  # Diag Up
                res = "DiagUp"
            if FilExpl == int(self.posiciones[col]) + (ColExpl - 1 - col) and self.posiciones[col] != "0":  # Diag Dn
                res = "DiagDn"
        return res

    def condTerminacion(self):
        if self.numReinas() == self.N:
            return True
        else:
            return False


