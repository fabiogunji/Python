import socket

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serv = input("Informe o servidor: ")
porta = int(input("Infome a porte: "))

servidor.bind((serv,porta))

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


    