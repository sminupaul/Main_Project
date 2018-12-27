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
plt.title('Comparsion of exeution time of various locking algorithms')
x1 = []
y1 = []
with open('input1.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
	#print(row[0])
        x1.append(int(row[0]))
        y1.append(float(row[1]))

plt.plot(x1,y1, label='with file lock flock')
plt.legend()
plt.show()
