import time
import socket
import struct
import sys

message = 'very important data'
multicast_group = ('224.3.29.71', 10000)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(100)

# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

for i in range(10000):

	    # Send data to the multicast group
#	    print >>sys.stderr, 'sending "%s"' % message
	sent = sock.sendto(str(i), multicast_group)

	    # Look for responses from all recipients
	time.sleep(.001)
	print i
