#1 - Importar Base de dados (pandas)
import pandas as pd
import xml
import openpyxl
from collections import OrderedDict

class Produtos():
    def __init__(self, bd_produtos):
        self.bd_produtos = bd_produtos

    def Fornecedores():
        bd_produtos = pd.read_excel('./produtos/Precificação SC.xlsx')
        fornecedores = list(bd_produtos['Fornecedor'])

        #print (fornecedores)

        OrderedDict.fromkeys(fornecedores)
        fornecedores_final = list(OrderedDict.fromkeys(fornecedores))

        #print(fornecedores_final)

    def Produtos():
        bd_produtos = pd.read_excel('./produtos/Precificação SC.xlsx')
        produtos = list(bd_produtos['Produto'])

        #print (produtos)

        OrderedDict.fromkeys(produtos)
        produtos_final = list(OrderedDict.fromkeys(produtos))

        #print(produtos_final)

    def Sku():
        bd_produtos = pd.read_excel('./produtos/Precificação SC.xlsx')
        sku = list(bd_produtos['SKU'])

        #print (sku)

        OrderedDict.fromkeys(sku)
        sku_final = list(OrderedDict.fromkeys(sku))

        #print(sku_final)
        

    
        

produto = Produtos
produto.Fornecedores()
produto.Produtos()
produto.Sku()
