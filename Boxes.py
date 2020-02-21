class Boxes:
    def __init__(self):
        self.boxlist=[]
        self.stack=[]
        self.dimensionDisp=[20,20]

    def copy(self, origin):
        self.boxlist= origin.boxlist.copy()


    def insert_box(self, box):
        self.boxlist.append(box)
        pass

    def AplicarRegla(self, R):
        pass ##TODO

    def Regla1(self, R):
        self.stack.append(R[1])
        self.dimensionDisp=[R[1][0],R[1][1]]

    def EncontrarReglasAplicables(self):
        pass ##TODO

    def condTerminacion(self):
        pass









n=10

Babs =Boxes()

Babs.insert_box([3,1,3])
