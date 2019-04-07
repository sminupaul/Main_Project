import subprocess
import threading
import time
import fcntl

global_lock = threading.Lock()
def invokingc():
	while global_lock.locked():
	        continue
    	global_lock.acquire()
	with open("sample.c", "r") as file:
		fcntl.flock(file,fcntl.LOCK_EX | fcntl.LOCK_NB)
		subprocess.call(["gcc", "sample.c"])
		fcntl.flock(file, fcntl.LOCK_UN)
		file.close()
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
limit=16
create_threads()
finish_time=time.time() - start_time
with open("exe_time_gcc_fcntl.txt", "a+") as file:
		limit=limit-1
		file.write(str(limit))
		file.write(",")
		file.write(str(finish_time))
		file.write("\n")
		file.close()
#print 'execution time in seconds: ', finish_time

