import argparse, socket
from datetime import datetime

MAX_BYTES = 65535

def cliente(porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = input('Digite a mensagem que deseja enviar para o servidor : ')
    data = text.encode('ascii')
    sock.sendto(data, ('127.0.0.1', porta)) # Possui uma mensagem e um endereço de destino
    print('Cliente >> O sistema operacional do cliente informou o IP e porta {}'.format(sock.getsockname())) # O SO atribui um IP e porta, na saída da chamada getsockname()
    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode('ascii')
    print('Cliente >> O servidor {} respondeu {!r}'.format(address, text))



cliente(1025)