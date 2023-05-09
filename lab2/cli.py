import sys
import socket

HOST = 'localhost' # maquina onde esta o servidor
PORTA = 10001       # porta que o servidor esta escutando

class Cliente:
    def __init__(self, host, porta):
        self.host = host
        self.porta = porta
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    def printCabecalho(self):
        print('Digite [1, 2, ou fim] para escolher uma das opções abaixo:')
        print('1 - Adicionar')
        print('2 - Consultar')
        print('fim')

    def iniciaConexao(self):
        '''Cria um socket de cliente e conecta-se ao servidor.'''
         # Internet (IPv4 + TCP)
        print(f"Conectando à: {self.host}:{self.porta}", end='...')
        try:
            self.sock.connect((self.host, self.porta))
            print('Ok!')
        except ConnectionRefusedError:
            print('Error')
            print(f'Conexão recusada, verifique se {HOST} esta ligado.')
            sys.exit(1)

    def terminaConexao(self):
        self.sock.close()
        print("Conexão encerrada!")

    def encapsulaMsg(self, tipo, msg):
        '''Encapsula a mensagem para ser enviada ao servidor'''
        if tipo == 1:
            return f'ADD[{msg}]'
        elif tipo == 2:
            return f'CON[{msg}]'

    def fazRequisicoes(self):
        '''Faz requisicoes ao servidor e exibe o resultado.'''
        # le as mensagens do usuario ate ele digitar 'fim' 
        self.printCabecalho()
        msg = input('Opção: ')
        while msg != 'fim':
            if msg == '1':
                chave = input('Chave: ')
                valor = input('Valor: ')
                msg = self.encapsulaMsg(1, f'{chave}:{valor}')
            if msg == '2':
                chave = input('Chave: ')
                msg = self.encapsulaMsg(2, f'{chave}')
            # envia a mensagem do usuario para o servidor
            self.sock.sendall(msg.encode('utf-8'))

            #espera a resposta do servidor
            msg = self.sock.recv(1024)

            # imprime a mensagem recebida
            print(f"> {str(msg,encoding='utf-8')}")

            print()
            self.printCabecalho()
            msg = input('Opção: ')

        # encerra a conexao
        self.terminaConexao()

    def executa(self):
        '''Método principal para executar o loop do cliente.'''
        self.iniciaConexao()
        self.fazRequisicoes()


if __name__ == '__main__':
    cliente = Cliente(HOST, PORTA)
    cliente.executa()
 