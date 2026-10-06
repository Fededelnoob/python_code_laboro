#verificando ocorrências de um item em uma lista

cardapio = ["refrigerante", "dogão", "frituras", "sobremesa", "burguer"]

while True:
    resposta = input("Informe um possivel item do cardápio: ")

    if resposta in cardapio: 
        print(f"o item {resposta} existe no cardápio!")
        break
    else:
        print(f"O item {resposta} não existe no cardápio, tente de novo")