import customtkinter as ctk
from livro import Livro
from banco import BancoDeDados

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Sistema de Gerenciamento de Livros")
        self.geometry("800x500") # Aumentei um pouco a tela para caber a busca confortavelmente
        self.resizable(False, False)

        self.db = BancoDeDados()
        self.protocol("WM_DELETE_WINDOW", self.fechar_sistema)

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
        # FRAME DIREITO: Busca e Exibição de Dados
        # ==========================================
        self.frame_direita = ctk.CTkFrame(self)
        self.frame_direita.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # --- NOVA ÁREA DE BUSCA ---
        self.frame_busca = ctk.CTkFrame(self.frame_direita, fg_color="transparent")
        self.frame_busca.pack(pady=10, padx=10, fill="x")

        self.entry_busca = ctk.CTkEntry(self.frame_busca, placeholder_text="Buscar por Título, Autor ou Assunto...")
        self.entry_busca.pack(side="left", expand=True, fill="x", padx=(0, 10))

        self.btn_buscar = ctk.CTkButton(self.frame_busca, text="Buscar", width=80, command=self.executar_busca)
        self.btn_buscar.pack(side="left")

        # --- BOTÃO E CAIXA DE TEXTO (Mantidos) ---
        self.btn_listar = ctk.CTkButton(self.frame_direita, text="Listar Todos os Livros", command=self.listar_livros)
        self.btn_listar.pack(pady=10)

        self.caixa_texto = ctk.CTkTextbox(self.frame_direita, font=("Consolas", 14))
        self.caixa_texto.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.imprimir_na_tela("Sistema conectado ao Banco de Dados. Pronto para uso.")

    # ==========================================
    # LÓGICA DO SISTEMA
    # ==========================================
    def cadastrar_livro(self):
        nome = self.entry_nome.get()
        assunto = self.entry_assunto.get()
        autor = self.entry_autor.get()
        status = self.entry_status.get()

        if not (nome and assunto and autor and status):
            self.imprimir_na_tela("ERRO: Todos os campos devem ser preenchidos!")
            return

        novo_livro = Livro(nome, assunto, autor, status)
        self.db.inserir_livro(novo_livro)

        self.entry_nome.delete(0, 'end')
        self.entry_assunto.delete(0, 'end')
        self.entry_autor.delete(0, 'end')
        self.entry_status.delete(0, 'end')

        self.imprimir_na_tela(f"Sucesso: O livro '{nome}' foi salvo no banco de dados!")
        self.listar_livros() # Atualiza a lista automaticamente após cadastrar

    def executar_busca(self):
        """Lógica executada ao clicar no botão 'Buscar'."""
        termo = self.entry_busca.get()
        
        if not termo:
            self.imprimir_na_tela("Por favor, digite algo na barra de busca.")
            return

        self.caixa_texto.delete("0.0", "end")
        
        # Chama a nova função do banco
        resultados = self.db.buscar_livro(termo)

        if not resultados:
            self.imprimir_na_tela(f"Nenhum livro encontrado contendo: '{termo}'")
            return

        self.caixa_texto.insert("end", f"--- RESULTADOS DA BUSCA: '{termo}' ---\n\n")
        self.renderizar_lista(resultados)

    def listar_livros(self):
        self.caixa_texto.delete("0.0", "end")
        livros_salvos = self.db.listar_todos()
        
        if not livros_salvos:
            self.imprimir_na_tela("Nenhum livro cadastrado no banco de dados.")
            return

        self.caixa_texto.insert("end", "--- RELATÓRIO DE TODOS OS LIVROS ---\n\n")
        self.renderizar_lista(livros_salvos)

    def renderizar_lista(self, dados):
        """Função auxiliar para não repetir código de formatação."""
        for linha_db in dados:
            nome, assunto, autor, status = linha_db
            linha_formatada = f"Título: {nome}\nAutor: {autor} | Assunto: {assunto} | Status: {status}\n"
            linha_formatada += "-" * 40 + "\n"
            self.caixa_texto.insert("end", linha_formatada)

    def imprimir_na_tela(self, mensagem):
        self.caixa_texto.delete("0.0", "end")
        self.caixa_texto.insert("end", mensagem + "\n")

    def fechar_sistema(self):
        self.db.fechar_conexao()
        self.destroy()

if __name__ == "__main__":
    app = Aplicativo()
    app.mainloop()