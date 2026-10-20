"""

chave : valor -> dicionário

valor ->


"""
contatos = {"huguinho":123, "zezinho":234, "luisinho":345} #dict()

print(type(contatos))

print(contatos)

#ADD ITENS AO DICIONÁRIO

#FORMA 1
contatos["donald"] = 456

print(contatos)

#FORMA 2
contatos.update({"patricia":567}) #ADD NOVO ITEM

print(contatos)

contatos.update({"huguinho":670}) #ADD UM VALOR EXISTENTE

print(contatos)

#EXCLUINDO DADOS DO DICIONÁRIO
#FORMA 1
contatos.pop("donald")
print(contatos)

#FORMA 2
del contatos["patricia"]
print(contatos)

#EXCLUSÃO GALÁTICA (TOTAL DO DICIONÁRIO)

contatos.clear()
print(contatos)