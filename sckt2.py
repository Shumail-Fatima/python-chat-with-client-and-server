import socket
host = '192.168.18.155'
port = 5001
obj = socket.socket()
obj.connect((host,port))
message = input("type message: ")
while message != 'q':
   obj.send(message.encode())
   data = obj.recv(1024).decode()
   print ('Received from server: ' + data)
   message = input("type message: ")
obj.close()