# coding: utf-8
import socket

hote = "192.168.1.232"
port = 135

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))

trame = "00 01 02 0F".encode()
socket.send(trame)

print("Close")
socket.close()
