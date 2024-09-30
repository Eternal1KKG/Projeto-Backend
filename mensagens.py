import random

def obter_mensagem_aleatoria():
    mensagens = [
        "Olá usuário!",
        "Olá, mundo!",
    ]

    return random.choice(mensagens)