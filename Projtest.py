import socket
UDP_IP = "192.168.0.19"
UDP_PORT = 23
MESSAGE = "(REA1)"

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))