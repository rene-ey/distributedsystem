import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 4444

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip,port))
    server.listen(5) #

    while True:
        client, adress = server.accept()
        print(f"Connection Estabished - {adress[0]}:{adress[1]}")

        string = client.recv(1024)
        string = string.decode("utf-8")
        string = string.upper()
        client.send(bytes(string, "utf-8"))

        client.close()