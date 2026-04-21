import unittest
import os
from livro import Livro
from banco import BancoDeDados

class TestLivro(unittest.TestCase):
    """Bateria de testes unitários para a classe Livro (Molde)."""

    def setUp(self):
        """Prepara um objeto Livro antes de cada teste."""
        self.livro_teste = Livro(
            nome_livro="Python Fluente", 
            assunto_livro="Programação", 
            autor_livro="Luciano Ramalho", 
            status_livro="Disponível"
        )

    def test_inicializacao_livro(self):
        """Verifica se os atributos estão sendo encapsulados corretamente."""
        self.assertEqual(self.livro_teste.nome, "Python Fluente")
        self.assertEqual(self.livro_teste.assunto, "Programação")
        self.assertEqual(self.livro_teste.autor, "Luciano Ramalho")
        self.assertEqual(self.livro_teste.status, "Disponível")


class TestBancoDeDados(unittest.TestCase):
    """Bateria de testes de integração para o SQLite."""

    def setUp(self):
        """
        Gera um arquivo de banco de dados EXCLUSIVO para testes.
        Isso impede que o teste apague ou suje os dados do seu sistema real.
        """
        self.nome_banco_teste = "banco_teste_automatizado.db"
        self.db = BancoDeDados(nome_arquivo=self.nome_banco_teste)

    def tearDown(self):
        """
        Executado APÓS cada teste. 
        Fecha a conexão e deleta o arquivo de teste para manter a pasta limpa.
        """
        self.db.fechar_conexao()
        if os.path.exists(self.nome_banco_teste):
            os.remove(self.nome_banco_teste)

    def test_inserir_e_listar_livros(self):
        """Testa o fluxo completo: salva um dado no arquivo e tenta ler de volta."""
        
        # 1. Preparação (Cria o objeto)
        livro_novo = Livro("Arquitetura Limpa", "Engenharia", "Robert Martin", "Disponível")
        
        # 2. Ação (Insere no banco de teste)
        self.db.inserir_livro(livro_novo)
        
        # 3. Verificação (Busca no banco e checa se o que voltou é o que foi enviado)
        resultados = self.db.listar_todos()
        
        # O banco retorna uma lista de tuplas. Ex: [('Arquitetura Limpa', 'Engenharia', 'Robert Martin', 'Disponível')]
        self.assertEqual(len(resultados), 1) # Garante que apenas 1 livro foi salvo
        
        # Extrai a primeira tupla da lista
        livro_salvo = resultados[0] 
        
        # Compara as colunas retornadas com os dados originais
        self.assertEqual(livro_salvo[0], "Arquitetura Limpa")
        self.assertEqual(livro_salvo[1], "Engenharia")
        self.assertEqual(livro_salvo[2], "Robert Martin")
        self.assertEqual(livro_salvo[3], "Disponível")


if __name__ == "__main__":
    unittest.main()