import random


class Cromosoma:
    def __init__(self):
        self.genes = ""
        self.bitlength = 20
        self.edad = 0

    def generar(self):
        self.genes=""
        for i in range(self.bitlength):
            self.genes += str(random.randint(0,1))

    def calcular_fitness(self):
        num_unos = 0
        for each in self.genes:
            if each == "1":
                num_unos += 1
        return num_unos / self.bitlength
