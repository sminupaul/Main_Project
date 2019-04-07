import threading
import time
import fcntl

limit=10
global_lock = threading.Lock()
file_contents = []
def write_to_file():
	while global_lock.locked():
		continue
	global_lock.acquire()
	with open("testfile1.txt", "a+") as file:
		fcntl.flock(file,fcntl.LOCK_EX | fcntl.LOCK_NB)
		file_contents.append(threading.get_ident())
		fcntl.flock(file, fcntl.LOCK_UN)
	global_lock.release()
threads = []
start_time=time.time()
for i in range(1, limit):
    	t = threading.Thread(target=write_to_file)
    	threads.append(t)
    	t.start()
[thread.join() for thread in threads]
finish_time=time.time() - start_time
with open("exe_time_1.txt", "a+") as file:
	#print("dhbfghs")
	file.write(str(limit))
	file.write("\t")
	file.write(str(finish_time))
	print(finish_time)
	file.write("\n")
	file.close()
with open("testfile1.txt", "a+") as file:
	file.write(str(file_contents))
	file.close()

