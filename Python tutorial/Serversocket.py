import socket

ser = socket.socket()

ser.bind(('localhost', 9988))

print("socket created")

ser.listen(3) # no of client to accept

print('Waiting for connection')

while True:
    cli, address = ser.accept()
    name = cli.recv(1024).decode()
    print("connect with ", address, name)
    cli.send(bytes('Hello client', 'utf-8'))



