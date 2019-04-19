from socket import *
ClientSocket = socket(AF_INET, SOCK_STREAM)
ClientSocket.connect(('localhost',9999))
while True:
	#There Connetction: close is different from the common keep-alive in Browser
	#close Indicates that the server is required to close the link after sending the requested object
	Head = '''GET /index.html HTTP/1.1\r\nHost: localhost:9999\r\nConnection: close\r\nUser-agent: Mozilla/5.0\r\n\r\n'''
	ClientSocket.send(Head.encode('utf-8'))
	data = ClientSocket.recv(1024)
	print(data)
	with open("response.html","wb") as f:
		f.write(data)
