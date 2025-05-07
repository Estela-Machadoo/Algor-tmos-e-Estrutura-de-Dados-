from produto import Produto

class Desktop(Produto):
    def __init__(self, nome, preco=0.0, gabinete="Padrão", categoria=None):
        super().__init__(nome, preco)
        self.gabinete = gabinete
        self.categoria = categoria

    def __str__(self):
        return super().__str__() + f"\nGabinete: {self.gabinete}\nCategoria: {self.categoria}"
