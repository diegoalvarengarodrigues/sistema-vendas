from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, cpf, endereco):
        super().__init__(nome, cpf)
        self.endereco = endereco
        
    def to_dict(self):
        pessoa_dict = super().to_dict()
        pessoa_dict['endereco'] = self.endereco
        return pessoa_dict
    