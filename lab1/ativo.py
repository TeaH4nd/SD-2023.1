# echo lado ativo
import sys
import socket

HOST = 'localhost'
PORTA = 5000

sock = socket.socket()
print(f"Conectando à: {HOST}:{PORTA}", end='...')
try:
    sock.connect((HOST, PORTA))
    print('Ok!')
except ConnectionRefusedError:
    print('Error')
    print(f'Conexão recusada, verifique se {HOST} esta ligado.')
    sys.exit(1)

print("Envie 'fim' para encerrar")

msg = input('Enviar: ')
while msg != 'fim':
    sock.send(bytes(msg, encoding='utf-8'))
    msg = sock.recv(1024);
    print(f"Echo: {str(msg,encoding='utf-8')}")
    msg = input('Enviar: ');

sock.close()