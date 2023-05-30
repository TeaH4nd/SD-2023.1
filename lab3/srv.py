import os
import json
import rpyc

from rpyc.utils.server import ThreadedServer
from dicionario import Dicionario

PORT = 10001 # porta de acesso

# Classe do servidor
class Servidor(rpyc.Service):
    def __init__(self):
        super().__init__()
        self.dictionary = Dicionario()

    def on_connect(self, conn):
        cliente_endr = conn._channel.stream.sock.getpeername()
        print("Conectado com:", cliente_endr)

    def on_disconnect(self, conn):
        self.dictionary.save_dictionary()

    def exposed_query(self, key):
        return self.dictionary.query(key)

    def exposed_write(self, key, value):
        return self.dictionary.write(key, value)

    def exposed_remove(self, key):
        return self.dictionary.remove(key)

# Iniciar o servidor
if __name__ == "__main__":
    server = ThreadedServer(Servidor, port=PORT)
    server.start()
