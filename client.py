# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 11:42:54 2020

@author: Anton
"""

import socket
server_address=('localhost',5050) #menentukan alamat server
SIZE=1024 #menentukan ukuran buffer
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #membuat objek socket
s.connect(server_address) #menghubungkan socket ke alamat server
while True:
    pesan=s.recv(1024) #menerima pesan
    print ("Server :",pesan)  #pesan yang diterima dari server
    pesan=input("Anda : ") #menginput pesan
    s.send(pesan.encode()) #mengirim pesan