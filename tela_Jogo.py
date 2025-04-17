import tkinter as tk
import time
from tkinter import messagebox
from utilitarios import resetaTela
from logica_Jogo import DadosFuncionais

class TelaJogo:
    def __init__(self, root):
        self.root = root
        self.operador_correto = None
        self.num1 = None
        self.num2 = None
        self.resultado = None

        self.tempo_label = None
        self.timer_id = None
        self.paused = False
        self.start_time_questao = 0

    def frameTelaJogo(self, root, partida_atual, pontos):
        resetaTela(root)
        self.root.title("The Math Game")
        self.root.pontos_jogo = pontos  # Use um atributo específico para os pontos do jogo
        self.start_time_questao = time.time()

        cabecalho = tk.Frame(root)
        cabecalho.pack(pady=10)

        tk.Label(cabecalho, text="Partida:").grid(row=0, column=0, padx=10)
        tk.Label(cabecalho, text=f"{partida_atual}/20").grid(row=0, column=1, padx=10)

        tk.Label(cabecalho, text="Pontuação:").grid(row=0, column=2, padx=10)
        tk.Label(cabecalho, text=str(self.root.pontos_jogo)).grid(row=0, column=3, padx=10)

        tk.Label(cabecalho, text="Tempo:").grid(row=0, column=4, padx=10)
        self.tempo_label = tk.Label(cabecalho, text="00:00")
        self.tempo_label.grid(row=0, column=5, padx=10)

        self.num1, self.num2 = DadosFuncionais.gerarNumeros()
        self.operador_correto = DadosFuncionais.selecionarOperador()
        self.resultado = DadosFuncionais.calcularResultado(self.num1, self.num2, self.operador_correto)

        numeros_frame = tk.Frame(root)
        numeros_frame.pack(pady=40)
        tk.Label(numeros_frame, text=str(self.num1), font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numeros_frame, text="?", font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numeros_frame, text=str(self.num2), font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numeros_frame, text="=", font=("Arial", 32)).pack(side="left", padx=10)
        tk.Label(numeros_frame, text=str(self.resultado), font=("Arial", 32)).pack(side="left", padx=10)

        operacoes_frame = tk.Frame(root)
        operacoes_frame.pack(pady=30)

        operadores_mapeados = {"+": "+", "-": "-", "x": "*", "÷": "/"}

        for texto_botao, operador_real in operadores_mapeados.items():
            botao = tk.Button(
                operacoes_frame,
                text=texto_botao,
                font=("Arial", 16),
                width=5,
                height=2,
                command=lambda op=operador_real: self.processarResposta(op)
            )
            botao.pack(side="left", padx=10)

        rodape = tk.Label(
            root,
            text="Desenvolvido por: \nJoão Silva e Maria Souza (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

        self.atualizarTempo()

    def atualizarTempo(self):
        if not hasattr(self.root, 'running') or not self.root.running or self.paused:
            return
        elapsed = int(time.time() - self.root.start_time)
        minutos = elapsed // 60
        segundos = elapsed % 60
        self.tempo_label.config(text=f"{minutos:02d}:{segundos:02d}")
        self.timer_id = self.root.after(1000, self.atualizarTempo)

    def processarResposta(self, resposta):
        if not hasattr(self.root, 'pontos_jogo'):
            self.root.pontos_jogo = 0
        if not hasattr(self.root, 'acertos'):
            self.root.acertos = 0

        tempo_decorrido_questao = time.time() - self.start_time_questao
        if resposta == self.operador_correto:
            if tempo_decorrido_questao < 20:
                self.root.pontos_jogo += 10  # Aumentei a pontuação para ficar mais claro
            else:
                self.root.pontos_jogo += 1
            self.root.acertos += 1

        self.root.continua_jogo.set(True)

    def pararJogo(self):
        self.root.running = False
        self.root.continua_jogo.set(True)