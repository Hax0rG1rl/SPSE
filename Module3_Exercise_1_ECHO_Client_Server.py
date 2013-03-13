#! /usr/bin/env python

# Simple UDP ECHO Client-Server Python2.7.3 script - by JohnnyAMD - 03/12/2013

import socket

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Clearing up the other mess by releasing the channel free

tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

#Setting up the server
tcpsocket.bind(('0.0.0.0', 2345))

#How many concurrent connections this can handle
tcpsocket.listen(1)
print 'waiting for a client.... '
(client, (ip,port)) = tcpsocket.accept()
print 'Receiging info from:.. ', ip
print 'starting ECHO output '

#Print the received data from the client
while 1:
  data = client.recv(128)
	print 'Client sent: ', data
	client.send(data)

# Byffer has been reach out, clossing the channel
print 'closing comm channel...'
client.close()
