# echo lado passivo

import socket

HOST = ''
PORTA = 5000
sock = socket.socket()
sock.bind((HOST, PORTA))
sock.listen(1)

print('Esperando conexões...')
novoSock, endereco = sock.accept()
print(f'Conectado com: {endereco}\n\tPronto para repetir')

while True:
    msg = novoSock.recv(1024)
    if not msg:
        break
    else:
        #print(str(msg, encoding='utf-8'))
        if str(msg, encoding='utf-8') != 'fim':
            novoSock.send(msg)
        else:
            break

novoSock.close()
sock.close()