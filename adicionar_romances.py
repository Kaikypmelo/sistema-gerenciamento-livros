from banco import BancoDeDados
from livro import Livro

def popular_romances():
    db = BancoDeDados()
    
    livros_romance = [
        Livro("Orgulho e Preconceito", "Romance de Época", "Jane Austen", "Disponível"),
        Livro("É Assim Que Acaba", "Drama Romântico", "Colleen Hoover", "Emprestado"),
        Livro("Teto Para Dois", "Comédia Romântica", "Beth O'Leary", "Disponível"),
        Livro("Os Sete Maridos de Evelyn Hugo", "Romance Histórico", "Taylor Jenkins Reid", "Emprestado"),
        Livro("A Culpa é das Estrelas", "Romance Jovem Adulto", "John Green", "Disponível")
    ]

    print("Iniciando inserção da nova categoria...")
    for livro in livros_romance:
        db.inserir_livro(livro)
        print(f"Inserido: {livro.nome}")
    
    db.fechar_conexao()
    print("\nLivros de romance adicionados com sucesso ao banco!")

if __name__ == "__main__":
    popular_romances()