from banco import BancoDeDados
from livro import Livro

def popular():
    db = BancoDeDados()
    
    livros = [
        Livro("Python Fluente", "Programação", "Luciano Ramalho", "Disponível"),
        Livro("Arquitetura Limpa", "Arquitetura de Software", "Robert C. Martin", "Emprestado"),
        Livro("Testes de Invasão: Uma Introdução Prática", "Segurança da Informação", "Georgia Weidman", "Disponível"),
        Livro("DAMA-DMBOK", "Governança de Dados", "DAMA International", "Disponível"),
        Livro("Manual de DevOps", "Infraestrutura e Operações", "Gene Kim", "Emprestado")
    ]

    print("Iniciando inserção de dados...")
    for livro in livros:
        db.inserir_livro(livro)
        print(f"Inserido: {livro.nome}")
    
    db.fechar_conexao()
    print("\nBanco de dados populado com sucesso!")

if __name__ == "__main__":
    popular()