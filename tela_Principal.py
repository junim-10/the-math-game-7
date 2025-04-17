import tkinter as tk
from tkinter import messagebox
from tela_Jogo import TelaJogo
from fim_jogo import FinalJogo
import time  # Import time aqui

def frameGenerico():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("The Math Game")
    root.resizable(False, False)

    root.continua_jogo = tk.BooleanVar(value=False)
    root.running = True
    root.pontos_jogo = 0
    root.acertos = 0
    root.partida_atual = 0
    root.start_time = 0

    def funcao_fechar():
        if messagebox.askyesno("Confirmação", "Você realmente deseja sair do jogo?"):
            root.running = False
            root.continua_jogo.set(True)
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", funcao_fechar)

    return root

def iniciar_jogo(root):
    root.start_time = time.time()
    root.pontos_jogo = 0
    root.acertos = 0
    root.partida_atual = 1
    tela_jogo = TelaJogo(root)
    exibir_proxima_partida(root, tela_jogo)

def exibir_proxima_partida(root, tela_jogo):
    if root.running and root.partida_atual <= 20:
        tela_jogo.frameTelaJogo(root, root.partida_atual, root.pontos_jogo)
        root.continua_jogo.set(False)
        root.wait_variable(root.continua_jogo)
        if root.running:
            root.partida_atual += 1
            exibir_proxima_partida(root, tela_jogo)
    elif root.running:
        final_jogo = FinalJogo(root, root.pontos_jogo, root.acertos, root.partida_atual - 1)
        final_jogo.frameFimJogo()

if __name__ == "__main__":
    root = frameGenerico()
    from tela_Abertura import TelaInicial
    tela_inicial = TelaInicial(root, iniciar_jogo) # Passa iniciar_jogo
    tela_inicial.frameTelaInicial()

    try:
        root.mainloop()
    except Exception as e:
        print(f"Erro durante a execução: {e}")