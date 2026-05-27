import tkinter as tk
from tkinter import messagebox
import random

# =====================
# STATUS DO PET
# =====================

pet = {
    "nome": "Kumo",
    "fome": 100,
    "energia": 100,
    "felicidade": 100,
    "higiene": 100
}

# =====================
# FUNÇÕES
# =====================

def limitar():
    for status in pet:
        if status != "nome":

            if pet[status] > 100:
                pet[status] = 100

            if pet[status] < 0:
                pet[status] = 0

def atualizar_tela():

    fome_label.config(text=f"Fome: {pet['fome']}")
    energia_label.config(text=f"Energia: {pet['energia']}")
    felicidade_label.config(text=f"Felicidade: {pet['felicidade']}")
    higiene_label.config(text=f"Higiene: {pet['higiene']}")

def alimentar():
    pet["fome"] += 20
    limitar()
    atualizar_tela()

def dormir():
    pet["energia"] += 30
    limitar()
    atualizar_tela()

def brincar():
    pet["felicidade"] += 25
    pet["energia"] -= 10
    pet["fome"] -= 5

    limitar()
    atualizar_tela()

def banho():
    pet["higiene"] += 30
    limitar()
    atualizar_tela()

# =====================
# TEMPO PASSANDO
# =====================

def passar_tempo():

    pet["fome"] -= random.randint(1, 3)
    pet["energia"] -= random.randint(1, 2)
    pet["felicidade"] -= random.randint(1, 2)
    pet["higiene"] -= random.randint(1, 2)

    limitar()
    atualizar_tela()

    if pet["fome"] <= 0:
        messagebox.showwarning(
            "Aviso",
            "Seu pet está com muita fome!"
        )

    janela.after(3000, passar_tempo)

# =====================
# JANELA
# =====================

janela = tk.Tk()

janela.title("Pet Game")
janela.geometry("400x500")
janela.configure(bg="#222222")

# =====================
# TÍTULO
# =====================

titulo = tk.Label(
    janela,
    text=pet["nome"],
    font=("Arial", 24),
    bg="#222222",
    fg="white"
)

titulo.pack(pady=20)

# =====================
# STATUS
# =====================

fome_label = tk.Label(
    janela,
    text="",
    font=("Arial", 14),
    bg="#222222",
    fg="white"
)

fome_label.pack(pady=5)

energia_label = tk.Label(
    janela,
    text="",
    font=("Arial", 14),
    bg="#222222",
    fg="white"
)

energia_label.pack(pady=5)

felicidade_label = tk.Label(
    janela,
    text="",
    font=("Arial", 14),
    bg="#222222",
    fg="white"
)

felicidade_label.pack(pady=5)

higiene_label = tk.Label(
    janela,
    text="",
    font=("Arial", 14),
    bg="#222222",
    fg="white"
)

higiene_label.pack(pady=5)

# =====================
# BOTÕES
# =====================

botao_alimentar = tk.Button(
    janela,
    text="Alimentar",
    font=("Arial", 12),
    width=20,
    command=alimentar
)

botao_alimentar.pack(pady=10)

botao_dormir = tk.Button(
    janela,
    text="Dormir",
    font=("Arial", 12),
    width=20,
    command=dormir
)

botao_dormir.pack(pady=10)

botao_brincar = tk.Button(
    janela,
    text="Brincar",
    font=("Arial", 12),
    width=20,
    command=brincar
)

botao_brincar.pack(pady=10)

botao_banho = tk.Button(
    janela,
    text="Banho",
    font=("Arial", 12),
    width=20,
    command=banho
)

botao_banho.pack(pady=10)

# =====================
# INICIAR
# =====================

atualizar_tela()
passar_tempo()

janela.mainloop()