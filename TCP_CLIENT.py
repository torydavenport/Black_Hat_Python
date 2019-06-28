
"""
This script is from the book "Black Hat Python" by Justin Seitz.
This version may have been modified from its origional version for personal use by Tory Davenport.
The original script can be found on page 10 of the book.  
UPDATE 6-28-2019 -- > This script is now update for python3 
"""

import socket

target_host = "172.16.30.64"
target_port = 60555

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

# send some data
client.send("AAAABBBBCCCC".encode()) # .enconde() to convert byte to string to fix type error

# recieve some data
response = client.recv(4096)

print(response)