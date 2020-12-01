import socket
import sys

HOST = '192.168.1.94'
PORT = 6000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created")

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print("bind failed")
    sys.exit()
print("bind complete")

s.listen(10)
print("started listening")
conn, addr = s.accept()
print("connected to" + addr[0] + ":" + str(addr[1]))

while True:
    data = conn.recv(1024)
    line = data.decode('UTF-8')
    line = line.replace("\n","")
    print(line)
    cmmd = input('Enter Command : ')
    cmmd = cmmd.encode()
    conn.send(cmmd)
    print("command send")
s.close()
