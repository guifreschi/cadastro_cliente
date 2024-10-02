import csv
import os

def msg_manner(msg):
    print(msg.center(50, '-'))

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def atualizar_info(nome, campo, nova_info):
    clear_terminal()
    linhas = []
    cliente_encontrado = False
    
    # Verifica se o campo existe no CSV
    with open("clientes.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        if campo not in fieldnames:
            print(f"Campo '{campo}' não existe no arquivo CSV.")
            return
    
    # Lê o arquivo CSV e armazena as linhas em uma lista
    with open('clientes.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Nome"] == nome:
                row[campo] = nova_info
                cliente_encontrado = True
                msg_manner("Dado atualizado com sucesso!")
            linhas.append(row)
            
    if not cliente_encontrado:
        print("Cliente não encontrado...")
                
                
    # Escreve as linhas atualizadas de volta no arquivo CSV
    with open("clientes.csv", "w", encoding="utf-8", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(linhas)
        
    input("Dê Enter para sair...")