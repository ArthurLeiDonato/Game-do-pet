import tkinter as tk
import random
#janela
janela = tk.Tk()
janela.geometry("350x550")
janela.title("Sistema de Status")


fome = 0
banheiro = 100
alegria = 100
def atualizar_tela():
    lbl_fome.config(text=f"Fome: {fome}%")
    lbl_banheiro.config(text=f"Banheiro: {banheiro}%")
    lbl_alegria.config(text=f"Alegria:{alegria}%")

def passar_tempo():
    global fome, banheiro, alegria
    fome += 3
    if fome > 100: fome = 100
        
    atualizar_tela()
    banheiro -= 10
    if banheiro < 0: banheiro = 0

    alegria -= 9
    if alegria < 0: alegria = 0
    janela.after(2000, passar_tempo)    # Roda de novo a cada 2 segundos
def alimentar():
    global fome
    fome -= 3
    if fome < 0: fome = 0
    if fome > 100: fome = 100
    atualizar_tela() 
    lbl_mensagem.config(text="Nhac! Que delícia! 🍖", fg="yellow")
def mijar():
    global banheiro
    banheiro += 7
    if banheiro > 100: banheiro = 100
    atualizar_tela()
    lbl_mensagem.config(text="Bem melhor!", fg="green") 

def brincar():
    global alegria
    alegria += 10
    if alegria > 100: alegria = 100
    atualizar_tela()
    mensagens_alegria = ["Eeeeba!", "estou muito feliz", "Hahaha"]
    lbl_mensagem.config(text=random.choice(mensagens_alegria), fg="green")

# 4. Elementos Visuais (Interface)
lbl_mensagem = tk.Label(janela, text="Olá!", font=("Arial", 14, "italic"), fg="blue")
lbl_mensagem.pack(pady=20)


lbl_fome = tk.Label(janela, text="Fome: 100%", font=("Arial", 16, "bold"))
lbl_fome.pack(pady=20)
btn_alimentar = tk.Button(janela, text="🍖 Dar Comida", font=("Arial", 12), command=alimentar,fg="orange")
btn_alimentar.pack()

lbl_banheiro = tk.Label(janela, text="Banheiro: 100%", font=("Arial", 16, "bold"))
lbl_banheiro.pack(pady=20)
btn_mijar = tk.Button(janela, text="mijar", font=("Arial", 12), command=mijar)
btn_mijar.pack()

lbl_alegria = tk.Label(janela, text="Alegria: 100%", font=("Arial", 16, "bold"))
lbl_alegria.pack(pady=20)
btn_brincar = tk.Button(janela, text="Brincar", font=("Arial", 12), command=brincar)
btn_brincar.pack()

# 5. Iniciar o Relógio do Jogo e a Janela
passar_tempo() # Liga o temporizador da fome
janela.mainloop()
atualizar_tela()
