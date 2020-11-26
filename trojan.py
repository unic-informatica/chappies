import os
import subprocess
import telnetlib
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"Hostname, {hostname}")
print(f"Ip_address, {ip_address}")