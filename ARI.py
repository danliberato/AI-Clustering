import sys
from sklearn import metrics

#load files in memory
source_file = open(sys.argv[1], 'r')
target_file = open(sys.argv[2], 'r')

#initialize arrays
source_array = []
target_array = []
source_obj = []
target_obj = []

while True:
    l_source = source_file.readline()
    l_target = target_file.readline()
    if not len(l_source) or not len(l_target): #stops when reach the end of file
        break

    source_obj = l_source.split('\t') # splits line in "\t" occurrence
    source_array.append(source_obj[1][0]) # adds obj in array
    target_obj = l_target.split('\t')
    target_array.append(target_obj[1][0])

print(metrics.adjusted_rand_score(source_array, target_array))