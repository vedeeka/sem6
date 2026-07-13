import socket
import threading

HOST = "127.0.0.1"
PORT = 8888

def handle_client(client):

    request = client.recv(4096)

    if not request:
        client.close()
        return

    text = request.decode(errors="ignore")

    print("\nRequest Received\n")
    print(text)

    # Get host name
    host = ""

    for line in text.split("\n"):
        if line.lower().startswith("host:"):
            host = line.split(":")[1].strip()
            break

    print("Connecting to:", host)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((host, 80))

    server.send(request)

    while True:
        data = server.recv(4096)

        if not data:
            break

        client.send(data)

    server.close()
    client.close()


proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

proxy.bind((HOST, PORT))

proxy.listen(5)

print("Proxy Server Running on Port", PORT)

while True:

    client, addr = proxy.accept()

    print("Connected:", addr)

    t = threading.Thread(target=handle_client, args=(client,))
    t.start()


#curl -x http://127.0.0.1:8888 http://example.com