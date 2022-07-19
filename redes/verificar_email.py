import login as log
def verificar_email(): # Função para verificar e-mail
    with open ("caixa de entrada/email.txt", "r") as email: # Abre o arquivo
        linha = email.readlines() # Le o arquivo
        cont = 0 # Contador
        usuario = log.usuario # Usuário logado
        for i in linha:

            if 'Para: '+usuario+'\n' in i: # Verifica se o usuário tem e-mail
                cont += 1
        print("Você tem {} e-mails".format(cont)) # Mostra quantos e-mails tem

        print("----------------")
        print("Deseja visualizar um e-mail? (s/n)")
        opcao = input()
        if opcao == "s": # Se o usuário desejar visualizar um e-mail
            print("----------------")
            print("Digite o número do e-mail que deseja visualizar")
            numero = int(input())
            print("----------------")
            for i in range(len(linha)):
                if 'Para: '+usuario+'\n' in linha[i]: # mostra pro usuario seus e-mail
                    for i in linha:
                        print(i)
                    if linha == '':
                        print("----------------")
                        break
            
            

def enviar_email(): # Função para enviar e-mail
    email = open("caixa de entrada/email.txt", "a") # Abre o arquivo
    de = log.usuario # Usuário logado
    email_envia = input("para quem você deseja enviar: ") # Usuário que recebe o e-mail
    assunto = input("assunto: ") # Assunto do e-mail
    mensagem = input("mensagem: ") # Mensagem do e-mail
    email.write("----------------\n De:{}\n Para: {}\n Assunto: {}\n Mensagem: {}\n".format(de, email_envia, assunto, mensagem))
    print("E-mail enviado")
    email.close() # Fecha o arquivo
    return email # Retorna o arquivo


