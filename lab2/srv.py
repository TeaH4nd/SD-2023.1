import socket
import select
import sys
import threading

import re
from dicionario import Dicionario

# define a localizacao do servidor
HOST = '' # vazio indica que podera receber requisicoes a partir de qq interface de rede da maquina
PORT = 10001 # porta de acesso

class Servidor:
    def __init__(self):
        '''Cria um socket de servidor e o coloca em modo de espera por conexoes.''' 

        #define a lista de I/O de interesse (jah inclui a entrada padrao)
        self.entradas = [sys.stdin]
        #armazena historico de conexoes 
        self.conexoes = {}
        # cria o socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Internet( IPv4 + TCP)

        # vincula a localizacao do servidor
        self.sock.bind((HOST, PORT))

        # coloca-se em modo de espera por conexoes
        self.sock.listen(5)

        # configura o socket para o modo nao-bloqueante
        self.sock.setblocking(False)

        # inclui o socket principal na lista de entradas de interesse
        self.entradas.append(self.sock)

        # cria lock para acesso ao dicionario
        self.lock = threading.Lock()

        # instancia o dicionario
        self.dicionario = Dicionario("srvData.json")

    def aceitaConexao(self):
        """Aceita o pedido de conexao de um cliente
        Saida: o novo socket da conexao e o endereco do cliente"""

        # estabelece conexao com o proximo cliente
        clisock, endr = self.sock.accept()

        # registra a nova conexao
        self.conexoes[clisock] = endr

        return clisock, endr

    def atendeRequisicoes(self, clisock, endr):
        """Recebe mensagens e as envia de volta para o cliente (ate o cliente finalizar)
        Entrada: socket da conexao e endereco do cliente
        Saida:"""

        while True:
            # recebe dados do cliente
            data = clisock.recv(1024)
            if not data:  # dados vazios: cliente encerrou
                print(str(endr) + "-> encerrou")
                clisock.close()  # encerra a conexao com o cliente
                return

            msg = str(data, encoding="utf-8")
            # print(str(endr) + ": " + msg)

            if msg.startswith('ADD'):
                msg = re.search(r"\[(.*?)\]", msg).group(1)
                chave, valor = msg.split(':')
                with self.lock:
                    valores_salvos = self.dicionario.add(chave, valor)
                response = bytes(f"Adicionado com sucesso. A chave '{chave}' possui os valores: {valores_salvos}.",encoding="utf-8",)
            elif msg.startswith('CON'):
                chave = re.search(r"\[(.*?)\]", msg).group(1)
                with self.lock:
                    valores = self.dicionario.con(chave)
                response = bytes(f"Os valores associados a chave '{chave}' são: {valores}",encoding="utf-8",)

            clisock.sendall(response)  # envia a resposta para o cliente


    def executa(self):
        """Inicializa e implementa o loop principal (infinito) do servidor"""
        clientes = []  # armazena as threads criadas para fazer join
        print('Esperando conexões...')
        print('Digite REM[chave] para remover uma chave do dicionario.')
        while True:
            # espera por qualquer entrada de interesse
            leitura, escrita, excecao = select.select(self.entradas, [], [])
            # tratar todas as entradas prontas
            for pronto in leitura:
                if pronto == self.sock:  # pedido novo de conexao
                    clisock, endr = self.aceitaConexao()
                    print("Conectado com: ", endr)
                    # cria nova thread para atender o cliente
                    cliente = threading.Thread(target=self.atendeRequisicoes, args=(clisock, endr))
                    cliente.start()
                    clientes.append(cliente)  # armazena a referencia da thread para usar com join()
                elif pronto == sys.stdin:  # entrada padrao
                    cmd = input()
                    if cmd == "fim":  # solicitacao de finalizacao do servidor
                        for c in clientes:  # aguarda todas as threads terminarem
                            c.join()
                        self.sock.close()
                        sys.exit()
                    elif cmd == "hist":  # outro exemplo de comando para o servidor
                        print(str(self.conexoes.values()))
                    elif cmd.startswith("REM"):  # remover chave do dicionario
                        chave = re.search(r"\[(.*?)\]", cmd).group(1)
                        with self.lock:
                            self.dicionario.rem(chave)

if __name__ == "__main__":
    servidor = Servidor()
    servidor.executa()
