import subprocess
import threading
import time

global_lock = threading.Lock()
def invokingc():
	while global_lock.locked():
	        continue
    	global_lock.acquire()
	subprocess.call(["javac", "sample1.java"])
	#stmp=subprocess.call("./a.out")
	global_lock.release()
def create_threads():
	threads = []
	for i in range(1, limit):
    		t = threading.Thread(target=invokingc)
    		threads.append(t)
    		t.start()
	[thread.join() for thread in threads]
start_time=time.time()
limit=11
create_threads()
finish_time=time.time() - start_time
with open("exe_time_javac.txt", "a+") as file:
		limit=limit-1
		file.write(str(limit))
		file.write(",")
		file.write(str(finish_time))
		file.write("\n")
		file.close()
#print 'execution time in seconds: ', finish_time

