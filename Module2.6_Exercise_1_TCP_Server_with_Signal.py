#! /usr/bin/env python

# Simple 100 seconds alive TCP Server - Python2.7.3 script - by JohnnyAMD - 03/16/2013

import socket
import random
import os
import signal
import time

print 'Pid for this server is %s' %os.getpid()

# defining the signal handler function 

def handler(sig, frame):

# Killing the process after the time is expired

   os.kill(os.getpid(), signal.SIGALRM) 

signal.signal(signal.SIGALRM, handler)

signal.alarm(10)

# exception handeling 

try:

  # Socket opened for TCP protocol
	tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Socket opened for UDP protocol
	# tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# Clearing up the other mess by releasing the channel free

	tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

	#Setting up the server to listen on all available interfaces
	print 'Server is alive for 100 seconds'
	tcpsocket.bind(('0.0.0.0', 2345))

	#How many concurrent connections this can handle
	tcpsocket.listen(1)

	# Setting up a random number and display the value
	x = random.randrange(100)
	print 'Value to be guessed is: %d'%x 

	# Waiting for a client to connect
	print 'waiting for a client.... '
	(client, (ip,port)) = tcpsocket.accept()
	print 'Receiging info from:.. ', ip
	print 'starting ECHO output '

	#Print the received data from the client and check to see if he guessed the value
	while 1:
		data = client.recv(128)
		print 'Client sent: ', data
		client.send(data)
		if int(data) == x:
			print "You've got it. Some magic inside maybe."
			break
		else: 
			print "He didn't pointed the correct value though"


	# Byffer has been reach out, clossing the channel
	print "Closing comm channel."
	client.close()

except socket.error:
    print "\nI'm done here waiting...."
	
