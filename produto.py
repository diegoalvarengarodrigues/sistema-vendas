class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        
    def to_dict(self):
        return {'codigo': self.codigo, 'nome': self.nome, 'preco': self.preco}
    