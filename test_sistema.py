import unittest
from unittest.mock import patch
from io import StringIO
from livro import Livro
from main import exibir_menu

class TestLivro(unittest.TestCase):
    """Bateria de testes para a classe Livro."""

    def setUp(self):
        """Método executado antes de cada teste para preparar o ambiente."""
        self.livro_teste = Livro(
            nome_livro="Python Fluente", 
            assunto_livro="Programação", 
            autor_livro="Luciano Ramalho", 
            status_livro="Disponível"
        )

    def test_inicializacao_livro(self):
        """Testa se o construtor (__init__) salva os atributos corretamente."""
        self.assertEqual(self.livro_teste.nome, "Python Fluente")
        self.assertEqual(self.livro_teste.assunto, "Programação")
        self.assertEqual(self.livro_teste.autor, "Luciano Ramalho")
        self.assertEqual(self.livro_teste.status, "Disponível")

    @patch('sys.stdout', new_callable=StringIO)
    def test_exibir_detalhes(self, mock_stdout):
        """Testa se o método exibir_detalhes formata e imprime os dados certos."""
        # Chama o método que gera o print
        self.livro_teste.exibir_detalhes()
        
        # Captura o que seria impresso na tela
        saida_impressa = mock_stdout.getvalue()
        
        # Verifica se as palavras-chave estão dentro da string impressa
        self.assertIn("Python Fluente", saida_impressa)
        self.assertIn("Luciano Ramalho", saida_impressa)
        self.assertIn("Disponível", saida_impressa)


class TestMain(unittest.TestCase):
    """Bateria de testes para as funções do arquivo principal."""

    @patch('builtins.input', return_value='2')
    def test_exibir_menu(self, mock_input):
        """
        Testa o menu interativo. 
        O @patch simula que o usuário digitou '2' e deu Enter.
        """
        opcao_escolhida = exibir_menu()
        self.assertEqual(opcao_escolhida, '2')

if __name__ == "__main__":
    unittest.main()