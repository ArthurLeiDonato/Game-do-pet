import tkinter as tk

#janela
janela = tk.Tk()
janela.geometry("300x200")
janela.title("Sistema de Status")


fome = 100
banheiro = 100


def atualizar_tela():
    lbl_fome.config(text=f"Fome: {fome}%")
    lbl_banheiro.config(text=f"Banheiro: {banheiro}%")

def passar_tempo():
    global fome
    fome -= 3
    if fome < 0:
        fome = 0
    atualizar_tela()
    janela.after(9000, passar_tempo) # Roda de novo a cada 2 segundos
    global banheiro
    banheiro -= 10
    if banheiro < 0:
        banheiro = 0

def alimentar():
    global fome
    fome += 20
    if fome > 100:
        fome = 100
    atualizar_tela() 

def mijar():
    global banheiro
    banheiro += 7
    if banheiro > 100:
        banheiro = 100 
    atualizar_tela()

# 4. Elementos Visuais (Interface)
lbl_fome = tk.Label(janela, text="Fome: 100%", font=("Arial", 16, "bold"))
lbl_fome.pack(pady=20)

btn_alimentar = tk.Button(janela, text="🍖 Dar Comida", font=("Arial", 12), command=alimentar)
btn_alimentar.pack()

lbl_banheiro = tk.Label(janela, text="Banheiro: 100%", font=("Arial", 16, "bold"))
lbl_banheiro.pack(pady=20)

btn_mijar = tk.Button(janela, text="mijar", font=("Arial", 12), command=mijar)
btn_mijar.pack()

# 5. Iniciar o Relógio do Jogo e a Janela
passar_tempo() # Liga o temporizador da fome
janela.mainloop()
