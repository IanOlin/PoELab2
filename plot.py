import matplotlib.pyplot as plt
import csv
import numpy as np

d={}
x=[]
y=[]

with open ('C:\Users\ipaul\Documents\PoE\lab2data03.csv', 'r') as csvfile:
	plots = csv.reader(csvfile)
	for row in plots:
		if int(row[0]) in d:
			d[int(row[0])].append(int(row[1]))
		else:
			d[int(row[0])] = [int(row[1])]

for key, value in d.iteritems():
	x.append(key)
	y.append(sum(value)/float(len(value)))

npx = np.asarray(x)
npy = np.asarray(y)
fit = np.polyfit(x, np.log(y), 1,  w=np.sqrt(y))
print("y = " + str(np.exp(fit[1])) + "e^(" + str(np.exp(fit[0])) +"x)")
t1 = np.linspace(5,24)
t2 = np.linspace(5,24)

#error
errd={}
errx=[]
erry=[]
with open ('C:\Users\ipaul\Documents\PoE\lab2data04.csv', 'r') as csvfile:
	plots = csv.reader(csvfile)
	for row in plots:
		if float(row[0]) in errd:
			errd[float(row[0])].append(float(row[1]))
		else:
			errd[float(row[0])] = [float(row[1])]

for key, value in errd.iteritems():
	errx.append(key)
	erry.append(sum(value)/float(len(value)))


plt.plot(t1, np.exp(fit[1]) * np.exp(fit[0]*t1))
plt.plot(x,y, 'x', label='Calibration Samples')
plt.plot(errx,erry,'x',label='Errors')
plt.xlabel('Distance (IN)')
plt.ylabel('Serial Out')
plt.title('Calibration Curve')
plt.legend()
plt.show()