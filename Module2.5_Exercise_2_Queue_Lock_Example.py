# !/usr/bin/env python

# Simple Queue Lock mechanism example script - Python2.7.3 - by JohnnyAMD - 03/07/2013

import threading
import Queue
import time
import ftplib

# opening the ftp file for reading the contents
print "\nOpening for reading the ftp list.\n" 
lines = []
text_file = open("anonymous_ftp_sites.txt", "r")
lines = text_file.readlines()
print lines

# Displaying some info about what's inside
print 'The file contains: %d'%len(lines) + ' ftp sites'
text_file.close()

# using the threading class
class WorkerThread(threading.Thread):

  def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue

# defining the constructor
	def run(self):
		print "In WorkerThread"
		while True:                        
			try:
                                counter = self.queue.get()
                                for line in lines:     
# doing some checking for nasty things as \n and like
                                    if line == '\n':
                                        break
                                    else:

# here I'm formatting the read lines in such way that they contain only the host name and nothing else. 
# Some restrictions are applied thought as ftp:// prefix is considered as not being present among listed targets

                                        line = line.rstrip('\n')
                                        print 'The target name has been checked: ' + line  + '\n'
                                        ftp = ftplib.FTP(line)
                                        lock.acquire()
                                        ftp.login()
                                        ftp.retrlines('LIST')
                                        time.sleep(4)
                                        lock.release()
                                        ftp.quit()				
				print "Ordered to sleep for %d seconds!"%counter
				time.sleep(counter)
				print "Finished sleeping for %d seconds"%counter
				self.queue.task_done()
				
# trying to catch as many possible exceptions could appear and handle them accordingly

			except NameError, detail:
				print 'Something is wrong', detail
				time.sleep(3)
				break 
			except  TypeError, detail:
				print 'Something is wrong', detail
				time.sleep(3)
				break
			except  EOFError, detail:
                                print 'EOFerr Occured. End of ftp sites file? Please have a check.', detail
                                time.sleep(3)
                                break
                        except  AttributeError, detail:
                                print 'Something is wron with locking mechanism: ', detail
                                time.sleep(3)
                                break
				

queue = Queue.Queue()
lock = threading.Lock()

# populating queue

for j in lines:
	queue.put(j)
	
# creating threads

for i in range(5):
	print "Creating a WorkerThread : %d"%i	
	worker =  WorkerThread(queue)
	worker.setDaemon(True)
	worker.start()
	print "WorkerThread %d Created!"%i

print '\r\n'
queue.join()

print "All tasks over!"
