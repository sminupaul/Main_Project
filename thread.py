import threading
import time

start_time=time.time()
global_lock = threading.Lock()
upper_limit=311
def write_to_file():
    while global_lock.locked():
        continue

    global_lock.acquire()

    with open("testfile2.txt", "a+") as file:
        file.write(str(threading.get_ident()))
        file.write("\n")
        file.close()

    global_lock.release()

# Create a 200 threads, invoke write_to_file() through each of them,
# and 
def createthreads():
	threads = []
	for i in range(1, upper_limit):
    		t = threading.Thread(target=write_to_file)
    		threads.append(t)
    		t.start()
	[thread.join() for thread in threads]

	with open("exe_time.txt", "a+") as file:
		file.write(str(upper_limit))
		file.write("\t")
		file.write(str(time.time() - start_time))
		file.write("\n")
		file.close()

while(upper_limit<405):
	upper_limit+=10
	createthreads()

