import os
import sys
import math
import ntpath
import time
#from numba import jit, njit
#import numpy as np

objetos = {}
clusters = []

def path_leaf(path):
	head, tail = ntpath.split(path)
	return tail or ntpath.basename(head)

''' ------------------------------------------------------------------------- '''
def calcular_distancia(c1, c2):
	menor_valor = 999999999
	for obj1 in c1:
		for obj2 in c2:
			sqrt = math.sqrt(((objetos[obj1][0]-objetos[obj2][0])**2)+((objetos[obj1][1]-objetos[obj2][1])**2))
			#sqrt = np.sqrt(((objetos[obj1][0]-objetos[obj2][0])**2)+((objetos[obj1][1]-objetos[obj2][1])**2))
			menor_valor = min(sqrt, menor_valor)

	return menor_valor

''' ------------------------------------------------------------------------- '''
def menor_distancia():
	i = j = 0
	min_i = min_j = 0
	menor_valor = 99999999
	qtd = len(matriz)
	for i in range(qtd):
	    for j in range(qtd):
	        if (i > j) and (matriz[i][j] < menor_valor):
	            menor_valor = matriz[i][j]
	            min_i = i
	            min_j = j
	return [min_i, min_j]

''' ------------------------------------------------------------------------- '''
def unir_clusters(i, j):
	clusters[j].extend(clusters[i])
	del clusters[i]

''' ------------------------------------------------------------------------- '''

#exec:		python single-link.txt file.txt kMin kMax
input_file = open(sys.argv[1], 'r')
input_name = path_leaf(sys.argv[1]).split(".")
kMin = int(sys.argv[2])
kMax = int(sys.argv[3])

linha = input_file.readline()
while True:
	linha = input_file.readline()
	if len(linha) == 0:
		break

	linha = linha.split('\n')
	linha = linha[0].split('\t')
	objetos.update({linha[0] : [float(linha[1]), float(linha[2])]})
	clusters.append([linha[0]])

start = time.time()
while len(clusters) > kMin:
	qtd = len(clusters)
	matriz = [
		[calcular_distancia(clusters[i], clusters[j]) if i > j else 0 for j in range(qtd)] for i in range(qtd)
	]
	min_dist = menor_distancia()
	unir_clusters(min_dist[0], min_dist[1])

	if len(clusters) == kMax:
		output_file = "./output/single-link/"+input_name[0]+"K"+str(kMax)+".clu"
		arquivo_saida = open(output_file, "w")
		#print('-- writing file: ' + output_file)

		for cluster in clusters:
			for item in cluster:
				arquivo_saida.write(item + "\t" + str(clusters.index(cluster)) + "\n")

		kMax = kMax - 1

print("Tempo --> ",time.time() - start)

sys.exit()
