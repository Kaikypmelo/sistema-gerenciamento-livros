class Livro:
    def __init__(self, nome_livro, assunto_livro, autor_livro, status_livro):
        """Inicializa os atributos do objeto Livro."""
        self.nome = nome_livro
        self.assunto = assunto_livro
        self.autor = autor_livro
        self.status = status_livro
    def exibir_detalhes(self):
        print(f"Livro: {self.nome:.<20} | Autor: {self.autor:.<15} | "
              f"Assunto: {self.assunto:.<15} | Status: {self.status}")