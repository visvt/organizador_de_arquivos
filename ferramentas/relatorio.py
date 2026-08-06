import os
import pandas as pd
from ferramentas.uteis import pedir_arquivo_valido

#df.shape                tupla (num_linhas, num_colunas)
#df.columns              lista com o nome das colunas
#df["Preço"]             Seleciona só a coluna "Preço"
#df["Preço"].sum()       Soma todos os valores da coluna
#df["Preço"].mean()      Calcula a média
#df["Preço"].min()       Valor mínimo
#df["Preço"].max()       Valor máximo

def ler_planilha(caminho_arquivo):
    extensao = os.path.splitext(caminho_arquivo)[1].lower()

    if extensao == ".csv":
        return pd.read_csv(caminho_arquivo)
    elif extensao in (".xlsx", ".xls"):         #o in verifica se extensao é uma das opções dentro da tupla (".xlsx", ".xls")
        return pd.read_excel(caminho_arquivo)
    else:
        return None

def mostrar_resumo(df):
    linhas, colunas = df.shape          #desempacotamento de tupla, df.shape retorna uma tupla tipo (10, 4), e ao invés de guardar isso numa variável só, guardamos cada valor numa variável separada de uma vez 

    print (f"Planilha carregada: {linhas} linhas, {colunas} colunas")
    print (f"Colunas disponíveis: {','.join(df.columns)}")              #junta os nomes das colunas numa única string, separados por vírgula. Ex: ["Produto", "Categoria"] vira "Produto, Categoria"         

def pedir_coluna_numerica(df):
    while True:
        coluna = input ("Digite o nome da coluna para analisar: ").strip()

        if coluna not in df.columns:        #verifica se o nome digitado existe entre as colunas da planilha
            print (f"Coluna {coluna} não encontrada. Tente novamente.")
            continue

        if not pd.api.types.is_numeric_dtype(df[coluna]):           #função do pandas que verifica se uma coluna contém números (não texto).
            print (f"A coluna {coluna} não é numérica. Escolha outra.")
            continue

        return coluna

def calcular_estatisticas(df, coluna):
    return {
        "soma": df[coluna].sum(),
        "media": df[coluna].mean(),
        "minimo": df[coluna].min(),
        "maximo": df[coluna].max(),
    }

def salvar_relatorio(caminho_arquivo, coluna, estatisticas):
    pasta = os.path.dirname(caminho_arquivo)            #pega só a pasta de um caminho de arquivo completo.
    caminho_saida = os.path.join(pasta, "relatorio.txt")

    with open (caminho_saida, "w", encoding="utf-8") as arquivo:            #esse é o jeito padrão do Python de abrir e escrever arquivos. O with garante que o arquivo seja fechado automaticamente no final (mesmo se der erro no meio), sem precisar lembrar de chamar arquivo.close() manualmente. "w" significa "write" (modo escrita, sobrescreve o arquivo se já existir)
        arquivo.write(f"Relatório da coluna: {coluna}\n")
        arquivo.write(f"Soma: {estatisticas['soma']:.2f}\n")
        arquivo.write(f"Média: {estatisticas['media']:.2f}\n")
        arquivo.write(f"Mínimo: {estatisticas['minimo']:.2f}\n")
        arquivo.write(f"Máximo: {estatisticas['maximo']:.2f}\n")

    return caminho_saida

def executar():
    caminho_arquivo = pedir_arquivo_valido()

    df = ler_planilha(caminho_arquivo)

    if df is None:
        print ("Formato de arquivo não suportado. Use .csv ou .xlsx")
        return

    mostrar_resumo(df)
    coluna = pedir_coluna_numerica(df)
    estatisticas = calcular_estatisticas(df, coluna)

    print (f"Soma: {estatisticas['soma']:.2f}")
    print (f"Média: {estatisticas['media']:.2f}")
    print (f"Mínimo: {estatisticas['minimo']:.2f}")
    print (f"Máximo: {estatisticas['maximo']:.2f}")

    caminho_saida= salvar_relatorio(caminho_arquivo, coluna, estatisticas)
    print (f"Relatório salvo em: {caminho_saida}")