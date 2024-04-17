import socket

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

servidor.bind(("localhost",8080))

servidor.listen()

cliente, end = servidor.accept()

while True:
    msg =cliente.recv(1024).decode("UTF-8")
    
    if msg == "SAIR":        
        break
    else:
        print(msg)
    
    cliente.send(input("Mensagem: ").encode("UTF-8"))        
    
cliente.close()
servidor.close()


    