import socket # Importa o módulo socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket e o binda ao endereço
tcp.bind((HOST, PORT)) # bind ao endereço e inicia o servidor
tcp.listen(1) # Aceita conexões de um cliente
print("listado na porta ", PORT) # Mostra a porta que o servidor está escutando

def close():  # Função para fechar a conexão
    tcp.close() # Fecha a conexão
    print("Servidor encerrado")

def main(): # Função principal
    while True: # Loop infinito
        conn, addr = tcp.accept() # Aceita conexão do cliente
        print("Conectado a: ", addr) # Mostra o endereço do cliente
        while True: # Loop infinito
            data = conn.recv(1024) # Recebe dados do cliente e armazena em data (1024 é o tamanho do buffer) 
            print(data.decode()) # Mostra o dado recebido do cliente em formato de string (decode é para transformar em string)
            if not data: # Se o dado recebido for nulo entra no if
                break # Sai do loop
            conn.sendall(data) # Envia o dado recebido do cliente para o cliente
        tcp.close() # Fecha a conexão
        print("Conecxão encerrada")

main()