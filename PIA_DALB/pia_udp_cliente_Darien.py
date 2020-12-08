import socket
import sys
server = ("127.0.0.1", 2000)
buffer = 1024
udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while(True):
    pregunta = input("introduze una pregunta, no olvide los signos ¿? y si quieres salir escribe bye ")
    if pregunta == "bye":
        udpsocket.close()
        sys.exit()
        exit()
    udpsocket.sendto(str.encode(pregunta), server)
    men = udpsocket.recvfrom(buffer)
    re = "respuesta" + men[0].decode()
    print(re)
