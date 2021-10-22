import socket

UDP_IP = "192.168.1.148"
UDP_PORT = 5005


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))




Clients = []




while True:
    try:
        while True:
            data, addr = sock.recvfrom(1024)

            message = data.decode('utf-8').split(" || ")[0]
            Qui = data.decode('utf-8').split(" || ")[1] + "#" + str(addr[1])

            print(f"received message: {message} by {Qui}")

            if not addr in Clients:
                Clients.append(addr)
            break

        for i in range(len(Clients)):
            if addr == Clients[i]:
                sock.sendto(f"Vous : {message}".encode(), (Clients[i][0], Clients[i][1]))

            else:
                sock.sendto(f"{Qui} : {message}".encode(), (Clients[i][0], Clients[i][1]))




        #print(Clients)
    except Exception as e:
        print(e)
