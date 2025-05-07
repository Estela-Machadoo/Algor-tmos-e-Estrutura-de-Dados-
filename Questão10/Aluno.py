from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula):
        self.nome = nome
        super().__init__(cpf)
        self.___matricula = matricula  

 
    def get_matricula(self):
        return self.___matricula

   
    def set_matricula(self, nova_matricula):
        self.___matricula = nova_matricula


    def marcarPresenca(self):
        print(f"Aluno com matrícula {self.___matricula} marcou presença.")
