import socket
from .model_predef import PORT
from .model_predef import IP
from .model_predef import BUFFER_SIZE


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, PORT))
    s.listen(1)

    conn, addr = s.accept()
    print('Starting server on address:', addr)
    while 1:
        data = conn.recv(BUFFER_SIZE)

        if not data:
            break
        print("received data:", data)
        conn.send(data)
    conn.close()
