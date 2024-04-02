from dotenv import load_dotenv
import os

def autenticar(usuario, senha):
    usuario_correto = os.getenv("USUARIO")
    senha_correta = os.getenv("SENHA")

    if usuario == usuario_correto and senha == senha_correta:
        return True
    else:
        return False

def main():
    load_dotenv()
    
    usuario_correto = os.getenv("USUARIO")

    print("Bem-vindo ao sistema de autenticação!")

    tentativa = 1
    while True:
        if tentativa == 1:
            usuario = input("Usuário: ").strip()
        else:
            usuario = usuario_correto

        senha = input("Senha: ").strip()

        if autenticar(usuario, senha):
            print("Acesso concedido")
            break
        else:
            print("Senha incorreta. Tente novamente.")
            tentativa += 1

if __name__ == "__main__":
    main()