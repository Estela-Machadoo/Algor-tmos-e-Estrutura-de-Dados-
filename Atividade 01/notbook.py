from produto import Produto

class Notbook(Produto):
    def __init__(self, nome, preco=0.0, polegadas=15.6, categoria=None):
        super().__init__(nome, preco)
        self.polegadas = polegadas
        self.categoria = categoria

    def __str__(self):
        return super().__str__() + f"\nTela: {self.polegadas}\" \nCategoria: {self.categoria}"
