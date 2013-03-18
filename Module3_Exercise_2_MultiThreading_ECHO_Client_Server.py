#! /usr/bin/env python

# Simple Multi-threading TCP ECHO Client-Server script - Python2.7.3 - by JohnnyAMD - 03/13/2013
# https://github.com/JohnnyAMD/SPSE/blob/master/Module3_Exercise_2_MultiThreading_ECHO_Client_Server

import socket
import random
import threading


# defining workerthread class 
class WorkerThread(threading.Thread) :
	def __init__(self, bucket, server_info) :
		threading.Thread.__init__(self)
		self.bucket = bucket
		self.ip = server_info[0]
		self.port = server_info[1]

# defining the constructor class
	def run(self) :
		print 'Incoming connection from %s port %d' % (self.ip, self.port)

# setting up the initial data value

		data=''

# what the client sees and sends from his prompt
		self.bucket.send("You are connected to the server; type 'exit' to exit \n ")		
		while data.find('exit') == -1 or data != x:
			data = self.bucket.recv(128)
			self.bucket.send(data)	
		
# client types 'exit' or guessed the correct value
		else :
			print 'Got it. Comm channel has been closed'
			self.bucket.close()
			del bucket
			break

# Socket opened for TCP protocol
tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Socket opened for UDP protocol
# tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Clearing up the other mess by releasing the channel free

tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

#Setting up the server to listen on all available interfaces

tcpsocket.bind(('0.0.0.0', 2345))

#How many concurrent connections this can handle
tcpsocket.listen(3)

# Setting up a random number and display the value
x = random.randrange(100)
print 'Value to be guessed is: %d'%x 
print '\n'
print "Let's fishing... "

# Defining the threads
while True :
	(client, (server_info)) = tcpsocket.accept()
	new_thread = WorkerThread(client, server_info)
	new_thread.start()
