from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("210.41.100.124", 9999))
serverSocket.listen(1)
# This blocks when there is no client link
connectionSocket, addr = serverSocket.accept()
while True:
    print('waiting for connection...')
    try:
        # receive 1k data
        data = connectionSocket.recv(1024)
        print(data)
        if not data:
            continue
        # data is geting http request message
        filename = data.split()[1]  # filename = /HelloWorld.html
        # #print(filename[1:])
        f = open(filename[1:], encoding="utf-8")  # f = HelloWorld.html
        outputdata = f.read()
        header = 'HTTP/1.1 200 OK\r\n\r\n'
        # Reply message
        connectionSocket.send(header.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
    #connectionSocket.close()
    except IOError:
        header = 'HTTP/1.1 404 NOT FOUND\r\n\r\n'
        connectionSocket.send(header.encode())
        connectionSocket.close()
# Browser key localhost:***/index.html will have two request
# index.html && favicon.ico(Website icon)
