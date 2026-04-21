from interface import Aplicativo

def rodar_teste_robo():
    # 1. Abre a interface real do seu programa
    app = Aplicativo()

    # 2. Cria o roteiro do que o "robô" vai fazer na tela
    def simular_acoes_usuario():
        print("[Robô] Janela aberta! Iniciando preenchimento dos campos...")

        # Preenche os campos de texto automaticamente
        app.entry_nome.insert(0, "O Programador Pragmático")
        app.entry_assunto.insert(0, "Engenharia de Software")
        app.entry_autor.insert(0, "Andrew Hunt")
        app.entry_status.insert(0, "Disponível")

        print("[Robô] Dados inseridos. Clicando em 'Cadastrar'...")
        # Aciona a mesma função que o botão "Cadastrar" acionaria
        app.cadastrar_livro()

        print("[Robô] Clicando em 'Listar Todos os Livros'...")
        # Aciona a função do botão de listar
        app.listar_livros()

        print("[Robô] Teste concluído com sucesso. Fechando o sistema em 4 segundos...")
        # Agenda o fechamento do sistema para 4000 milissegundos (4 segundos) no futuro
        app.after(4000, app.fechar_sistema)

    # 3. O 'after' diz para a janela: "Abra e espere 1.5 segundos (1500ms) para rodar o robô"
    app.after(1500, simular_acoes_usuario)

    # 4. Inicia a janela gráfica na tela
    app.mainloop()

if __name__ == "__main__":
    print("--- INICIANDO TESTE AUTOMATIZADO DA INTERFACE ---")
    rodar_teste_robo()