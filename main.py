from livro import Livro

def exibir_menu():
    """Exibe as opções do menu interativo."""
    print("\n--- SISTEMA DE GERENCIAMENTO DE LIVROS ---")
    print("1. Cadastrar Livro")
    print("2. Listar Livros")
    print("3. Buscar Livro (Nome/Assunto/Autor)")
    print("4. Sair")
    return input("Escolha uma opção: ")

def main():
    # Coleção para armazenar as instâncias dos objetos
    biblioteca = []

    while True:
        opcao = exibir_menu()

        if opcao == '1':
            # Cadastrar: Solicita dados e instancia o objeto
            print("\n-- Cadastro de Novo Livro --")
            nome = input("Nome do Livro: ")
            assunto = input("Assunto: ")
            autor = input("Autor: ")
            status = input("Status (Disponível/Emprestado): ")
            
            novo_livro = Livro(nome, assunto, autor, status)
            biblioteca.append(novo_livro)
            print(f"Livro '{nome}' cadastrado com sucesso!")

        elif opcao == '2':
            # Listar: Usa laço for para percorrer a lista
            print("\n-- Relatório de Livros Cadastrados --")
            if not biblioteca:
                print("A biblioteca está vazia.")
            else:
                for livro in biblioteca:
                    livro.exibir_detalhes()

        elif opcao == '3':
            # Buscar: Localiza o item por múltiplos atributos
            print("\n-- Busca de Itens --")
            termo = input("Digite o nome, assunto ou autor para buscar: ").lower()
            encontrado = False
            
            for livro in biblioteca:
                # Lógica de busca insensível a maiúsculas/minúsculas
                if (termo in livro.nome.lower() or 
                    termo in livro.assunto.lower() or 
                    termo in livro.autor.lower()):
                    livro.exibir_detalhes()
                    encontrado = True
            
            if not encontrado:
                print(f"Nenhum livro encontrado para o termo: '{termo}'")

        elif opcao == '4':
            # Sair: Encerra a execução
            print("Encerrando o sistema. Bons estudos!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()