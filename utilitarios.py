import tkinter as tk

def resetaTela(root):
    for widget in root.winfo_children():
        widget.destroy()
