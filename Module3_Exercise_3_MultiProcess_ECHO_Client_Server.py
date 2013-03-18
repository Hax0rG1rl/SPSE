#! /usr/bin/env python

# Simple TCP Multiprocess ECHO Client-Server - Python 2.7.3 script - by JohnnyAMD - 03/18/2013

import socket
import random
import os

# Socket opened for TCP protocol
tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Clearing up the other mess by releasing the channel free

tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

# Socket opened for UDP protocol
# tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Setting up the server to listen on all available interfaces
tcpsocket.bind(('0.0.0.0', 2345))

# Setting up a random number and display the value
x = random.randrange(100)
print 'Value to be guessed is: %d \n'%x 

# defining how many fork processes will be created

for i in range(2):
  	child_processes = os.fork()

# Checking to see where we are child or just parent process	 
		if child_processes == 0:
			
#How many concurrent connections this can handle
			tcpsocket.listen(1)
			print("Child process details: %d"%os.getpid())

# Waiting for a client to connect
			print 'waiting for a client.... '
			(client, (ip,port)) = tcpsocket.accept()
			print 'Receiging info from:.. ', ip
			print 'starting ECHO output '

#Print the received data from the client and check to see if he guessed the value
			while 1:
				data = client.recv(128)
				print("Process PID cliet %d sent: %s"%(os.getpid(),data))
				client.send(data)
				if data == x:
					print "You've got it. Some magic inside maybe."
					tcpsocket.close()
				else: 
					print "He didn't pointed the correct value though"

		else:
			#we are inside the parent process
			print("We are in the parent process...")

			print("Child process has the PID: %d"%child_processes)


# Buffer has been reach out, clossing the channel
print "Closing comm channel..."
tcpsocket.close()
