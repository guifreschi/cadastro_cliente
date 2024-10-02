import csv
import os

def msg_manner(msg):
    print(msg.center(50, '-'))

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def listar_cliente():
    while True:
        msg_manner("Listar Clientes!")
        clientes = []

        with open("clientes.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                clientes.append({"Nome": row["Nome"], "Idade": row["Idade"], "Endereço": row["Endereço"], "Telefone": row["Telefone"]})

        # Verifica se há clientes
        if not clientes:
            print("Nenhum cliente encontrado.")
        else:
            for cliente in sorted(clientes, key=lambda cliente: cliente["Nome"]):
                print(f"{cliente['Nome']}: {cliente['Idade']} anos. {cliente['Endereço']}. Telefone:{cliente['Telefone']}.")

        input("Dê um Enter para sair...")
        break
