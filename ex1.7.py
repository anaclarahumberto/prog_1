nome_produto = input("Digite o nome do produto:")
preco_custo = float(input("Digite o preço de custo do produto:"))
preco_venda = float(input("Digite o preço de venda do produto:"))
quantidade_produto_estoque = int(input("Digite a quantidade do produto em estoque:"))

lucro = preco_venda - preco_custo
lucro_total = lucro * quantidade_produto_estoque
print(f"O lucro gerado por esse produto na queima de estoque é de R${lucro_total}")


                    