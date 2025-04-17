import tkinter as tk
from utilitarios import resetaTela

class TelaInstrucoes:
    def __init__(self, root):
        self.root = root
        resetaTela(self.root)
        self.root.title("Instruções - The Math Game")

    def frameTelaInstrucoes(self, iniciar_jogo_callback=None):
        titulo = tk.Label(self.root, text="Instruções do Jogo", font=("Arial", 24))
        titulo.pack(pady=30)

        instrucoes_texto = """
        Bem-vindo ao The Math Game!

        O objetivo do jogo é identificar a operação matemática (+, -, x, ÷)
        que resulta no valor exibido.

        Você verá dois números e o resultado da operação entre eles,
        com o operador escondido por um '?'.

        Selecione o botão da operação correta para ganhar pontos.
        Respostas mais rápidas podem render pontos extras!

        O jogo tem um total de 20 partidas. Ao final, sua pontuação
        e número de acertos serão exibidos.

        Clique no botão 'Jogar' para começar.
        """
        instrucoes_label = tk.Label(self.root, text=instrucoes_texto, font=("Arial", 12), justify="left", padx=20)
        instrucoes_label.pack(pady=20)

        botao_jogar = tk.Button(
            self.root,
            text="Jogar",
            command=lambda: iniciar_jogo_callback(self.root) if iniciar_jogo_callback else self.voltarParaMenu,
            font=("Arial", 16),
            width=15,
            height=2
        )
        botao_jogar.pack(pady=20)

        botao_voltar = tk.Button(
            self.root,
            text="Voltar para o Menu",
            command=self.voltarParaMenu,
            font=("Arial", 16),
            width=15,
            height=2
        )
        botao_voltar.pack(pady=10)

        rodape = tk.Label(
            self.root,
            text="Desenvolvido por: kelvin de Jesus ,Wendel Rafael e Marcos Alves (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

    def voltarParaMenu(self):
        from tela_Abertura import TelaInicial
        TelaInicial(self.root).frameTelaInicial()