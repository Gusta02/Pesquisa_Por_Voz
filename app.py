#4 - Procurar na tabela a partir do topico 3  - (https://www.youtube.com/watch?v=kzVfvC29hQo)
#5 - imprimir resultado na tela

from produtos import Produtos
from voz import Bot_Ouvido
import pandas as pd
#import numpy as np

#1 a base de dados
#2 A frase dita
#3 Encotra na base de dados 

class Main():
    def __init__(self):
        self.marcas = Produtos.Fornecedores()
        self.Produtos = Produtos.Produtos()
        self.Sku = Produtos.Sku()
        self.frase = Bot_Ouvido.text

    def ValorProcurado(self):
        self.frase = []


    def EncontraProduto(self):

        frase = self.frase


        resultado = self.marcas.index({frase})

        print(resultado)

sla = Main()
sla.ValorProcurado()
sla.EncontraProduto()

