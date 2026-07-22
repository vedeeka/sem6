import socket 
serverPort = 8080
host="127.0.0.1"

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,serverPort))
s.listen(1)

while True:
    conn,adrr=s.accept()
    rec=conn.recv(1024).decode()
    print(rec)


    filepath = "mcn_practical/webserver/index.html"
        
    if filepath == "favicon.ico":
            connectionSocket.close()
            continue

    with open(filepath,'rb') as f:
        outputdata=f.read()

    response=b"HTTP/1.1 200 OK \r\n"
    response+=b"Content-type: text/html;charset=utf-8 \r\n"
    response += b"Content-Length: " + str(len(outputdata)).encode() + b"\r\n"
    response+=b"Connection : close \r\n"
    response+=b"\r\n"


    conn.sendall(response)
    conn.sendall(outputdata)
