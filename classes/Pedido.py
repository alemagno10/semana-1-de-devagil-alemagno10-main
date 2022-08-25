#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re

class Pedido:
    EM_ABERTO = 1
    PAGO = 2

    def __init__(self,pessoa,carrinho):
        self.pessoa = pessoa
        self.carrinho = carrinho
    
    def detalhes(self):
        return f'Nome: {self.pessoa.nome}. Endereços: {list(self.pessoa.listar_enderecos().keys())}. Produtos: {self.carrinho.itens()}'
    
