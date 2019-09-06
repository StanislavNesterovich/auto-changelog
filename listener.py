
from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


while True:
    client, addr = s.accept()
    print("test" % str(addr))
    print(client)
    timestr = time.ctime(time.time()) + "\r\n"
    client.send(timestr.encode('ascii'))
    client.close()