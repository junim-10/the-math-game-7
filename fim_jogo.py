import tkinter as tk
from utilitarios import resetaTela

class FinalJogo:
    def __init__(self, root, pontos=0, acertos=0, partidas=0):
        self.root = root
        self.pontos = pontos
        self.acertos = acertos
        self.partidas = partidas

    def frameFimJogo(self):
        resetaTela(self.root)
        self.root.title("Fim do jogo!")

        titulo = tk.Label(self.root, text="Fim do jogo!", font=("Arial", 24))
        titulo.pack(pady=50)

        texto = tk.Label(
            self.root,
            text=f"Parabéns pela partida!\n"
                 f"Você marcou {self.pontos} pontos e acertou {self.acertos} de {self.partidas} partidas!",
            font=("Arial", 14)
        )
        texto.pack(pady=10)

        botao_play = tk.Button(
            self.root,
            text="Jogar Novamente",
            command=self.reiniciarJogo, # Alterei para chamar a função de reiniciar
            font=("Arial", 16),
            width=15,
            height=2
        )
        botao_play.pack(pady=20)

        botao_sair = tk.Button(
            self.root,
            text="Sair do Jogo",
            command=self.sairJogo,
            font=("Arial", 16),
            width=15,
            height=2
        )
        botao_sair.pack(pady=10)

        rodape = tk.Label(
            self.root,
            text="Desenvolvido por: \nJoão Silva e Maria Souza (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

    def reiniciarJogo(self):
        # Resetar as variáveis de estado do jogo no root
        self.root.pontos_jogo = 0
        self.root.acertos = 0
        self.root.partida_atual = 0
        self.root.start_time = 0
        self.root.running = True
        self.root.continua_jogo.set(False)

        # Iniciar o jogo novamente
        from tela_Principal import iniciar_jogo
        iniciar_jogo(self.root)

    def sairJogo(self):
        self.root.running = False
        self.root.destroy()