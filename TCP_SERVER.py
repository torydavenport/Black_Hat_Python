"""
This script is from the book "Black Hat Python" by Justin Seitz.
This version may have been modified from its origional version for personal use by Tory Davenport.
The original script can be found on page 12 of the book.  
UPDATE 6-28-2019 -- > This script is now update for python3 
"""

import socket
import threading

bind_ip = "172.16.30.64"
bind_port = 60555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

# this is our client-handling thread
def handle_client(client_socket):

	# print out what the client sends
	request = client_socket.recv(1024)

	print "[*] Received: %s" % request

	# send back a packet
	client_socket.send("ACK")

	client_socket.close()

while True:

	client, addr = server.accept()

	print "[*] Accepted connection from %s:%d" % (addr[0],addr[1])

	# spin up our client thread to handle incoming data
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()