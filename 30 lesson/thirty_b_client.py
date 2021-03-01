'''
Task 2
Extend the echo server, which returns to client the data, encrypted using the Caesar cipher algorithm by a specific key obtained from the client
'''


import socket
import thirty_b_caesar_cipher

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(cipher_encrypt(plain_text, key))
    data = s.recv(1024)

print('Received', repr(data))


if __name__ == '__main__':
    plain_text = "Mate, the adventure ride in Canberra was so much fun, We were so drunk we ended up calling 911!"
    key = 4
