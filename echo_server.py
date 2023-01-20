import socket


def main():
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    con.bind(("", 8001))
    con.listen(2)

    while True:
        connect, address = con.accept()
        print(f"Connected by {address}")

        fullData = connect.recv(1024)
        connect.sendall(fullData)
        connect.close()

if __name__ == "__main__":
    main()