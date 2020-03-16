class Boxes:
    def __init__(self):
        self.boxlist = []
        self.stack = []
        self.ancho_disp = 20
        self.largo_disp = 20
        self.max_cajas=0
        self.padre = None

    def copy(self, origin):
        self.boxlist = origin.boxlist.copy()
        self.stack=origin.stack.copy()
        self.ancho_disp=origin.ancho_disp
        self.largo_disp=origin.largo_disp
        self.max_cajas=origin.max_cajas
        self.padre = origin.padre

    def insert_box(self, box):
        self.boxlist.append(box)

    def aplicar_regla(self, regla):
        if regla[0] == 1:
            self.apilar_caja(regla[1])
        elif regla[0] == 2:
            self.desapilar_caja()

    def apilar_caja(self, indice_caja):
        ancho_expl = self.boxlist[indice_caja][0]
        largo_expl = self.boxlist[indice_caja][1]
        alto_expl = self.boxlist[indice_caja][2]
        if self.ancho_disp >= ancho_expl and self.largo_disp >= largo_expl:
            self.stack.append([ancho_expl, largo_expl, alto_expl])
            self.ancho_disp = ancho_expl
            self.largo_disp = largo_expl
            orientacion = 1
        elif self.ancho_disp >= ancho_expl and self.largo_disp >= alto_expl:
            self.stack.append([ancho_expl, alto_expl, largo_expl])
            self.ancho_disp = ancho_expl
            self.largo_disp = alto_expl
            orientacion = 2
        elif self.ancho_disp >= largo_expl and self.largo_disp >= alto_expl:
            self.stack.append([largo_expl, alto_expl, ancho_expl])
            self.ancho_disp = largo_expl
            self.largo_disp = alto_expl
            orientacion = 3

        del self.boxlist[indice_caja]
        self.max_cajas += 1

    def desapilar_caja(self):
        aux_caja= self.stack.pop()
        self.max_cajas -= 1
        self.insert_box(aux_caja)
        if len(self.stack) == 0:
            self.ancho_disp = 20
            self.largo_disp = 20
        else:
            self.ancho_disp = self.stack[-1][0]
            self.largo_disp = self.stack[-1][1]

    def encontrar_reglas_aplicables(self):
        reglas = []
        if len(self.stack) > 0:
            reglas.append([2])
        for each in self.boxlist:
            ancho_expl = each[0]
            largo_expl = each[1]
            alto_expl = each[2]
            if self.ancho_disp >= ancho_expl and self.largo_disp >= largo_expl:
                reglas.append([1,self.boxlist.index(each)])
                orientacion = 1
            elif self.ancho_disp >= ancho_expl and self.largo_disp >= alto_expl:
                reglas.append([1,self.boxlist.index(each)])
                orientacion = 2
            elif self.ancho_disp >= largo_expl and self.largo_disp >= alto_expl:
                reglas.append([1,self.boxlist.index(each)])
                orientacion = 3
        return reglas

    def cond_terminacion(self):
        return len(self.boxlist) == 0

    def leer_entradas(self, direccion):
        f = open(direccion, "r")
        data = f.readlines()
        f.close()
        n = data.pop(0)
        for x in range(int(n)):
            results = data.pop(0).split()
            results = list(map(int, results))
            self.insert_box(results)

    def calcular_opciones(self):
        cajas_apilables = 0
        for each in self.boxlist:
            ancho_expl = each[0]
            largo_expl = each[1]
            alto_expl = each[2]
            if self.ancho_disp >= ancho_expl and self.largo_disp >= largo_expl:
                cajas_apilables += 1
            elif self.ancho_disp >= ancho_expl and self.largo_disp >= alto_expl:
                cajas_apilables += 1
            elif self.ancho_disp >= largo_expl and self.largo_disp >= alto_expl:
                cajas_apilables += 1
        return cajas_apilables

    def calcular_heuristica(self):
        cajas_apilables = 0
        for each in self.boxlist:
            ancho_expl = each[0]
            largo_expl = each[1]
            alto_expl = each[2]
            if self.ancho_disp >= ancho_expl and self.largo_disp >= largo_expl:
                cajas_apilables += 1
            elif self.ancho_disp >= ancho_expl and self.largo_disp >= alto_expl:
                cajas_apilables += 1
            elif self.ancho_disp >= largo_expl and self.largo_disp >= alto_expl:
                cajas_apilables += 1
        return self.max_cajas
