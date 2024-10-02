import csv
import os
import listar_cliente as lc

def msg_manner(msg):
    print(msg.center(50, '-'))

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def verificar_clientes():
    with open('clientes.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        linhas = list(reader)
        if not linhas:
            print("Não há clientes cadastrados.")
            input("Dê um Enter para sair...")
            return False
        else:
            print("Clientes cadastrados:")
            lc.listar_cliente()
            return True

def remover_cliente():
    clear_terminal()
    msg_manner("Remover Cliente")
    if not verificar_clientes():
        return
    
    continuar = 's'
    while continuar == 's':
        linhas = []
        cliente_encontrado = False
        
        nome = input("\nDigite o nome do cliente que deseja remover: ")
        
        # Lê o arquivo CSV e armazena as linhas em uma lista, exceto a linha a ser removida
        with open('clientes.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Nome"] == nome:
                    cliente_encontrado = True
                else:
                    linhas.append(row)
                    
        if cliente_encontrado:
            # Escreve as linhas restantes de volta no arquivo CSV
            with open("clientes.csv", "w", encoding="utf-8", newline='') as file:
                fieldnames = ["Nome", "Idade", "Endereço", "Telefone"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(linhas)
                
            print("Cliente removido com sucesso...")
        else:
            print("Cliente não encontrado.")
        
        continuar = input("Deseja remover mais cliente [S/N]? ").lower()
        if continuar == 's':
            clear_terminal()
            msg_manner("Remover Cliente")
            if not verificar_clientes():
                return

