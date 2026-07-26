from ferramentas import organizador, renomeador, relatorio # Aqui estou importando as ferramentas.

def menu():
    print ("*~*= AUTOMATIZADOR DE TAREFAS =*~*")
    print ("1 - Organizador de Arquivos")
    print ("2 - Renomeador em Lote")
    print ("3 - Gerador de Relatório")
    print ("0 - Sair")
    return input ("Escolha uma opção: ")

def main():
    while True:
        escolha = menu()

        match escolha:
            case "1":
                organizador.executar()

            case "2":
                renomeador.executar()

            case "3":
                relatorio.executar()

            case "0":
                print ("Até logo!")
                break

            case _:
                print ("Opção inválida, tente novamente.")

if __name__ == "__main__": #isso garante que main() só roda quando você executa o arquivo diretamente (não quando ele é importado por outro arquivo). É um padrão que você vai ver em praticamente todo projeto Python sério.
    main()