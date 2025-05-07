import sys
from PyQt5.QtWidgets import QApplication
from categoria import Categoria
from notbook import Notbook
from desktop import Desktop

app = QApplication(sys.argv)

categorias = []
cat = Categoria("Cadastro de Categoria", categorias)

notbook = Notbook("Cadastro de Notbook", categorias, cat)
desktop = Desktop("Cadastro de Desktop", categorias, cat)

notbook.show()

sys.exit(app.exec_())
