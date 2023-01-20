#!/usr/bin/env python3
import socket
con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    host = socket.gethostbyname("www.google.com")
    port = 80
    try:
        con = socket.create_connection((host, port));
    except:
        print("Connection Failed")
    else:
        try:
            con.send("GET / HTTP/1.1\n".encode("utf-8"))
            fullData = b""
            while True:
                data = con.recv(4096)
                if not data:
                    break
                fullData += data
            print(fullData)
        except Exception as e:
            print(e)
        finally:
            con.close()


if __name__ == "__main__":
    main()
