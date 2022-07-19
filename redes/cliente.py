import socket # Importa o módulo socket
from turtle import clear # Importa o módulo clear
import login as log # Importa o módulo login
import verificar_email as ve # Importa o módulo verificar_email

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

        elif opcao == "2": # Se a opção for 2 entra no if e envia o e-mail
            print("Enviando e-mail")
            ve.enviar_email()
        
        elif opcao == "sair": # Se a opção for sair entra no if e sai do programa
            tcp.close()
            exit()
        else:
            print("Opção inválida") # Se a opção for inválida entra no if e mostra a mensagem de erro
            main() # Chama a função principal


main() # Chama a função principal