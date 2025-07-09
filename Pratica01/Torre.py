#A classe Torre deve possuir os atributos id, nome e endereço. 

class Torre:
    def __init__(self, id, nome, endereço):
        self.id = id
        self.nome = nome
        self.endereço = endereço
        self.prox = None

        