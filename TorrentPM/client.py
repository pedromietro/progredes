#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import base64

class client:
    HOST = ''     # Endereco IP do Servidor
    PORT = 40030           # Porta que o Servidor esta
    BUFFER_SIZE = 1024
    
    def __init__(self):
        HOST = ''     # Endereco IP do Servidor
        PORT = 40030            # Porta que o Servidor esta
        BUFFER_SIZE = 1024
        conection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        destination = (HOST, PORT)
        conection.connect(destination)
        print 'Conex�o Aberta!\n'

    def sendMessage(xmlEncode):
        conection.send(xmlEncode)
        print 'Mensagem Enviada!'
        print xmlEncode

    def closeConection():
        tcp.close()

    def encode(xml):
        file_encoded = base64.b64encode(xml) # ver como vai ser com arquivo



c=client()