import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('input.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
	#print(row[0])
        x.append(int(row[0]))
        y.append(float(row[1]))

plt.plot(x,y, label='without file lock')
plt.xlabel('No.of threads ')
plt.ylabel('Execution Time in seconds')
plt.title('Comparsion b/w exeution time of various locking algorithms')
x1 = []
y1 = []
with open('input1.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
	#print(row[0])
        x1.append(int(row[0]))
        y1.append(float(row[1]))

plt.plot(x1,y1, label='with file lock flock')
x2=[]
y2=[]
with open('exe_lockf.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
	#print(row[0])
        x2.append(int(row[0]))
        y2.append(float(row[1]))

plt.plot(x2,y2, label='with file lock lockf')
plt.legend()
plt.show()
