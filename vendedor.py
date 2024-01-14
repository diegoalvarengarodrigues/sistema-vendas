from pessoa import Pessoa

class Vendedor(Pessoa):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf)
        self.salario = salario
        
    def to_dict(self):
        pessoa_dict = super().to_dict()
        pessoa_dict['salario'] = self.salario
        return pessoa_dict
    