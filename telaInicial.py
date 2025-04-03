import tkinter as tk 
class TelaInicial: 
  def _init_(self, window):
   self.janela= window 

def constroiLayout(self): 

#titulo que vai aparecer grande na tela (tk.Label) 
#botão de play (tk.Button) 
    rodape = tk.Label( 
        self.janela, 
        text="Desenvolvido por: João Silva e Maria Souza (Senai Betim 202 5)", 
font=("Arial", 8) 
     ) 
    rodape.pack(side="bottom", pady=10) 

    self.janela.mainloop()