import threading
import time
import fcntl

start_time=time.time()
global_lock = threading.Lock()
limit=301
def read_files():
	while global_lock.locked():
        	continue
	global_lock.acquire()

	with open("testfile2.txt", "a+") as file:
		fcntl.flock(file,fcntl.LOCK_EX | fcntl.LOCK_NB)
		file.write(str(threading.get_ident()))
		file.write("\n")
		fcntl.flock(file, fcntl.LOCK_UN)
		file.close()
	global_lock.release()
		

def createthreads():
	threads = []
	for i in range(1, limit):
    		t = threading.Thread(target=read_files)
    		threads.append(t)
    		t.start()
	[thread.join() for thread in threads]

	with open("exe_time_fcntl.txt", "a+") as file:
		file.write(str(limit))
		file.write("\t")
		file.write(str(time.time() - start_time))
		file.write("\n")
		file.close()

#while(limit<305):
#	limit+=10
createthreads()
