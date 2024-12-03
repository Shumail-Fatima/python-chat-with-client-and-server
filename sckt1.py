import socket
host = "192.168.18.155"
port = 5001
server = socket.socket()
server.bind((host,port))
server.listen()
conn, addr = server.accept()
print ("Connection from: " + str(addr))
while True:
   data = conn.recv(1024).decode()
   if not data:
      break
   data = str(data).upper()
   print (" from client: " + str(data))
   data = input("type message: ")
   conn.send(data.encode())
conn.close()

hoste = '192.168.18.155'
port = 5001
obj = socket.socket()
obj.connect((hoste,port))
message = input("type message: ")
while message != 'q':
   obj.send(message.encode())
   data = obj.recv(1024).decode()
   print ('Received from server: ' + data)
   message = input("type message: ")
obj.close()