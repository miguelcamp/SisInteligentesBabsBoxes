import random
from Cromosoma import Cromosoma


class AGSimple:
    def __init__(self):
        self.cromosomas=[]
        self.bitlength=20

    def generar(self, tamP):
        for each in range(tamP):
            nuevo = Cromosoma()
            nuevo.generar()
            self.cromosomas.append(nuevo)

    def funcion_adaptacion(self):
        for each in self.cromosomas:
            each.calcular_fitness()

    def insertar(self, cromosoma):
        self.cromosomas.append(cromosoma)

    def converge(self):
        num_convergentes = 0
        for each in self.cromosomas:
            if each.calcular_fitness() == 1:
                num_convergentes += 1
        if num_convergentes >= len(self.cromosomas)/2:
            return True
        return False

    def calcular_numero_cruces(self, Pc):
        return int(Pc * len(self.cromosomas))

    def cromosoma_mas_optimo(self):
        mejor_fa = 0
        mejor_cromosoma = None
        for each in self.cromosomas:
            if each.calcular_fitness() > mejor_fa:
                mejor_cromosoma = each
                mejor_fa = each.calcular_fitness()
        return mejor_cromosoma

    def seleccionar_par(self):
        seleccionables=[]
        for each in self.cromosomas:
            probabilidad = round(each.fa, 2)*100
            for i in range(int(probabilidad)+1):
                seleccionables.append(each)
        seleccion1 = random.choice(seleccionables)
        seleccion2 = random.choice(seleccionables)
        return seleccion1, seleccion2

    def cruzar(self, I1, I2):
        D1 = Cromosoma()
        D2 = Cromosoma()
        midpoint = random.randint(1,self.bitlength - 2)
        mitad_i1_ini = I1.genes[:midpoint]
        mitad_i1_fin = I1.genes[midpoint:]
        mitad_i2_ini = I2.genes[:midpoint]
        mitad_i2_fin = I2.genes[midpoint:]
        genes_cruzados1 = mitad_i1_ini + mitad_i2_fin
        genes_cruzados2 = mitad_i2_ini + mitad_i1_fin
        D1.genes = genes_cruzados1
        D2.genes = genes_cruzados2
        return D1, D2

    def reducir(self, tam):
        while len(self.cromosomas) > tam:
            self.cromosomas.pop(0)
