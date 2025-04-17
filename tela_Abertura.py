import tkinter as tk
from tela_Instrucoes import TelaInstrucoes
from utilitarios import resetaTela

class TelaInicial:
    def __init__(self, root, iniciar_jogo_callback=None):
        self.root = root
        self.iniciar_jogo_callback = iniciar_jogo_callback
        resetaTela(self.root)
        self.root.title("The Math Game")

    def frameTelaInicial(self):

        titulo = tk.Label(self.root, text="Bem-vindo ao \nThe Math Game!", font=("Arial", 24))
        titulo.pack(pady=50)

        botao_play = tk.Button(
            self.root,
            text="Play",
            command=self.irParaInstrucoesParaJogar,
            font=("Arial", 16),
            width=10,
            height=2
        )
        botao_play.pack(pady=20) # Aumentei o pady já que não há outro botão

        rodape = tk.Label(
            self.root,
            text="Desenvolvido por: kelvin de Jesus ,Wendel Rafael e Marcos Alves (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

    def irParaInstrucoesParaJogar(self):
        TelaInstrucoes(self.root).frameTelaInstrucoes(self.iniciar_jogo_callback)