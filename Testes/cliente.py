import socket

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cliente.connect("localhost",8080)

print("Digite SAIR para terminar o chat.")

while True:
    cliente.send(input("Mensagem: ").encode("UTF-8"))
    
    msg = cliente.recv(1024).decode("UTF-8")
    
    if msg == "SAIR":
        break
    else:
        print(msg)
        
cliente.close
