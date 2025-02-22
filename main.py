import mensagens

def saudar_usuario_e_enviar_mensagem(nome):
    return f"Olá {nome}!\nMensagem: {mensagens.obter_mensagem_aleatoria()}"

def main():
    #saudação de abertura
    print("### Bem-vindo ao programa da aula 03. ###")

    #Captura o nome do usuário
    nome = input("Por favor, informe o seu nome: ")

    #Gera a mensagem
    mensagem = saudar_usuario_e_enviar_mensagem(nome)

    #Exibe a mensagem final
    print("\n" + mensagem)

    print("\n\n### Fim do  programa. ###")

if __name__ == '__main__':
    main()