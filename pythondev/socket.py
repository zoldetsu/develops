import socket


HOST = (socket.gethostname(),10000)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(HOST)

s.listen()
print("i am listening your connections")


while True:
    conn, addr = s.accept()
    print("Connect - ", addr)
    res = b"Hello, my friend"
    conn.send(res)