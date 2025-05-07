class Produto:
    def __init__(self, nome, preco=0.0):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome}\nPreço: R${self.preco:.2f}"
