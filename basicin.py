import socket

host = "1.1.1.1"            



for port in range(50, 54):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.settimeout(1)
		sock.connect((host, port))
		sock.sendall(b"Hello")
		resp = sock.recv(1024)
		sock.close()
		print(resp)
		break
	except Exception as e:
		print(e)
	finally:
		sock.close()