import threading
import time
threads = []
def write_to_file():
	for i in threads:
		print i.getName()
		#print ("hai")
	

for i in range (0,10):
	t = threading.Thread(target=write_to_file)
	threads.append(t)
	t.start()
[thread.join() for thread in threads]

