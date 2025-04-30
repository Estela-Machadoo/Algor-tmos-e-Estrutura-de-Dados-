from Cliente import Cliente

class Juridico( Cliente ):

    def __init__(self, nome, cnpj = None):
        super().__init__(nome)
        self.cnpj = cnpj

    def __str__(self):
        return super().__str__() + "\nCNPJ: " + self.cnpj

    def cadastrar(self):
        self.nome = input("Digite o nome: ")
        self.cnpj = input("Digite o cnpj: ")