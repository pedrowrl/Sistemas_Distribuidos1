#Aluno: Pedro Wilson Rodrigues de Lima.
#Nº de Matrícula: 2020267.

import socket
import sys

HOST = ''  # <-- endereço IP do servidor 
PORT = 8888  # <-- porta do servidor
BUFFER_SIZE = 1024  # <-- tamanho máximo dos dados que poderão ser recebidos

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((HOST, PORT))

while True:

    data, address = sock.recvfrom(BUFFER_SIZE)
    
    inverted_data = data[::-1]
    
    sock.sendto(inverted_data, address)
