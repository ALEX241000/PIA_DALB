import socket
import os
import requests
from lxml import html
from bs4 import BeautifulSoup
import nmap
import hashlib
opc = int(input("¿Que desea hacer? \n 1 escanear un puerto TCP con nmap \n 2 cifrar con cesar \n 3 scraping de imagenes \n 4 servidor udp \n 5 encriptar un docuento txt con hash 512 \n"))
if opc == 1 :
    escaner = nmap.PortScanner()
    escaner.scan('127.0.0.1', '1-1024')
    print(escaner.scan('127.0.0.1', '1-1024', '-v -sV'))
    print(escaner.command_line())
    print(escaner.scaninfo())
    print(escaner.all_hosts())
    print(escaner['127.0.0.1'].hostname())
    print(escaner['127.0.0.1'].state())
    print(escaner['127.0.0.1'].all_protocols())
    print(escaner['127.0.0.1']['tcp'].keys())
    n = int(input("que puerto quieres verificar: \n "))
    print(escaner['127.0.0.1'].has_tcp(n))
    print(escaner['127.0.0.1']['tcp'][n])
    print(escaner['127.0.0.1']['tcp'][n]['product'])
if opc == 2 :
    sim = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    r = " "
    men = input("introduze un mensaje ")
    key = int(input("introduze una clave "))
    ci = int(input("¿deseas cifrar(1) o desifrar(2)? "))
    for simon in men:
        if simon in sim:
            isimo = sim.find(simon)
            if ci == 1:
                indin = isimo + key
                if indin >= len(sim):
                    indin = indin - len(sim)
                elif indin < 0:
                    indin = indin + len(sim)
                r = r + sim[indin]
            elif ci == 2:
                indin = isimo - key
                r = r + sim[indin]
            else:
                print("te equivocaste")
                exit()
    print(r)
    with open('reporte_cesar.txt', 'w') as esc:
        esc.write(r)    
elif opc == 3 :
    url = input("introduce la url \n ")
    print("descargando imagenes de:"+ url)
    try:
        res = requests.get(url)  
        pana = html.fromstring(res.text)
        ima = pana.xpath('//img/@src')
        print ('Imagenes %s encontradas' % len(ima))
        os.system("mkdir images")
        for j in ima:
            if j.startswith("http") == False:
                desca = url + image
            else:
                desca = j
                print(desca)
                ro = requests.get(desca)
                f5 = open('images/%s' % desca.split('/')[-1], 'wb')
                f5.write(ro.content)
                f5.close()
        print("se a creado una carpeta con imagenes")
                
    except Exception as e:
        print(e)
        print ("Error conexion con " + url)
        pass

elif opc == 4 :
#este viene con otro programa de cliente udp para que funcione
#se tiene que abrir primero el servidor
    ipl = "127.0.0.1"
    pl = 2000
    buffer = 1024
    udpserver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpserver.bind((ipl, pl))
    print("Servidor UDP listo para recibir preguntas")
    while(True):
        reci = udpserver.recvfrom(buffer)
        men = reci[0]
        ip = reci[1]
        print("pregunta: " + men.decode())
        re = input("respuesta: ")
        udpserver.sendto(str.encode(re), ip)
elif opc == 5:
#para este se necesita un archivo txt con 100 paswords
    lista = open("100passwords.txt","r",errors='ignore').readlines()
    arr = []
    for i in lista:
        sha512 = hashlib.sha512(i.encode())
        r = sha512.hexdigest()
        arr.append(r)
        with open('pasword_hash512.txt', 'w') as tabla:
           for j in arr:
            tabla.write(j)
    print("se ha creado un documento txt con los hashes")
else :
    print("te equivocaste opcion no valida")

