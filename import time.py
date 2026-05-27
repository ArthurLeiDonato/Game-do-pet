import time
import random
import json
import os

# =========================
# CONFIG
# =========================

ARQUIVO_SAVE = "pet_save.json"

# =========================
# PET
# =========================

pet = {
    "nome": "",
    "nivel": 1,
    "xp": 0,
    "moedas": 100,

    "fome": 100,
    "energia": 100,
    "felicidade": 100,
    "higiene": 100,
    "vida": 100,

    "inventario": {
        "maça": 3,
        "hamburguer": 1,
        "kit_medico": 1,
        "sabonete": 2
    }
}

# =========================
# SAVE / LOAD
# =========================

def salvar_jogo():
    with open(ARQUIVO_SAVE, "w") as arquivo:
        json.dump(pet, arquivo)

    print("\nJOGO SALVO!")

def carregar_jogo():
    global pet

    if os.path.exists(ARQUIVO_SAVE):
        with open(ARQUIVO_SAVE, "r") as arquivo:
            pet = json.load(arquivo)

        print("\nSAVE CARREGADO!")
        return True

    return False

# =========================
# STATUS
# =========================

def mostrar_status():
    print("\n=========================")
    print(f"PET: {pet['nome']}")
    print(f"Nível: {pet['nivel']}")
    print(f"XP: {pet['xp']}/100")
    print(f"Moedas: {pet['moedas']}")

    print("\nSTATUS")
    print(f"Fome: {pet['fome']}")
    print(f"Energia: {pet['energia']}")
    print(f"Felicidade: {pet['felicidade']}")
    print(f"Higiene: {pet['higiene']}")
    print(f"Vida: {pet['vida']}")
    print("=========================")

# =========================
# LIMITES
# =========================

def limitar_status():
    for status in ["fome", "energia", "felicidade", "higiene", "vida"]:

        if pet[status] > 100:
            pet[status] = 100

        if pet[status] < 0:
            pet[status] = 0

# =========================
# XP
# =========================

def ganhar_xp(valor):
    pet["xp"] += valor

    while pet["xp"] >= 100:
        pet["xp"] -= 100
        pet["nivel"] += 1

        print(f"\n{pet['nome']} SUBIU PARA O NÍVEL {pet['nivel']}!")

# =========================
# AÇÕES
# =========================

def alimentar():
    print("\nCOMIDAS:")
    print("1 - Maçã")
    print("2 - Hambúrguer")

    escolha = input("Escolha: ")

    if escolha == "1":

        if pet["inventario"]["maça"] > 0:
            pet["inventario"]["maça"] -= 1
            pet["fome"] += 20

            print("\nO pet comeu uma maçã!")
            ganhar_xp(10)

        else:
            print("\nVocê não tem maçãs.")

    elif escolha == "2":

        if pet["inventario"]["hamburguer"] > 0:
            pet["inventario"]["hamburguer"] -= 1

            pet["fome"] += 40
            pet["felicidade"] += 10

            print("\nO pet comeu um hambúrguer!")
            ganhar_xp(15)

        else:
            print("\nVocê não tem hambúrguer.")

def dormir():
    print("\nO pet está dormindo...")

    time.sleep(2)

    pet["energia"] += 40
    pet["vida"] += 10

    ganhar_xp(5)

def brincar():
    print("\nVocê brincou com o pet!")

    pet["felicidade"] += 25
    pet["energia"] -= 15
    pet["fome"] -= 10

    moedas = random.randint(10, 30)

    pet["moedas"] += moedas

    print(f"Você ganhou {moedas} moedas!")

    ganhar_xp(20)

def banho():
    if pet["inventario"]["sabonete"] > 0:

        pet["inventario"]["sabonete"] -= 1
        pet["higiene"] += 40

        print("\nO pet tomou banho!")

        ganhar_xp(10)

    else:
        print("\nVocê não tem sabonete.")

def usar_kit_medico():
    if pet["inventario"]["kit_medico"] > 0:

        pet["inventario"]["kit_medico"] -= 1
        pet["vida"] += 50

        print("\nKit médico utilizado!")

    else:
        print("\nVocê não possui kit médico.")

# =========================
# LOJA
# =========================

def loja():

    while True:

        print("\n===== LOJA =====")
        print("1 - Maçã (10 moedas)")
        print("2 - Hambúrguer (25 moedas)")
        print("3 - Sabonete (15 moedas)")
        print("4 - Kit médico (40 moedas)")
        print("5 - Sair")

        escolha = input("Escolha: ")

        if escolha == "1":

            if pet["moedas"] >= 10:
                pet["moedas"] -= 10
                pet["inventario"]["maça"] += 1

                print("Você comprou uma maçã!")

            else:
                print("Moedas insuficientes.")

        elif escolha == "2":

            if pet["moedas"] >= 25:
                pet["moedas"] -= 25
                pet["inventario"]["hamburguer"] += 1

                print("Você comprou um hambúrguer!")

            else:
                print("Moedas insuficientes.")

        elif escolha == "3":

            if pet["moedas"] >= 15:
                pet["moedas"] -= 15
                pet["inventario"]["sabonete"] += 1

                print("Você comprou um sabonete!")

            else:
                print("Moedas insuficientes.")

        elif escolha == "4":

            if pet["moedas"] >= 40:
                pet["moedas"] -= 40
                pet["inventario"]["kit_medico"] += 1

                print("Você comprou um kit médico!")

            else:
                print("Moedas insuficientes.")

        elif escolha == "5":
            break

# =========================
# INVENTÁRIO
# =========================

def mostrar_inventario():

    print("\n===== INVENTÁRIO =====")

    for item, quantidade in pet["inventario"].items():
        print(f"{item}: {quantidade}")

# =========================
# PASSAGEM DE TEMPO
# =========================

def passar_tempo():

    pet["fome"] -= random.randint(2, 5)
    pet["energia"] -= random.randint(1, 4)
    pet["felicidade"] -= random.randint(1, 3)
    pet["higiene"] -= random.randint(1, 4)

    if pet["fome"] <= 0:
        pet["vida"] -= 5

    if pet["energia"] <= 0:
        pet["vida"] -= 5

    limitar_status()

# =========================
# GAME OVER
# =========================

def verificar_game_over():

    if pet["vida"] <= 0:
        print(f"\n{pet['nome']} ficou sem vida...")
        print("GAME OVER")

        exit()

# =========================
# INÍCIO
# =========================

print("===== PET GAME =====")

if not carregar_jogo():

    pet["nome"] = input("Digite o nome do seu pet: ")

# =========================
# LOOP PRINCIPAL
# =========================

while True:

    mostrar_status()

    print("\n===== MENU =====")
    print("1 - Alimentar")
    print("2 - Dormir")
    print("3 - Brincar")
    print("4 - Banho")
    print("5 - Loja")
    print("6 - Inventário")
    print("7 - Kit Médico")
    print("8 - Salvar")
    print("9 - Sair")

    escolha = input("\nEscolha: ")

    if escolha == "1":
        alimentar()

    elif escolha == "2":
        dormir()

    elif escolha == "3":
        brincar()

    elif escolha == "4":
        banho()

    elif escolha == "5":
        loja()

    elif escolha == "6":
        mostrar_inventario()

    elif escolha == "7":
        usar_kit_medico()

    elif escolha == "8":
        salvar_jogo()

    elif escolha == "9":
        salvar_jogo()
        print("Saindo...")
        break

    passar_tempo()

    verificar_game_over()

    time.sleep(1)