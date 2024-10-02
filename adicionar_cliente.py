import csv
import time
import os

def msg_manner(msg):
    print(msg.center(50, '-'))
    
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_cliente():
    while True:
        clear_terminal()
        msg_manner("Adicionar Cliente(s)!")
        name = input("Informe o nome do cliente: ")
        age = int(input("Digite a idade do cliente: "))
        address = str(input("Digite endereço do cliente: "))
        phone = str(input("Digite telefone do cliente: "))
        

        with open("clientes.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow([name, age, address, phone])
        
        continuar = ' '
        while continuar != 's' and continuar != 'n':
            continuar = input("Deseja adicionar mais clientes [S/N]? ").lower()
        
        if continuar == 'n':
            print("Saindo...")
            time.sleep(0.5)
            break
        msg_manner("Cliente Adicionado!")
        time.sleep(0.5)