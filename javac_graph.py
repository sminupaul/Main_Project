import matplotlib.pyplot as plt
import csv

plt.xlabel('No.of threads ')
plt.ylabel('Execution Time in seconds')
plt.title('Comparision of execution time using system files')
x1 = []
y1 = []
with open('etime_javac.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
	#print(row[0])
        x1.append(int(row[0]))
        y1.append(float(row[1]))

plt.plot(x1,y1, label='javac with lockf')
x2=[]
y2=[]
with open('etime_java_fcntl.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
	#print(row[0])
        x2.append(int(row[0]))
        y2.append(float(row[1]))

plt.plot(x2,y2, label='javac with fcntl')
x3=[]
y3=[]
with open('etime_javac_pro.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
	#print(row[0])
        x3.append(int(row[0]))
        y3.append(float(row[1]))
plt.plot(x3,y3, label='javac with proposed system')

plt.legend()
plt.show()
