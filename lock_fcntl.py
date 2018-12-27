import fcntl
from time import sleep
x=open('/home/sminupaul/Desktop/main/testfile1.txt','w+')
fcntl.flock(x,fcntl.LOCK_EX | fcntl.LOCK_NB)
print "sleeping...."
sleep(100)
print "sleep time complete"
fcntl.flock(x, fcntl.LOCK_UN)
