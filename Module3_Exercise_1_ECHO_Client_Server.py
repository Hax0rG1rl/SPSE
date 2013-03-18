#! /usr/bin/env python

# Simple TCP/[UDP] ECHO Client-Server script - Python2.7.3 - by JohnnyAMD - 03/12/2013

import socket
import random

# Socket opened for TCP protocol
tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Socket opened for UDP protocol
# tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Clearing up the other mess by releasing the channel free

tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

#Setting up the server to listen on all available interfaces 
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
try:
	while 1:
		data = client.recv(128)
		print 'Client sent: ', data
		client.send(data)
			if data == x:
				print "You've got it. Some magic inside maybe."
				client.close()
				del client
				break
			else: 
				print "He didn't pointed the correct value though"

except KeyboardInterrupt:
	print 'Intrerupted.'
	client.close()
	break

# Byffer has been reach out, clossing the channel
print "Closing comm channel."
client.close()
