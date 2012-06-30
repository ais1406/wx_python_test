import socket

HOST='localhost'
PORT = 8000

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn,addr = s.accept()

print 'connect by', addr

while 1:
    data = conn.recv(1024)
    if not data: break
    print data
    conn.send(data)

conn.close()

