'''
Task 2
Echo server with threading
Create a socket echo server which handles each connection in a separate Thread
'''

# [https://stackoverflow.com/questions/24582545/multi-threading-tcp-echo-server-in-python]

import socket
from threading import Thread


class workingthread(Thread):
    def __init__(self, client, ip, port):
        Thread.__init___(self)
        self.client = client
        self.ip = ip
        self.port = port

    def run(self):
        data = client.recv(6000)
        print('Client Sent: ', data)
        client.send(data)


if __name__ == '__main__':

    tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsocket.bind(('0.0.0.0', 8000))
    tcpsocket.listen(5)
    (client, (ip, port)) = tcpsocket.accept()

    newthread = workingthread(client, ip, port)
    newthread.start()

'''
---output---

'''
