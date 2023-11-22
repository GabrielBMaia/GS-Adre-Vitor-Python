import json

# usuarios
# compartilhamentos
# entradas

def sobrescreve_usuarios(usuarios):

    with open('./bases/usuarios.json', 'w', encoding='utf-8') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(usuarios, arquivo)

def sobrescreve_compartilhamentos(compartilhamentos):

    with open('./bases/compartilhamentos.json', 'w', encoding='utf-8') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(compartilhamentos, arquivo)

def sobrescreve_entradas(entradas):

    with open('./bases/entradas.json', 'w', encoding='utf-8') as arquivo:
        # Gravar os dados em formato JSON no arquivo
        json.dump(entradas, arquivo)

def carrega_usuarios():
    try:
        with open('./bases/usuarios.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            usuarios = json.load(arquivo)
            return usuarios
    except FileNotFoundError:
        return ['arquivo n encontrado'] 
    
def carrega_compartilhamentos():
    try:
        with open('./bases/compartilhamentos.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            compartilhamentos = json.load(arquivo)
            return compartilhamentos
    except FileNotFoundError:
        return ['arquivo n encontrado']
    
def carrega_entradas():
    try:
        with open('./bases/entradas.json', 'r', encoding='utf-8') as arquivo:
            # Ler os dados em formato JSON do arquivo
            entradas = json.load(arquivo)
            return entradas
    except FileNotFoundError:
        return ['arquivo n encontrado']


