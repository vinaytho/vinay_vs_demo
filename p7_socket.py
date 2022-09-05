import socket

s = socket.socket()
print('Socket Created')

s.bind(('localhost', 9998))
s.listen(3)
print('Waiting for connections')

while True:
    c, addr = s.accept()
    print("Connected with", addr)

    c.send(bytes('Welcome to the party. You are now connected','utf-8'))

    c.close()