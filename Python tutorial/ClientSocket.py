import socket

cli = socket.socket()

cli.connect(('localhost', 9988))
name = input("Enter your Name")
cli.send(bytes(name, 'utf-8'))

print(cli.recv(1024).decode())

