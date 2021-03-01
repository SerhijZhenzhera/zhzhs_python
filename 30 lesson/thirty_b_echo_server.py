'''
Task 2
Extend the echo server, which returns to client the data, encrypted using the Caesar cipher algorithm by a specific key obtained from the client
'''


# Echo server program
import socket
import thirty_b_caesar_cipher

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()


if __name__ == '__main__':
    print(cipher_decrypt(data[0], data[1]))
