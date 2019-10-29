import os
import sys
import ntpath
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors

#HOW TO USE: python plot.py <dataset_file> <clustered_file> [optional] -p <plot only>
#if "-p" it's not passed, script will create a path and store the image

def path_leaf(path):
    head, tail = ntpath.split(path)
    return head, tail or ntpath.basename(head)

x = [] # X-axis
y = [] # Y-axis
z = [] # Z-axis (colors)
np.random.seed(19680801)
colors = np.random.rand(80) # set random colors to show

source_input = sys.argv[1]
cluster_input = sys.argv[2]
result_path, title = path_leaf(cluster_input) # Get dataset clustered filename
title = title.split(".")[0]

source_file = open(source_input, 'r')
cluster_file = open(cluster_input, 'r')

source_file.readline() # jumps one line in dataset file

# reads and add to x,y arrays
for line in source_file:
  content = line.split("\t")
  x.append(float(content[1]))
  y.append(float(content[2]))

for line in cluster_file:
  content = line.split()
  z.append(colors[int(content[1].strip('\t'))])

source_file.close()
cluster_file.close()

#print(z)
plt.title(title)
plt.scatter(x, y, c=z, alpha=0.5)

if len(sys.argv) == 4 and sys.argv[3] == "-p":
  plt.show()

else:
  result_path += "\\imgs\\"
  if not os.path.exists(result_path):
    os.makedirs(result_path)
    print(result_path+" Sucessfully created!")
  plt.savefig(result_path+title+".png")