#A classe Apartamento deve conter os atributos, id, número do apartamento, número da vaga de garagem e torre.
from Torre import Torre

class Apartamento:
    def __init__(self, id, numero_ap, vaga_garagem, torre):
        self.id = id
        self.nuemro_ap = numero_ap
        self.vaga_garagem = vaga_garagem
        self.torre = torre
        self.prox = None
    
    def __str__(self):
        vaga_info = self.vaga if self.vaga else "Sem vaga"
        return f"Apto {self.numero} | Torre: {self.torre.nome} | Vaga: {vaga_info}"


