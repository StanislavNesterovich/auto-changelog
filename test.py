import socket
import yaml
import json
HOST = '10.236.1.233'
PORT = 7777

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen(2)
  conn, addr = s.accept()

  print('Connected by', addr)
  while True:
    data = conn.recv(1024)
    if not data:
      break
    else:
      conn.sendall(data)
      data = data.decode('utf8').replace("'", '"')
      # print(type(data))
      print(data)