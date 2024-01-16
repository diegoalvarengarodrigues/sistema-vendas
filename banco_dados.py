import json


def salvar_em_arquivo(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
        json.dump(dados, file)
    
def carregar_de_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []