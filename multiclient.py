import socket
import requests


def make_connection(host, port, data_to_send):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	s.sendall(bytes(''.join(data_to_send), 'utf-8'))
	b = []
	while True:
	 	data = s.recv(1024)
	 	if data:
	 		b.append(data)
	 	else:
	 		break

	file = open('mydify.html','w')
	file.write(b''.join(b).decode('utf-8'))
	file.close()


if __name__=='__main__':
	import sys
	host, port = sys.argv[1].split(':')
	link = 'http://habrahabr.ru/company/yandex/blog/258673/';
	data_to_send = requests.get(link).text
	# with open ("index.html", "r") as myfile:
	# 	data_to_send = myfile.readlines()
	make_connection(host, int(port), data_to_send)			