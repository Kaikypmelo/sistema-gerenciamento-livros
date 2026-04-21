import customtkinter as ctk
from livro import Livro

# Configuração visual padrão (Dark mode e tema azul)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Aplicativo(ctk.CTk):
    """Classe principal que constrói a janela do sistema."""
    
    def __init__(self):
        super().__init__()
        
        # Configurações da Janela
        self.title("Sistema de Gerenciamento de Livros")
        self.geometry("750x450")
        self.resizable(False, False)

        # Nossa coleção de objetos
        self.biblioteca = []

        # ==========================================
        # FRAME ESQUERDO: Formulário de Cadastro
        # ==========================================
        self.frame_cadastro = ctk.CTkFrame(self, width=250)
        self.frame_cadastro.pack(side="left", fill="y", padx=10, pady=10)

        ctk.CTkLabel(self.frame_cadastro, text="Novo Livro", font=("Arial", 20, "bold")).pack(pady=20)

        self.entry_nome = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Nome do Livro", width=200)
        self.entry_nome.pack(pady=10)

        self.entry_assunto = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Assunto", width=200)
        self.entry_assunto.pack(pady=10)

        self.entry_autor = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Autor", width=200)
        self.entry_autor.pack(pady=10)

        self.entry_status = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Status (ex: Disponível)", width=200)
        self.entry_status.pack(pady=10)

        self.btn_cadastrar = ctk.CTkButton(self.frame_cadastro, text="Cadastrar", command=self.cadastrar_livro)
        self.btn_cadastrar.pack(pady=20)

        # ==========================================
        # FRAME DIREITO: Exibição de Dados
        # ==========================================
        self.frame_lista = ctk.CTkFrame(self)
        self.frame_lista.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.btn_listar = ctk.CTkButton(self.frame_lista, text="Listar Todos os Livros", command=self.listar_livros)
        self.btn_listar.pack(pady=10)

        # Caixa de texto onde os relatórios vão aparecer
        self.caixa_texto = ctk.CTkTextbox(self.frame_lista, font=("Consolas", 14))
        self.caixa_texto.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Mensagem de boas-vindas
        self.imprimir_na_tela("Bem-vindo! Cadastre um livro ou clique em 'Listar Todos'.")

    # ==========================================
    # LÓGICA DO SISTEMA
    # ==========================================
    def cadastrar_livro(self):
        """Captura os dados, cria o objeto e salva na lista."""
        nome = self.entry_nome.get()
        assunto = self.entry_assunto.get()
        autor = self.entry_autor.get()
        status = self.entry_status.get()

        # Validação simples
        if not (nome and assunto and autor and status):
            self.imprimir_na_tela("ERRO: Todos os campos devem ser preenchidos!")
            return

        # Instancia o objeto Livro e adiciona à biblioteca
        novo_livro = Livro(nome, assunto, autor, status)
        self.biblioteca.append(novo_livro)

        # Limpa os campos visuais após o cadastro
        self.entry_nome.delete(0, 'end')
        self.entry_assunto.delete(0, 'end')
        self.entry_autor.delete(0, 'end')
        self.entry_status.delete(0, 'end')

        self.imprimir_na_tela(f"Sucesso: O livro '{nome}' foi cadastrado!")

    def listar_livros(self):
        """Percorre a lista e exibe os livros na tela."""
        self.caixa_texto.delete("0.0", "end") # Limpa a tela antes de listar
        
        if not self.biblioteca:
            self.imprimir_na_tela("A biblioteca está vazia no momento.")
            return

        self.caixa_texto.insert("end", "--- RELATÓRIO DE LIVROS ---\n\n")
        for livro in self.biblioteca:
            # Formatação usando os dados do objeto
            linha = f"Título: {livro.nome}\nAutor: {livro.autor} | Assunto: {livro.assunto} | Status: {livro.status}\n"
            linha += "-" * 40 + "\n"
            self.caixa_texto.insert("end", linha)

    def imprimir_na_tela(self, mensagem):
        """Função auxiliar para escrever no quadro de texto."""
        self.caixa_texto.delete("0.0", "end")
        self.caixa_texto.insert("end", mensagem + "\n")

# Executa o aplicativo
if __name__ == "__main__":
    app = Aplicativo()
    app.mainloop()