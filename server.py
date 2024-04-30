import argparse, socket
from datetime import datetime

MAX_BYTES = 65535

def servidor(porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #cria um socket
    sock.bind(('127.0.0.1', porta)) 
    print('Servidor >> Escutando no IP e porta {}'.format(sock.getsockname()))

    while True: # Executa repetidamente recvfrom()
            data, address = sock.recvfrom(MAX_BYTES) # Recebe mensagens ate 65.535 bytes; retorna o endereço do cliente e conteúdo do datagrama no formato de bytes
            text = data.decode('ascii')
            print('Servidor >> O cliente no IP e porta {} enviou a mensagem {!r}'.format(address, text))
            text = 'Mensagem para o cliente: O dado enviado possui comprimento de {} bytes'.format(len(data))
            data = text.encode('ascii')
            sock.sendto(data, address) # Datagrama de resposta enviado ao cliente


servidor(1025)







