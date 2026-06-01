import tkinter as tk
import random

#janela
janela = tk.Tk()
janela.geometry("350x550")
janela.title("Sistema de Status")
janela.configure(bg="#903bf0")

#logica

fome = 0
banheiro = 100
alegria = 100
jogo_iniciado = False

def iniciar_jogo():
    global jogo_iniciado
    frame_menu.pack_forget()    
    frame_jogo.pack(fill="both", expand=True)

    jogo_iniciado = True
    atualizar_tela()
    passar_tempo()

def voltar_ao_menu():
    global jogo_iniciado
    jogo_iniciado = False
    frame_jogo.pack_forget()
    frame_menu.pack(fill="both", expand=True)

def atualizar_tela():
    if jogo_iniciado:
        lbl_fome.config(text=f"Fome: {fome}%")
        lbl_banheiro.config(text=f"Banheiro: {banheiro}%")
        lbl_alegria.config(text=f"Alegria:{alegria}%")

def passar_tempo():
    global fome, banheiro, alegria

    if not jogo_iniciado:
        return
    
    fome += 3
    if fome > 100: fome = 100
        
    atualizar_tela()
    banheiro -= 10
    if banheiro < 0: banheiro = 0

    alegria -= 9
    if alegria < 0: alegria = 0
    atualizar_tela()
    janela.after(2000, passar_tempo)    # Roda de novo a cada 2 segundos

#ações 
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

#menu
frame_menu = tk.Frame(janela, bg="#e0ebeb")
frame_menu.pack(fill="both", expand=True)

lbl_menu_titulo = tk.Label(frame_menu, text="Kumo", font=("Arial", 24, "bold"), bg="#e0ebeb", fg="#4a4a4a")
lbl_menu_titulo.pack(pady=80)

btn_jogar = tk.Button(frame_menu, text="JOGAR", font=("Arial", 16, "bold"), command=iniciar_jogo, bg="#4CAF50", fg="white", width=12)
btn_jogar.pack(pady=20)

btn_sair = tk.Button(frame_menu, text="SAIR", font=("Arial", 12), command=janela.quit, bg="#f44336", fg="white", width=12)
btn_sair.pack(pady=10)

frame_jogo = tk.Frame(janela, bg="#f0f0f0")

#Interface
lbl_mensagem = tk.Label(frame_jogo, text="Olá!", font=("Arial", 14, "italic"), fg="blue")
lbl_mensagem.pack(pady=15)

#botões
lbl_fome = tk.Label(frame_jogo, text="Fome: 100%", font=("Arial", 16, "bold"))
lbl_fome.pack(pady=10)
btn_alimentar = tk.Button(frame_jogo, text="🍖 Dar Comida", font=("Arial", 12), command=alimentar,fg="orange")
btn_alimentar.pack()

lbl_banheiro = tk.Label(frame_jogo, text="Banheiro: 100%", font=("Arial", 16, "bold"))
lbl_banheiro.pack(pady=10)
btn_mijar = tk.Button(frame_jogo, text="mijar", font=("Arial", 12), command=mijar)
btn_mijar.pack()

lbl_alegria = tk.Label(frame_jogo, text="Alegria: 100%", font=("Arial", 16, "bold"))
lbl_alegria.pack(pady=10)
btn_brincar = tk.Button(frame_jogo, text="Brincar", font=("Arial", 12), command=brincar)
btn_brincar.pack()

btn_voltar = tk.Button(frame_jogo, text="⬅ Voltar ao Menu", font=("Arial", 10), command=voltar_ao_menu)
btn_voltar.pack(pady=25)

#Relógio do Jogo e a Janela 
janela.mainloop()
