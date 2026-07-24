# 🛠️ Automatizador de Tarefas em CLI

Ferramenta de linha de comando para automatizar tarefas repetitivas do dia a dia, escrita em Python puro (bibliotecas padrão apenas — sem dependências externas).

Feita como um mini "canivete suíço" com três ferramentas em um só menu:

- ✅ **Organizador de Arquivos** — organiza arquivos de uma pasta em subpastas por tipo (Imagens, Documentos, Planilhas, etc.)
- 🚧 **Renomeador em Lote** — renomeia múltiplos arquivos seguindo um padrão *(em desenvolvimento)*
- 🚧 **Gerador de Relatório** — gera resumo a partir de uma planilha *(em desenvolvimento)*

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
- Nenhuma dependência externa — usa apenas bibliotecas padrão do Python (`os`, `shutil`)

## 🚀 Como usar

Clone o repositório e rode o menu principal:

```bash
git clone https://github.com/visvt/organizador_cli.git
cd organizador_cli
python main.py
```

Escolha uma opção no menu e siga as instruções no terminal.

### Organizador de Arquivos

Ao escolher a opção `1`, informe o caminho de uma pasta. A ferramenta:

1. Lê todos os arquivos da pasta informada
2. Identifica a extensão de cada arquivo
3. Move cada arquivo para uma subpasta correspondente à sua categoria (Imagens, Documentos, Planilhas, Vídeos, Áudios, Compactados)
4. Para extensões desconhecidas, pergunta ao usuário o nome da categoria (ou permite pular)

## 📁 Estrutura do projeto

```
organizador_cli/
├── main.py                 # Menu principal (match/case)
├── ferramentas/
│   ├── __init__.py
│   ├── organizador.py      # Organizador de Arquivos
│   ├── renomeador.py       # Renomeador em Lote (em desenvolvimento)
│   └── relatorio.py        # Gerador de Relatório (em desenvolvimento)
├── requirements.txt
├── README.md
└── .gitignore
```

## 🗺️ Roadmap

- [x] Menu principal com `match`/`case`
- [x] Organizador de Arquivos
- [x] Validação de pasta com loop de repetição em caso de caminho inválido
- [ ] Renomeador em Lote
- [ ] Gerador de Relatório a partir de planilha
- [ ] Modo simulação (`--dry-run`) para pré-visualizar mudanças sem executá-las

## 🧠 O que este projeto demonstra

- Organização de código em módulos (separação de responsabilidades)
- Uso de bibliotecas padrão do Python para manipulação de arquivos (`os`, `shutil`)
- Tratamento de erros e validação de entrada do usuário
- Estrutura de projeto escalável, pronta para novas ferramentas

## 📄 Licença

Este projeto está sob a licença MIT.