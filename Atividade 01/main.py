import sys
from PyQt5.QtWidgets import QApplication
from categoria import Categoria
from notbook import Notbook
from desktop import Desktop

app = QApplication(sys.argv)

categorias = []
cat = Categoria("Cadastro de Categoria")

notbook = Notbook("Cadastro de Notbook", 2500.0, cat)
notbook.show()

sys.exit(app.exec_())
