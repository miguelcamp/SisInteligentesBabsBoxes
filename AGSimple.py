import random


class AGSimple:
    def __init__(self):
        self.cromosomas=[]
        self.bitlength=20

    def generar(self, tamP):
        for each in range(tamP):
            cromosoma=""
            for i in range(self.bitlength):
                cromosoma+=str(random.randint(0,1))
            self.cromosomas.append(cromosoma)

    def cromosoma_converge(self, cromosoma):
        for each in cromosoma:
            if each == "0":
                return False
        return True

    def converge(self):
        num_convergentes = 0
        for each in self.cromosomas:
            if self.cromosoma_converge(each):
                num_convergentes += 1
        if num_convergentes >= len(self.cromosomas)/2:
            return True
        return False

    def funcion_adaptacion(self, cromosoma):
        num_unos = 0
        for each in cromosoma:
            if each == "1":
                num_unos += 1
        return num_unos/self.bitlength

    def calcular_numero_cruces(self, Pc):
        return int(Pc * len(self.cromosomas))

    def cromosoma_mas_optimo(self):
        mejor_fa = 0
        mejor_cromosoma = None
        for each in self.cromosomas:
            if self.funcion_adaptacion(each) > mejor_fa:
                mejor_cromosoma = each
                mejor_fa = self.funcion_adaptacion(each)
        return mejor_cromosoma




print(random.randint(0,1))

AGS = AGSimple()
AGS.generar(9)
print(AGS.cromosomas[0])
print(AGS.cromosomas[1])
print(AGS.funcion_adaptacion(AGS.cromosomas[0]))
print(AGS.funcion_adaptacion(AGS.cromosomas[2]))
print(AGS.cromosoma_mas_optimo())
