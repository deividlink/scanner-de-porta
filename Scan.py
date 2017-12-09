import socket
from time import sleep
__Author__="Deivid K.l"


def time_loop():
    for a in range(10):
        sleep(0.1)

ip = input("digite seu ip:")
while True:
    for port in range(8000,10000):
         time_loop()
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         try:
          s.connect((ip, int(port)))
          print('Port {} Aberta'.format(port))
         except:
          print('Port {} Fechada'.format(port))
          s.close()
