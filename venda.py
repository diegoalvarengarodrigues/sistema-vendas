import json

class Venda:
    def __init__(self, cliente, vendedor):
        self.cliente = cliente
        self.vendedor = vendedor
        self.produtos = []
        
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def calcular_total(self):
        return sum(produto.preco for produto in self.produtos)
    
    def emitir_cupom_fiscal(self, forma_pagamento):
        pass
    
    def salvar_em_arquivo(dados, nome_arquivo):
        with open(nome_arquivo, 'w') as file:
            json.dump(dados, file)
    
    def carregar_de_arquivo(nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        