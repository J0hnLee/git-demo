#hello everyone

import scipy
import numpy as np
import random
import csv
import matplotlib.pyplot as plt
plt.interactive(False)

height = np.array([random.gauss(0,1)*20+160 for i in range(100)])
weight = np.array([random.gauss(0,1)*20+60 for i in range(100)])
bmi=weight/(height*0.01)**2

is_fat=[]
for element in bmi:
    if element > 28:
        is_fat.append(True)
    else:
        is_fat.append(False)
#print(is_fat)

print(is_fat.count(False))

with open('data.csv','w',newline='') as csvfile:
    w=csv.writer(csvfile,delimiter=',')
    for row in range(100):
        a=[height[row], weight[row], is_fat[row]]
        w.writerow(a)


plt.scatter(height,weight)
plt.show()