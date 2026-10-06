mercearia = ["Frutas", "Verduras", "Arroz", "Carne", "Detergente"]

#print(type(mercearia))
#print(mercearia)

mercearia[4] = "Feijão"
print(mercearia)

#exibindo a lista completa
for item in mercearia:
    print(item)

#insenrindo item ao final da lista

mercearia.append("Batata")
print(mercearia)

#iNSERINDO ITEM EM QUALQUER LUGAR DA LISTA

mercearia.insert(2,"Açúcar Mascavo")
print(mercearia)

#removendo o último item da lista

mercearia.pop()
print(mercearia)

#removendo qualquer item da lista

mercearia.pop(4)
print(mercearia)

mercearia.remove("Açúcar Mascavo")
print(mercearia)