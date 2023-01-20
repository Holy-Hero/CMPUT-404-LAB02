import socket


def main():
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con.connect("www.google.com", 80)
    con.send(b"GET / HTTP/1.1\nHost: " + "www.google.com".encode("utf-8"))
    con.shutdown(socket.SHUT_WR)
    res = con.recv(4096)

    while len(res) > 0:
        print(res)
        res = con.recv(4096)
    con.close()

if __name__ == "__main__":
    main()