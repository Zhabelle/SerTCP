import socket


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 65432))
    res = s.recv(1024)
    print(res)
    s.close()
