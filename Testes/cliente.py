import socket

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

servidor = input("Informe o servidor: ")
porta = int(input("Infome a porta: "))

cliente.connect((servidor,porta))

print("Digite SAIR para terminar o chat.")

while True:
    cliente.send(input("Mensagem: ").encode("UTF-8"))
    
    msg = cliente.recv(1024).decode("UTF-8")
    
    if msg == "SAIR":                     
        break
    else:
        print(msg)

cliente.close()     
