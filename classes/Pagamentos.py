class Pagamento:
    def __init__(self,pedido,pessoa,carrinho):
        self.pedido = pedido 
        self.pessoa = pessoa
        self.carrinho = carrinho

    def processa_pagamento(self):
        pass 

    # Função dummy que sempre dá o pagamento como aprovado
    def pagamento_aprovado():
        return True
    
    def detalhes(self):
        return self.pessoa.nome + ' ' + self.pessoa.listar_enderecos + ' ' + self.carrinho.itens

