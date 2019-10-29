#requires python 3.7

#College ID
####################################################
# Nome: Daniel Liberato de Jesus    RA: 552127     #
# Nome:       RA:      #
# Nome:       RA:      #
# Nome:       RA:      #
####################################################

import os
import sys
import math
import random
import ntpath

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

# Classe Objeto
class Objeto:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.current_cluster = -1
        self.previous_cluster = -1
        self.distance = []

class Kmeans:
    def __init__(self, k = 2, i = 10, file_name = ""):
        # Declaring all arrays
        self.obj_array = []      # array with objects
        self.x_array = []        # array containing x values
        self.y_array = []        # array containing y values
        self.count_array = []    # array containing quantity values
        self.centroid_array = [] # centroids array
        self.data_counter = 0    # current read data counter
        self.dataset_changed = 0 # flag to keep track of centroid changes
        self.iterations = i
        self.K = k
        # Abrindo o arquivo passado pela linha de comando
        try:
            self.data_file = open(file_name, 'r')
        except IOError:
            print('--==\t Unable to open the file (' + file_name + ').\t ==--')
            exit()
    
    def cluster_it(self):
        
        # Ignorando primeira linha do arquivo
        self.data_file.readline()

        # Lendo os dados do arquivo
        for line in self.data_file:
            name = line.split()[0]
            x = float(line.split()[1])
            y = float(line.split()[2])
            self.data_counter += 1

            # Inserindo no vetor de dados
            self.obj_array.insert(len(self.obj_array), Objeto(name, x, y))

        # Inicializando variaveis para calculo de centroide
        for i in range(0, self.K):
            j = random.randint(0, self.data_counter)   # Rand para escolher os centroides aleatoriamente
            self.x_array.insert(len(self.x_array), 0)
            self.y_array.insert(len(self.y_array), 0)
            self.count_array.insert(len(self.count_array), 0)
            self.centroid_array.insert(len(self.centroid_array), [self.obj_array[j].x, self.obj_array[j].y])

        iteration = 0
        has_changed = 1

        while iteration < self.iterations:
        #while has_changed == 1:
            
            if iteration == 0:
                # Calculating Euclidian distance between each object and each centroid
                for i in range(len(self.obj_array)):
                    for j in range(len(self.centroid_array)):
                        self.obj_array[i].distance.insert(len(self.obj_array[i].distance), math.sqrt(math.pow(self.obj_array[i].x - self.centroid_array[j][0], 2) + math.pow(self.obj_array[i].y - self.centroid_array[j][1], 2)))
            else:
                for i in range(len(self.obj_array)):
                    for j in range(len(self.centroid_array)):
                        self.obj_array[i].distance[j] = math.sqrt(math.pow(self.obj_array[i].x - self.centroid_array[j][0], 2) + math.pow(self.obj_array[i].y - self.centroid_array[j][1], 2))

            current_cluster, previous_cluster = 0, 0

            # Clustering each object to nearest centroid
            for i in range(len(self.obj_array)):
                shortest_dist = 999

                for j in range(len(self.centroid_array)):
                    if ((self.obj_array[i].distance[j] < shortest_dist) & (self.obj_array[i].distance[j] > 0)):
                        shortest_dist, previous_cluster, current_cluster = self.obj_array[i].distance[j], self.obj_array[i].current_cluster, j

                self.obj_array[i].current_cluster, self.obj_array[i].previous_cluster = current_cluster, previous_cluster
                if self.obj_array[i].current_cluster == self.obj_array[i].previous_cluster:
                    has_changed = 0

            # Soma para o calculo de centroide
            for i in range(len(self.obj_array)):
                self.x_array[self.obj_array[i].current_cluster] += self.obj_array[i].x
                self.y_array[self.obj_array[i].current_cluster] += self.obj_array[i].y
                self.count_array[self.obj_array[i].current_cluster] += 1

            # Calculating centroid position
            for i in range(len(self.count_array)):
                if self.count_array[i] != 0:
                    self.centroid_array[i][0], self.centroid_array[i][1] = (self.x_array[i] / self.count_array[i]), (self.y_array[i] / self.count_array[i])
                else:
                    self.centroid_array[i][0], self.centroid_array[i][1] = -1, -1

            iteration += 1

            # Reseting variables
            for i in range(len(self.x_array)):
                self.x_array[i] = 0
                self.y_array[i] = 0
                self.count_array[i] = 0

def Main():

    input_file = sys.argv[1]
    input_name = path_leaf(input_file).split('.')[0]
    num_K = sys.argv[2]
    iterations = sys.argv[3]
    
    kms = Kmeans(int(num_K),int(iterations),input_file)
    kms.cluster_it()

    # Setting output file
    output_path = "./output/k-means/"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(output_path+" Sucessfully created!")

    output_file = output_path+input_name+"K"+sys.argv[2]+"I"+str(iterations)+".clu"

    arquivo_saida = open(output_file, 'w')

    # Writing data in file
    for i in range(len(kms.obj_array)):
        arquivo_saida.write(kms.obj_array[i].name + '\t' + str(kms.obj_array[i].current_cluster) + '\n')
    
    arquivo_saida.close()
    #print("python ./plot.py "+sys.argv[1]+" "+output_file + " -p")
    os.system("python ./plot.py "+sys.argv[1]+" "+output_file)

if __name__ == "__main__":
    
    if len(sys.argv) != 4:
        print('== How to: python k-means.py <input.txt> <K_centroids> <iterations> ==')
        exit()
    Main()