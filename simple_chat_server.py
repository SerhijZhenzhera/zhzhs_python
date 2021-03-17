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
# import select
# import sys
import threading


class Server:
    def __init__(self, name, cl_list=None, cl_max=25):
        self.name = name
        if cl_list is not None:
            self.list_of_clients = cl_list
        else:
            self.list_of_clients = []
        self.list_max = cl_max
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port_and_ip = ('127.0.0.1', 12345)
        self.server.bind(port_and_ip)
        self.server.listen(self.list_max)

    def send_hi(self, conn, addr):
        conn.send('Hi! Welcome to this chatroom!')
        while True:
            try:
                message = conn.recv(2048)
                if message:
                    print('<' + addr[0] + '> ' + message)
                    message_to_send = '<' + addr[0] + '> ' + message
                    broadcast(message_to_send, conn)
                else:
                    remove(conn)
            except:
                continue

    def broadcast(self, message, connection):
        for clients in self.list_of_clients:
            if clients != connection:
                try:
                    clients.send(message)
                except:
                    clients.close()
                    remove(clients)

    def modify_list(self, number):
        if type(number) == int and number > 0:
            self.list_max = number // 1
        else:
            print('Use only integers!')

    def remove(self, connection):
        if connection in self.list_of_clients:
            self.list_of_clients.remove(connection)

    def run_server(self):
        while True:
            conn, addr = self.server.accept()
            self.list_of_clients.append(conn)
            print(addr[0] + ' connected')
            Thread(send_hi(conn, addr)).start()
        conn.close()
        self.server.close()


if __name__ == "__main__":
    s1 = Server('Sproba')
