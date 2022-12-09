import socket
import gzip
from io import BytesIO

# code borrowed from https://gist.github.com/dhilst/7435a09b4419da349bb4cc4ae855a451
def delegate(to, *methods):
    '''
    Class decorator to delegate methods to another objects.
    >>> @delegate('v', 'upper')
    ... @delegate('v', 'lower')
    ... @delegate('v', 'wrong_method')
    ... @delegate('not_an_attribute', 'wrong_attribute')
    ... class Foo:
    ...     def __init__(self, v):
    ...         self.v = v
    >>>
    >>> Foo('foo').upper()
    'FOO'
    >>> Foo('FOO').lower()
    'foo'
    >>> Foo('foo').wrong_method()
    Traceback (most recent call last):
        ...
    AttributeError: 'str' object has no attribute 'wrong_method'
    
    >>> Foo('foo').wrong_attribute()
    Traceback (most recent call last):
        ...
    AttributeError: 'Foo' object has no attribute 'not_an_attribute'
    You can use pass any number of methods to delegate
    >>> @delegate('v', 'upper', 'lower')
    ... class Foo:
    ...     def __init__(self, v):
    ...         self.v = v
    '''
    def dec(klass):
        def create_delegator(method):
            def delegator(self, *args, **kwargs):
                obj = getattr(self, to)
                m = getattr(obj, method)
                return m(*args, **kwargs)
            return delegator

        for m in methods:
            setattr(klass, m, create_delegator(m))
        return klass
    return dec


@delegate('socket', 'close', 'getpeername')
class GzipSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode="w")
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())

    # def close(self):
    #     self.socket.close()

    # def getpeername(self):
    #     return self.socket.getpeername()


@delegate('socket', 'close', 'getpeername')
class LogSocket():
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        print(
            "Sending {0} to {1}".format(
                data, self.socket.getpeername()[0]
            )
        )
        self.socket.send(data)

    # def close(self):
    #     self.socket.close()

    # def getpeername(self):
    #     return self.socket.getpeername()

def respond(client, message):
    client.send(bytes(message, "utf8"))
    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 2402))
server.listen(1)
try:
    while True:
        client, addr = server.accept()
        # client = LogSocket(LogSocket(GzipSocket(client)))
        message = input("Enter a value: ")
        if "gzip" in message:
            client = GzipSocket(client)
        if "log" in message:
            client = LogSocket(client)

        
        respond(client, message)
finally:
    server.close()


