import os
import shutil

CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".odt"],
    "Planilhas": [".xls", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audios": [".mp3", ".wav", ".flac"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
}

def obter_categoria (extensao, categorias, extensoes_desconhecidas): # Caso o tenha arquivos com extensões que não foram declaradas no diciónário
    #Se o usuário digitar um nome (ex: "Instaladores"), usa isso como nome da pasta de destino
    # Se o usuário deixar em branco, guarda None — isso significa "pular esse tipo de arquivo sempre"
    # extensoes_desconhecidas funciona como um cache: guarda a decisão do usuário pra não perguntar de novo pra mesma extensão
    # Já vimos essa extensão antes nesta execução?
    if extensao in extensoes_desconhecidas:
        return extensoes_desconhecidas[extensao]

    # Procura nas categorias já conhecidas
    for categoria, extensoes in categorias.items():
        if extensao in extensoes:
            return categoria

    # Extensão desconhecida: pergunta ao usuário
    print (f"Extensão desconhecida: '{extensao}'")
    resposta = input (f"Digite o nome da categoria para arquivos '{extensao}'"
                      f"(ou deixe em branco para pular este arquivo): ").strip() #.strip() retira espaços em branco e quebras de linha do início e fim do texto, não mexe no meio

    if resposta == "":
        extensoes_desconhecidas[extensao] = None # marca para pular sempre
        return None

    extensoes_desconhecidas[extensao] = resposta
    return resposta

def pedir_pasta_valida():
    while True:
        pasta = input ("Digite o caminho da pasta a organizar: ").strip()

        # os.path.isdir(pasta) verifica se o caminho existe e é uma pasta e não um arquivo
        if os.path.isdir(pasta):
            return pasta

        print (f"A pasta {pasta} não é válida. Tente novamente.")

def executar ():
    pasta = pedir_pasta_valida()

    # Dicionário "cache" que vai guardar decisões sobre extensões desconhecidas, para não perguntar a mesma coisa várias vezes
    extensoes_desconhecidas = {}

    # os.listdir(pasta) lista tudo que tem na pasta
    for nome_arquivo in os.listdir(pasta):

        # os.path.join junta a pasta + o nome do arquivo formando o caminho completo
        caminho_completo = os.path.join(pasta, nome_arquivo)

        # os.path.isfile filtra só arquivos (ignora subpastas)
        # Isso evita tentar "organizar" uma pasta que já esteja lá dentro
        if os.path.isfile(caminho_completo):

            # os.path.splitext Separa nome e extensão
            # [1] pega o segundo item da tupla, ou seja, só a extensão .lower() deixa tudo minúsculo, pra ".JPG" e ".jpg"
            extensao = os.path.splitext(nome_arquivo)[1].lower()


            categoria = obter_categoria (extensao, CATEGORIAS, extensoes_desconhecidas)

            if categoria is None:
                continue

            pasta_destino = os.path.join (pasta, categoria)

            # os.makedirs cria a subpasta se ela ainda não existir e garante que a subpasta de destino existe
            # exist_ok=True evita erro caso ela já exista
            os.makedirs (pasta_destino, exist_ok=True)

            #shutil.move move o arquivo de verdade, do caminho original paara a pasta de destino
            shutil.move(caminho_completo, pasta_destino)

            print (f"{nome_arquivo} -> {categoria}")

print ("Organização concluída! *~º¨*")