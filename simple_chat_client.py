'''
Task 1 Building a simple chat application
    A basic client to server chat in the console. We will need to create two files, one server, and one client.
    The clients will send messages to the server and the server will then broadcast them to all the connected clients.
    Users (clients) will be able to rename themselves in the server, so that other clients don’t see client1, client2 etc, but the user’s name instead.

'''

# [https://hackernoon.com/a-simple-guide-to-building-chat-applications-in-python-q5633t1c]
# [https://www.thepythoncode.com/article/make-a-chat-room-application-in-python]
# [https://www.geeksforgeeks.org/simple-chat-room-using-python/]


import socket
import select
import sys


class Client:
    def __init__(self, name):
        self.name = input('Enter your name: ')
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_and_ip = ('127.0.0.1', 12345)
        self.server.connect(port_and_ip)

    def run_client(self):
        while True:
            self.sockets_list = [sys.stdin, server]
            self.read_sockets, self.write_socket, self.error_socket = select.select(
                self.sockets_list, [], [])
        for socks in self.read_sockets:
            if socks == self.server:
                message = socks.recv(2048)
                print(message)
            else:
                message = sys.stdin.readline()
                self.server.send(message)
                sys.stdout.write(self.name)
                sys.stdout.write(message)
                sys.stdout.flush()
        self.server.close()


if __name__ == "__main__":
    c1 = Client('1')
    c2 = Client('2')
