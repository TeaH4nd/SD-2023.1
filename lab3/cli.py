import rpyc

HOST = 'localhost'  # maquina onde esta o servidor
PORTA = 10001       # porta que o servidor esta escutando

# Classe cliente para interagir com o dicionário remoto
class Cliente:
    def __init__(self):
        self.conn = rpyc.connect(HOST, PORTA)  # Conectar ao servidor na porta 5000

    def query(self, key):
        values = self.conn.root.query(key)
        return values

    def write(self, key, value):
        response = self.conn.root.write(key, value)
        return response

    def remove(self, key):
        response = self.conn.root.remove(key)
        return response

# Função para exibir as opções do menu e obter a escolha do usuário
def show_menu():
    print("======= Dicionário Remoto =======")
    print("1. Consultar")
    print("2. Escrever")
    print("3. Remover")
    print("0. Sair")
    choice = input("Escolha uma opção: ")
    return choice

# Função principal do cliente
def run_client():
    client = Cliente()
    while True:
        choice = show_menu()
        if choice == "1":
            key = input("Informe a chave: ")
            values = client.query(key)
            print(f"Valores associados à chave '{key}': {values}")
        elif choice == "2":
            key = input("Informe a chave: ")
            value = input("Informe o valor: ")
            response = client.write(key, value)
            print(response)
        elif choice == "3":
            key = input("Informe a chave: ")
            response = client.remove(key)
            print(response)
        elif choice == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    run_client()
