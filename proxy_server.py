import socket
import threading

def main():
    proxyServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxyServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    proxyServer.bind(("127.0.0.1", 8080))
    proxyServer.listen(2)

    while True:
        con, addr = proxyServer.accept()
        thread = threading.Thread(target=handleCon, args=(con, addr))
        thread.run()


def handleCon(con, addr):
    print(f"Connected by {addr}")
    fullData = b""
    while True:
        data = con.recv(4096)
        if not data:
            break
        fullData += data

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect("www.google.com", 80)
    server.send(fullData)
    server.shutdown()
    info = server.recv(4096)
    res = b"" + info
    while len(info) > 0:
        info = server.recv(4096)
        res += info
    con.sendall(res)





if __name__ == "__main__":
    main()