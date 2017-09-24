from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import csv
import string
import math

x=[]
y=[]
z=[]

#read data from file and turn from string to numbers
with open ("C:\Users\ipaul\Documents\PoE\Lab2_Data_H") as f:
	lines = f.read().splitlines()
	x = lines[0].translate(None, string.punctuation).split()
	y = lines[1].translate(None, string.punctuation).split()
	z = lines[2].translate(None, string.punctuation).split()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for el in range(len(x)):
	x[el] = int(x[el])/10

for el in range(len(y)):
	y[el] = int(y[el])/10

for el in range(len(z)):
	z[el] = int(z[el])/10


# clean backgorund
avg = sum(z)/len(z)

newz=[]
newy=[]
newx=[]

for i in range(len(z)):
	if z[i] > avg :
		newx.append(x[i])
		newy.append(y[i])
		newz.append(z[i])
x = newx
y = newy
z = newz




newz=[]
newy=[]
newx=[]

for i in range(len(z)):
	if z[i] > avg :
		zv = math.log(z[i]/680.0)/.95
		zv = zv * math.sin(math.radians(x[i])) * math.sin(math.radians(y[i])) * -100
		newz.append(zv)
z = newz
newz=[]


# minz = int(min(z))
# maxz = int(max(z))
# count = 0
# bestCount = 0
# bestDist = 0
# distRange = 10

# for i in range(minz, maxz):
# 	for dist in z:
# 		if i<dist and dist<(i+distRange):
# 			count += 1
# 	if count > bestCount:
# 		bestDist = i
# 		bestCount = count
# 	count = 0

# for i in range(len(z)):
# 	if (z[i]>bestDist) and (z[i]<(bestDist+distRange)) :
# 		newx.append(x[i])
# 		newy.append(y[i])
# 		newz.append(z[i])
# x = newx
# y = newy
# z = newz
# newz=[]
# newy=[]
# newx=[]

ax.scatter(x, y, z)
# ax.plot_trisurf(x,y,z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
