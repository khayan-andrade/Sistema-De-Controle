
class Produto:
    def __init__(self, id, nome, quantidade, categoria_id, preco):
      self.id = id 
      self.nome = nome
      self.quantiade = quantidade
      self.categoria = categoria_id
      self.preco = preco 
class categoria:
    def __init__(self, id , nome):
      self.id = id 
      self. nome = nome 
class movimentacao:
    def __init__(self, id, produto_id, quantidade, data, tipo_movimentacao):
      self.id = id
      self.produto_id = produto_id 
      self.quantidade = quantidade
      self.tipo_movimentacao = tipo_movimentacao
      self.data = data 
def cadastrar_produtos(produtos, contador_produtos):
  id = contador_produtos + 1 
  nome = input(" Nome do produto")
  categoria_id = int(input("ID da categoria:"))
  quantidade = int(input(" Insira a quantidade: "))
  preco = float(input("Insira o preço:"))
  produtos.append(Produto(id,nome,categoria_id,quantidade, preco))
  return contador_produtos + 1 

def consultar_produto_id(produtos, id):
   for produto in produtos:
     if produto.id == id:
       print(f'ID:{produto.id}, Nome: {produto.nome}, Categoria: {produto.categoria_id}, quantidade: {produto.quantidade}, preço: {produto.preco}')
       return

print ('Produto não encontrado')
produtos = []
contador = 0 

contador = cadastrar_produtos( produtos, contador )
 
consultar_produto_id(produtos, contador) 

  