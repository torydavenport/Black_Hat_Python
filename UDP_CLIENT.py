"""
This script is from the book "Black Hat Python" by Justin Seitz.
This version may have been modified from its origional version for personal use by Tory Davenport.
The original script can be found on page 11 of the book.  
UPDATE --> This script has been updated for Python3
"""

import socket

target_host = "192.168.6.9"
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto("AAABBBCCC".encode(),(target_host, target_port))

# receive some data
data, addr = client.recvfrom(4096)

print(data)
