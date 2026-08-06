import os

def pedir_pasta_valida():
    while True:
        pasta = input ("Digite o caminho da pasta: ").strip()

        # os.path.isdir(pasta) verifica se o caminho existe e é uma pasta e não um arquivo
        if os.path.isdir(pasta):
            return pasta

        print (f"A pasta {pasta} não é válida. Tente novamente.")


def pedir_arquivo_valido():
    while True:
        caminho = input("Digite o caminho da planilhas (.csv ou .xlsx): ").strip()

        if os.path.isfile(caminho):
            return caminho

        print (f"O arquivo {caminho} não existe. Tente novamente.")        