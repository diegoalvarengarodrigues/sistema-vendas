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
        cupom = f"======= Cupom Fiscal =======\n"
        cupom += f"Cliente: {self.cliente.nome}\n"
        cupom += f"Vendedor: {self.vendedor.nome}\n"
        cupom += f"======= Produtos =======\n"
        for produto in self.produtos:
            cupom += f"{produto.nome}: R${produto.preco:.2f}\n"
        cupom += f"======= Total: R${self.calcular_total():.2f} =======\n"
        cupom += f"Forma de Pagamento: {forma_pagamento}\n"
        cupom += f"===========================\n"
        return cupom
    
        