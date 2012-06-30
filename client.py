import socket

HOST = 'localhost'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send("hello world")
data = s.recv(1024)
s.close()
print "recevied", repr(data)