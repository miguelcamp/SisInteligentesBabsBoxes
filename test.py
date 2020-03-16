box = []


def f1(n1, n2):
    aux1 = n1*10
    aux2 = n2*3
    return aux1, aux2

var1 = 2
var2 = 4

var1, var2 = f1(var1, var2)

print(var1,", ", var2)