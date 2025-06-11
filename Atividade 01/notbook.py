class Notbook(QWidget):  
    def __init__(self, nome, preco=0.0, categoria=None):
        super().__init__()

        self.produto = Produto(nome, preco)
        self.categoria = categoria

        self.setWindowTitle(nome)
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Nome: {nome}"))
        layout.addWidget(QLabel(f"Preço: R${preco:.2f}"))
        layout.addWidget(QLabel(f"Categoria: {categoria}"))

        self.setLayout(layout)
