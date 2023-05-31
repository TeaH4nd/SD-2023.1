import sys
import rpyc

HOST = 'localhost'  # maquina onde esta o servidor
PORTA = 10001       # porta que o servidor esta escutando

# Classe cliente para interagir com o dicionário remoto
class Cliente:
    def __init__(self, host, porta):
        print(f"Conectando à: {host}:{porta}", end='...')
        try:
            self.conn = rpyc.connect(host, porta)  # Conectar ao servidor
        except ConnectionRefusedError:
            print('Error')
            print(f'Conexão recusada, verifique se {HOST} esta ligado.')
            sys.exit(1)

    def query(self, key):
        values = self.conn.root.exposed_query(key)
        return values

    def write(self, key, value):
        response = self.conn.root.exposed_write(key, value)
        return response

    def remove(self, key):
        response = self.conn.root.exposed_remove(key)
        return response
    # Função principal do cliente
    def run_client(self):
        while True:
            choice = show_menu()
            if choice == "1":
                key = input("Informe a chave: ")
                values = client.query(key)
                print(f"R: Valores associados à chave '{key}': {values}")
            elif choice == "2":
                key = input("Informe a chave: ")
                value = input("Informe o valor: ")
                response = client.write(key, value)
                print(f'R: {response}')
            elif choice == "3":
                key = input("Informe a chave: ")
                response = client.remove(key)
                print(f'R: {response}')
            elif choice == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")

# Função para exibir as opções do menu e obter a escolha do usuário
def show_menu():
    print()
    print("======= Dicionário Remoto =======")
    print("1. Consultar")
    print("2. Escrever")
    print("3. Remover")
    print("0. Sair")
    choice = input("Escolha uma opção: ")
    return choice


if __name__ == "__main__":
    client = Cliente(HOST, PORTA)
    client.run_client()
