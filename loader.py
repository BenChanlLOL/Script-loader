#loader.py
import socket
sock = socket.socket()
print(" the payload must be in the folder and called 'payload'"
payload1 = open("payload")
payload2 = payload1.read
con = input("what IP should we connect to?")
port = int(input("what port"))
sock.connect((con, port))
sock.send(payload.encode(utf-8))
print("sent payload")
sock.close()
