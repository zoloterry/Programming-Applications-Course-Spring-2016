import os
import numpy as np
import matplotlib.pyplot as plt

filePath = 'output.txt'

#for accuracy array
accArray = []
with open(filePath, "r") as f:
    searchlines = f.readlines()
for i, line in enumerate(searchlines):
    if "solver.cpp:414]     Test net output #0: accuracy =" in line: 
        for l in searchlines[i:i+1]: 
		trash, accuracy = l.rsplit(' ', 1)
		cleanAcc = accuracy.strip('\n')
		numAcc = float(cleanAcc)
		accArray.append(numAcc)
	print accuracy
print accArray
f.close()

#for iteration array
iterationArray = []
with open(filePath, "r") as f:
    searchlines = f.readlines()
for i, line in enumerate(searchlines):
    if "solver.cpp:346] Iteration" in line: 
        for l in searchlines[i:i+1]: 
		firstSplit = l.split('Iteration ')[1]
		secondSplit = firstSplit.split(',')[0]
		iteration = int(secondSplit)		
		iterationArray.append(iteration)
	print iteration	
print iterationArray
f.close()


#for graphing plot

plt.plot(iterationArray, accArray)
plt.xlabel('Iteration Step')
plt.ylabel('Accuracy')
plt.title('Accuracy vs. Iteration')

plt.savefig('/home/bison/Documents/caffe_dev/caffe/plots/AccPlot256by256.png')
plt.show()

