import random


class Cromosoma:
    def __init__(self):
        self.genes = ""
        self.bitlength = 20
        self.edad = 0
        self.fa = 0

    def generar(self):
        self.genes=""
        for i in range(self.bitlength):
            self.genes += str(random.randint(0,1))
        self.calcular_fitness()

    def calcular_fitness(self):
        num_unos = 0
        for each in self.genes:
            if each == "1":
                num_unos += 1
        self.fa = num_unos / self.bitlength
        return num_unos / self.bitlength

    def mutar(self):
        probabilidad_mutacion = 0.001
        if random.random() < probabilidad_mutacion:
            pos = random.randint(0,self.bitlength-1)
            aux = list(self.genes)
            bit = aux[pos]
            if bit == '0':
                aux[pos] = '1'
            else:
                aux[pos] = '0'
            self.genes = "".join(aux)