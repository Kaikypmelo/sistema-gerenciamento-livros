import sqlite3
import os
import sys

class BancoDeDados:
    def __init__(self, nome_arquivo="biblioteca.db"):
        """Conecta ao arquivo do banco garantindo o caminho correto no .exe"""
        
        # Lógica para descobrir a pasta real do programa
        if getattr(sys, 'frozen', False):
            # Se estiver rodando pelo .exe criado pelo PyInstaller
            pasta_base = os.path.dirname(sys.executable)
        else:
            # Se estiver rodando pelo VS Code/Terminal (.py normal)
            pasta_base = os.path.dirname(os.path.abspath(__file__))

        # Junta a pasta real com o nome do arquivo de banco
        caminho_banco = os.path.join(pasta_base, nome_arquivo)

        self.conexao = sqlite3.connect(caminho_banco)
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                assunto TEXT,
                autor TEXT,
                status TEXT
            )
        ''')
        self.conexao.commit()

    def inserir_livro(self, livro):
        self.cursor.execute('''
            INSERT INTO livros (nome, assunto, autor, status)
            VALUES (?, ?, ?, ?)
        ''', (livro.nome, livro.assunto, livro.autor, livro.status))
        self.conexao.commit()

    def listar_todos(self):
        self.cursor.execute('SELECT nome, assunto, autor, status FROM livros')
        return self.cursor.fetchall()
    def buscar_livro(self, termo):
        """Busca no banco por nome, assunto ou autor usando LIKE."""
        # O % no SQL atua como um curinga (busca qualquer coisa antes ou depois do termo)
        termo_busca = f"%{termo}%" 
        
        self.cursor.execute('''
            SELECT nome, assunto, autor, status FROM livros
            WHERE nome LIKE ? OR assunto LIKE ? OR autor LIKE ?
        ''', (termo_busca, termo_busca, termo_busca))
        
        return self.cursor.fetchall()

    def fechar_conexao(self):
        self.conexao.close()