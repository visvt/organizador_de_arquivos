# 🛠️ Automatizador de Tarefas em CLI

Ferramenta de linha de comando para automatizar tarefas repetitivas do dia a dia, escrita em Python.

Feita como um mini "canivete suíço" com três ferramentas em um só menu:

- ✅ **Organizador de Arquivos** — organiza arquivos de uma pasta em subpastas por tipo (Imagens, Documentos, Planilhas, etc.)
- ✅ **Renomeador em Lote** — renomeia múltiplos arquivos de uma vez, por número sequencial ou por busca e substituição de texto
- ✅ **Gerador de Relatório** — lê uma planilha (`.csv` ou `.xlsx`) e gera um resumo estatístico de uma coluna numérica

## 📸 Demonstração

```
===== AUTOMATIZADOR DE TAREFAS =====
1 - Organizador de Arquivos
2 - Renomeador em Lote
3 - Gerador de Relatório
0 - Sair
Escolha uma opção: 1
Digite o caminho da pasta a organizar: ~/Downloads
✅ foto1.jpg → Imagens/
✅ documento.pdf → Documentos/
✅ planilha.xlsx → Planilhas/

🎉 Organização concluída!
```

## 📦 Requisitos

- Python 3.10 ou superior (usa `match`/`case`, disponível a partir dessa versão)
- `pandas` e `openpyxl`, usados apenas pelo Gerador de Relatório (veja instalação abaixo)

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/visvt/organizador_cli.git
cd organizador_cli
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/Scripts/activate    # Windows (Git Bash)
# ou: source venv/bin/activate  # Linux/Mac
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Rode o menu principal

```bash
python main.py
```

Escolha uma opção no menu e siga as instruções no terminal.

### Organizador de Arquivos

Ao escolher a opção `1`, informe o caminho de uma pasta. A ferramenta:

1. Lê todos os arquivos da pasta informada
2. Identifica a extensão de cada arquivo
3. Move cada arquivo para uma subpasta correspondente à sua categoria (Imagens, Documentos, Planilhas, Vídeos, Áudios, Compactados)
4. Para extensões desconhecidas, pergunta ao usuário o nome da categoria (ou permite pular)

### Renomeador em Lote

Ao escolher a opção `2`, informe o caminho de uma pasta e o modo desejado:

- **Prefixo + número sequencial** — renomeia todos os arquivos com um prefixo escolhido, seguido de um número sequencial com zeros à esquerda (ex: `foto_001.jpg`, `foto_002.jpg`)
- **Busca e substituição de texto** — substitui um trecho específico do nome dos arquivos por outro (ex: trocar `"IMG"` por `"ferias"`)

### Gerador de Relatório

Ao escolher a opção `3`, informe o caminho de uma planilha `.csv` ou `.xlsx`. A ferramenta:

1. Carrega a planilha e mostra um resumo (número de linhas, colunas disponíveis)
2. Pergunta qual coluna numérica analisar
3. Calcula soma, média, mínimo e máximo dessa coluna
4. Salva o resultado em um arquivo `relatorio.txt`, na mesma pasta da planilha original

## 📁 Estrutura do projeto

```
organizador_cli/
├── main.py                 # Menu principal (match/case)
├── ferramentas/
│   ├── __init__.py
│   ├── utils.py             # Funções compartilhadas (validação de pasta e arquivo)
│   ├── organizador.py      # Organizador de Arquivos
│   ├── renomeador.py       # Renomeador em Lote
│   └── relatorio.py        # Gerador de Relatório
├── requirements.txt
├── README.md
└── .gitignore
```

## 🗺️ Roadmap

- [x] Menu principal com `match`/`case`
- [x] Organizador de Arquivos
- [x] Validação de pasta com loop de repetição em caso de caminho inválido
- [x] Renomeador em Lote (modo sequencial e modo busca/substituição)
- [x] Gerador de Relatório a partir de planilha, com pandas
- [x] Funções compartilhadas centralizadas em `utils.py`
- [ ] Modo simulação (`--dry-run`) para pré-visualizar mudanças sem executá-las
- [ ] Testes automatizados

## 🧠 O que este projeto demonstra

- Organização de código em módulos (separação de responsabilidades)
- Reaproveitamento de código entre ferramentas (`utils.py`)
- Uso de bibliotecas padrão do Python para manipulação de arquivos (`os`, `shutil`)
- Uso de biblioteca externa (`pandas`) para análise de dados tabulares
- Ambiente virtual (`venv`) e gerenciamento de dependências via `requirements.txt`
- Tratamento de erros e validação de entrada do usuário
- Estrutura de projeto escalável, pronta para novas ferramentas

## 📄 Licença

Este projeto está sob a licença MIT.