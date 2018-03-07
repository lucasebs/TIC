from numpy.lib.scimath import log2
# import binascii
# import codecs

class Elemento:
    """docstring for ClassName"""
    def __init__(self, valor, dado):
        self.valor = valor
        self.dado = dado
        self.codigo = ''
        self.auto_info = 0

    def __str___(self):
        return str(self.valor) + ', ' + str(self.codigo)

    def __repr__(self):
        return repr((self.valor, self.codigo))

# Read File #
def get_text():
	arq = open('text.txt', 'r')
	lines = arq.readlines()
	text = ''
	for line in lines:
		text += line
	return text

def write_text(name, text):
	file_name = name + ".txt"
	fl = open(file_name,"w") 
	fl.writelines(text) 
	fl.close() 

def get_chars(text):
	chars = []
	for char in text:
		chars.append(char)
		# if char is not "\n":
	 # 		chars.append(char)
	# print(chars)

	# words = text.split()
	# chars = []
	# # for word in words:
	# for char in text:
	# 	# for char in word:
 	# chars.append(char)

	return chars

def frequencia(text):
	chars = get_chars(text)
	charset = set(chars)
	freq_dict = {char: chars.count(char) for char in chars}
	# freq = []
	# for char in charset:
	# 	freq.append(freq_dict[char])
	# freq = cria_elementos(freq)
	# freq = cria_elementos(freq_dict, charset)
	# return freq
	return cria_elementos(freq_dict, set(chars))

# Encoding #
def cria_elementos(freq_dict, charset):
    freq = []
    soma = 0
    # for elemento in conjunto:
    #     soma += elemento
    #     conjunto_aux.append(Elemento(elemento))
    for char in charset:
    	soma += freq_dict[char]
    	freq.append(Elemento(freq_dict[char],char))

    for elemento in freq:
        elemento.auto_info = auto_info(elemento.valor, soma)        
    
    return freq

def auto_info(freq, soma):
    # prob = float(freq / soma)
    # auto_info = log2(1.0/prob)
    # return log2(1.0/prob)
    return log2(1.0/float(freq / soma))

def max_p(conjunto):
    somatorio = 0
    for elemento in conjunto:
        somatorio += elemento.valor
    return somatorio

def entropia(conjunto):
    entropia = 0
    # n = len(conjunto)
    for elemento in conjunto:
        entropia -= (elemento.valor/len(conjunto)* log2(elemento.valor/len(conjunto)))
    return entropia

def soma_elementos(conjunto):
    soma = 0
    for elemento in conjunto:
        soma += elemento.valor
    return soma

def get_codigo(conjunto, text):
	codigo = ''
	for char in text:
		for elemento in conjunto:
			if elemento.dado == char:
				codigo += elemento.codigo
	print(codigo)
	return codigo

def novo_arquivo(codigo):

	# Código adaptado de Shijun Hou: github.com/scotthou94/sf_comp/blob/master/shanno_fano_comp.py
	listofbytes = []
	for i in range(int(len(codigo)/8)):
		listofbytes.append(codigo[(i*8):(i*8+8)])
	lstlen = len(listofbytes[len(listofbytes)-1])

	if lstlen != 8:
		for i in range(8-lstlen):
			listofbytes[len(listofbytes)-1].append('0')

	dcmlst = []
	for strbyte in listofbytes:
		strbyte = bytearray(strbyte, 'utf-8')
		u = 0
		for i in range(8):
			u += (strbyte[i]-48)*2**(7-i) 
		dcmlst.append(u)

	arquivo_n = ''
	for f in bytearray(dcmlst):
		arquivo_n += chr(f)

	write_text('text_cod_bin', codigo)
	write_text('text_cod', arquivo_n)

	print(arquivo_n)

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

    # codigo = ''
    conjunto_f = []
    for elemento in conjunto1:
        conjunto_f.append(elemento)
    for elemento in conjunto0:
        conjunto_f.append(elemento)

    return conjunto_f

    # for elemento in sorted(conjunto_f, key=lambda elemento: elemento.valor, reverse = True):    
    #     for i in range(0,elemento.valor):
    #         codigo += elemento.codigo

    # # print(codigo)

    # return codigo
    

def main():
    
	# text = get_text()
	# F = frequencia(text)
	
	# conjunto = shannon_fano(frequencia(get_text()))
	
	# print()
	
	# # codigo = get_codigo(conjunto, text)

	# print(codigo)
	novo_arquivo(get_codigo(shannon_fano(frequencia(get_text())), get_text()))



if __name__ == "__main__":
    main()