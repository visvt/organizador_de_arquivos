import os
from ferramentas.uteis import pedir_pasta_valida

def renomear_sequencial(pasta):
    prefixo = input ("Digite o prefixo (nome) desejado: ").strip()

    numero_inicial_input = input ("Número inicial da sequencia: ").strip()
    numero_atual = int (numero_inicial_input) if numero_inicial_input else 1  # Expressão condicional, se o usuário digitar algo, converte para número, senão, usa 1 como padrão

    digitos_input = input ("Quantidade de digitos: ").strip()
    digitos = int(digitos_input) if digitos_input else 3

    arquivos = [nome for nome in os.listdir(pasta)
                if os.path.isfile(os.path.join(pasta, nome))]   

    for nome_antigo in arquivos:
        extensao = os.path.splitext (nome_antigo)[1]

        numero_formatado = str(numero_atual).zfill(digitos)  # preenche com zeros à esquerda até atingir o tamanho desejado.
        nome_novo = f"{prefixo}_{numero_formatado}{extensao}"

        caminho_antigo = os.path.join(pasta, nome_antigo)
        caminho_novo = os.path.join(pasta, nome_novo)

        os.rename(caminho_antigo, caminho_novo)  # Enquanto shutil.move move entre pastas, os.rename() muda o nome mantendo o arquivo no mesmo lugar
        print (f"{nome_antigo} -> {nome_novo}")

        numero_atual += 1

    print ("Renomeação concluída")

def renomear_busca_substituicao(pasta):
    print ("Em construção")

def executar():
    pasta = pedir_pasta_valida()

    print ("Como gostaria de renomear?")
    print ("1 - Prefixo + número sequencial")
    print ("2 - Busca e substituição de texto")
    modo = input ("Escolha uma opção: ").strip()

    match modo:
        case "1":
            renomear_sequencial(pasta)

        case "2":
            renomear_busca_substituicao(pasta)

        case _:
            print ("Opção inválida.")