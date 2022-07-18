import socket
from turtle import clear
import login as log
import verificar_email as ve

HOST = "127.0.0.1"  # Endereco IP do Servidor
PORT = 65432      # Porta do Servidor

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
tcp.connect((HOST, PORT)) # Conecta ao servidor


def main(): # Função principal
    while True: # Loop infinito
        print("___________________")
        print("Bem vindo ao cliente")
        print("Para verificar e-mail digite 1")
        print("Para enviar e-mail digite 2")
        print("Para sair digite sair")
        print("___________________")


        opcao = input("Digite a opção: ")   # Recebe a opção do usuário
        if opcao == "1":
            print("Verificando e-mail")
            ve.verificar_email()

        elif opcao == "2":
            print("Enviando e-mail")
            ve.enviar_email()
        
        elif opcao == "sair":
            tcp.close()
            exit()
        else:
            print("Opção inválida")
            main()


main()