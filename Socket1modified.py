import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url = input("Introduzca la dirección a la que quiere acceder: ")
dominio = url.split("/")[2]
print(dominio)

try:
    mysock.connect((dominio, 80))
    cmd = 'GET ' + str(url) + ' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)
except:
    print("Introduciste una dirección que no se puede acceder")

letters= dict()
count = 0
while True:
    data = mysock.recv(512)
    count += len(data)
    if (len(data) < 1) or count >= 3000:
        break
    print (data.decode())
mysock.close()
print(count)