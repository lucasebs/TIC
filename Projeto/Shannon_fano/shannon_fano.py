from numpy.lib.scimath import log2

class Elemento:
    """docstring for ClassName"""
    def __init__(self, valor):
        self.valor = valor
        self.auto_info = 0
        self.codigo = ''


    def __str___(self):
        return str(self.valor) + ', ' + str(self.codigo)

    def __repr__(self):
        return repr((self.valor, self.codigo))

def cria_elementos(conjunto):
    conjunto_aux = []
    soma = 0
    for elemento in conjunto:
        soma += elemento
        conjunto_aux.append(Elemento(elemento))

    for elemento in conjunto_aux:
        elemento.auto_info = auto_info(elemento.valor, soma)        
    
    return conjunto_aux    

def auto_info(freq, soma):
    prob = float(freq / soma)
    # auto_info = log2(1.0/prob)
    return log2(1.0/prob)


def max_p(conjunto):
    somatorio = 0
    for elemento in conjunto:
        somatorio += elemento.valor
    return somatorio

def entropia(conjunto):
    entropia = 0
    n = len(conjunto)
    for elemento in conjunto:
        entropia -= (elemento.valor/n* log2(elemento.valor/n))
    return entropia

def soma_elementos(conjunto):
    soma = 0
    for elemento in conjunto:
        soma += elemento.valor
    return soma


def shannon_fano(conjunto):
    prob = 0

    max_prob = 0
    max_prob = entropia(conjunto)
    conjunto1 = sorted(conjunto, key=lambda elemento: elemento.valor)
    conjunto0 = []

    # print("conjunto1")
    # for elemento in conjunto1:
    #     print(elemento.valor)

    aux = 0
    # while prob <= entropia(conjunto1):
    while (prob <= max_prob/2 or 
        # soma_elementos(conjunto0) < soma_elementos(conjunto1) or
        aux < soma_elementos(conjunto1)):
    # for elemento in conjunto1:
        # if soma_elementos(conjunto0) < soma_elementos(conjunto1):
        elemento = conjunto1.pop()
        conjunto0.append(elemento)
        prob = prob + elemento.auto_info
        # prob = prob + elemento.valor
        aux = soma_elementos(conjunto0) + conjunto1[-1].valor

    # if len(conjunto) == 2:
    #     elemento = conjunto1.pop()
    #     conjunto0.append(elemento)        
    
    # conjunto1 = sorted(conjunto_aux, key=lambda elemento: elemento.valor)

    # print("conjunto0")
    # for elemento in conjunto0:
    #     print(str(elemento.auto_info) + ' - ' + str(elemento.valor))

    # print("conjunto1")
    # for elemento in conjunto1:
    #     print(str(elemento.auto_info) + ' - ' + str(elemento.valor))

    # conjunto1 = sorted(conjunto1, key=lambda elemento: elemento.valor, reverse = True)


    # print("conj1")
    for elemento in conjunto1:
        elemento.codigo += '1'   
        # print(str(elemento.codigo) + ' - ' + str(elemento.valor))

    # print("conj0")
    for elemento in conjunto0:
        elemento.codigo += '0'
        # print(str(elemento.codigo) + ' - ' + str(elemento.valor))

    if len(conjunto0) > 1:
        shannon_fano(conjunto0)

    if len(conjunto1) > 1:
        shannon_fano(conjunto1)

    codigo = ''
    conjunto_f = []
    for elemento in conjunto1:
        conjunto_f.append(elemento)
    for elemento in conjunto0:
        conjunto_f.append(elemento)

    for elemento in sorted(conjunto_f, key=lambda elemento: elemento.valor, reverse = True):    
        for i in range(0,elemento.valor):
            codigo += elemento.codigo

    print(codigo)

def main():
    # F = [15,7,6,6,5]
	F = [6,5,4,3,2,1]
	# F = [6,5,2,1,1]
	F_aux = []
	F_el = cria_elementos(F)
	shannon_fano(F_el)


if __name__ == "__main__":
    main()