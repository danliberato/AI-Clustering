import os
from sys import argv
from threading import Thread


#this file is inteded to run avg-link, single-link and k-means algorithms over folowing datasets
#c2ds1-2sp.txt --- k (2 to 5)
c2ds1_2spNum_Clusters = [i+2 for i in range(4)]
#c2ds3-2g.txt --- k (2 to 5)
c2ds3_2gNum_Clusters = [i+2 for i in range(4)]
#monkey.txt --- k (5 to 12)
monkeyNum_Clusters = [i+5 for i in range(8)]


### 1st dataset THREAD ###
def c2ds1_2spThread(i):
    #for k in c2ds1_2spNum_Clusters:
    #for k in c2ds1_2spNum_Clusters:
        #k-means execution
     #   kmeans_cmd = 'python k-means.py ./datasets/c2ds1-2sp.txt '+ str(k) + ' '+ str(i)
        #print(kmeans_cmd)
        #os.system(kmeans_cmd)
        
    #single-link execution
    single_cmd = 'python single-link.py datasets/c2ds1-2sp.txt '+ str(min(c2ds1_2spNum_Clusters)) + " " +str(max(c2ds1_2spNum_Clusters))
    #print(single_cmd)
    #os.system(single_cmd)

    #average-link execution
    average_cmd = 'python average-link.py datasets/c2ds1-2sp.txt '+ str(k)
    print(average_cmd)
    os.system(average_cmd)

### 2nd dataset THREAD ###
def c2ds3_2gThread(i):
    #for k in c2ds3_2gNum_Clusters:
        #k-means exection
    #    kmeans_cmd = 'python k-means.py datasets/c2ds3-2g.txt '+ str(k) + ' '+ str(i)
    #    print(kmeans_cmd)
    #    os.system(kmeans_cmd)

    #single-link execution
    single_cmd = 'python single-link.py datasets/c2ds3-2g.txt '+ str(min(c2ds3_2gNum_Clusters)) + " " +str(max(c2ds3_2gNum_Clusters))
    #print(single_cmd)
    #os.system(single_cmd)

    #average-link execution
    average_cmd = 'python average-link.py datasets/c2ds3-2g.txt '+ str(k)
    print(average_cmd)
    os.system(average_cmd)

### 3rd dataset THREAD ###
def monkeyThread(i):
    #for k in monkeyNum_Clusters:
        #k-means exectuion
     #   kmeans_cmd = 'python k-means.py .\datasets\monkey.txt '+ str(k) + ' '+ str(i)
      #  print(kmeans_cmd)
       # os.system(kmeans_cmd)

    #single-link execution
    #single_cmd = 'python single-link.py datasets/monkey.txt '+ str(min(monkeyNum_Clusters)) + " " +str(max(monkeyNum_Clusters))
    single_cmd = 'python old_single-link.py datasets/monkey.txt '+ str(min(monkeyNum_Clusters)) + " " +str(max(monkeyNum_Clusters))
    #print(single_cmd)
    #os.system(single_cmd)

    #average-link execution
    average_cmd = 'python average-link.py datasets/monkey.txt '+ str(k)
    print(average_cmd)
    os.system(average_cmd)

def Main(iteration = 1):

    try:
            
        Thread(target=c2ds1_2spThread, args=[iteration]).start()
        #Thread(target=c2ds3_2gThread, args=[iteration]).start()
        #Thread(target=monkeyThread, args=[iteration]).start()

    except:
        print("--== ERROR: in iteration "+str(iteration))
        Main()

if __name__ == "__main__":
    Main(argv[1])
