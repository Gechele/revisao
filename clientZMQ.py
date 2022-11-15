from email import message
from multiprocessing import context
from socket import socket
import zmq

context = zmq.Context()

print("Conectando")

socketEconomia = context.socket(zmq.SUB)
socketEconomia.connect("tcp://localhost:5555")
socketEconomia.setsockopt(zmq.SUBSCRIBE, b"Economia")


socketEntretenimento = context.socket(zmq.SUB)
socketEntretenimento.connect("tcp://localhost:5555")
socketEntretenimento.setsockopt(zmq.SUBSCRIBE, b"Entretenimento")


socketEsportes = context.socket(zmq.SUB)
socketEsportes.connect("tcp://localhost:5555")
socketEsportes.setsockopt(zmq.SUBSCRIBE, b"Esportes")


socketPolitica = context.socket(zmq.SUB)
socketPolitica.connect("tcp://localhost:5555")
socketPolitica.setsockopt(zmq.SUBSCRIBE, b"Politica")


socketBemEstar = context.socket(zmq.SUB)
socketBemEstar.connect("tcp://localhost:5555")
socketBemEstar.setsockopt(zmq.SUBSCRIBE, b"Bem-estar")



while True:
    messageEconomia = socketEconomia.recv()
    messageEntretenimento = socketEntretenimento.recv()
    messageEsportes = socketEsportes.recv()
    messagePolitica = socketPolitica.recv()
    messageBemEstar = socketBemEstar.recv()

    
    print(f"Recebido Economia [ {messageEconomia} ]")
    print(f"Recebido Entretenimento [ {messageEntretenimento} ]")
    print(f"Recebido Esportes [ {messageEsportes} ]")
    print(f"Recebido Politica [ {messagePolitica} ]")
    print(f"Recebido Bem-estar [ {messageBemEstar} ]")
