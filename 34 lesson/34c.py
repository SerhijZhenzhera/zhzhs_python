'''
Task 3.Echo server with threading
Create a socket echo server that handles each connection using the multiprocessing library
'''

# [https://stackoverflow.com/questions/44257579/zeromq-hangs-in-a-python-multiprocessing-class-object-solution]
'''
[https://habr.com/ru/post/483586/] Разберем пример простого key/value хранилища, например такого как memcache.
Устроен он просто — данные хранятся в памяти, в структуре hashmap. Доступ к ним осуществлятся через tcp-сокет.
В питоне hashmap — это обычный dict. Для доступа будем использовать zeromq.
Для установки этого пакета в debian/ubuntu достаточно ввести в консоли
sudo apt-get install libzmq-dev
sudo pip install zmq
'''

#mpzmq_class.py

from multiprocessing import Process
import zmq


class Base(Process):
    """
    Inherit from Process and
    holds the zmq address.
    """
    def __init__(self, address):
        super().__init__()
        self.address = address


class Server(Base):
    def run(self):
        ctx = zmq.Context()
        socket = ctx.socket(zmq.PULL)
        socket.connect(self.address)
        msg = socket.recv_string()
        print(msg)


class Client(Base):
    def run(self):
        ctx = zmq.Context()
        socket = ctx.socket(zmq.PUSH)
        socket.bind(self.address)
        msg = "Hello World!"
        socket.send_string(msg)


if __name__ == "__main__":
    server_addr = "tcp://127.0.1:6068"
    client_addr = "tcp://*:6068"
    s = Server(server_addr)
    c = Client(client_addr)
    s.start()
    c.start()
    s.join()
    c.join()
