class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        
    def to_dict(self):
        return {'nome': self.nome, 'cpf': self.cpf}
    
