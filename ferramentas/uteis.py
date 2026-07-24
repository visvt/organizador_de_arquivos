import os

def pedir_pasta_valida():
    while True:
        pasta = input ("Digite o caminho da pasta: ").strip()

        # os.path.isdir(pasta) verifica se o caminho existe e é uma pasta e não um arquivo
        if os.path.isdir(pasta):
            return pasta

        print (f"A pasta {pasta} não é válida. Tente novamente.")