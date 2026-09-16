import sqlite3

conexao = sqlite3.connect("doceria.db")


brigadeiro = 5
beijinho = 4
bolo = 10
brownie = 8


print("SEJA BEM VINDO A DOCERIA!!")
print("Faça seu pedido conosco")
print("""
================================
            DOCERIA
================================
    A - Brigadeiro ........ R$ 5,00
    B - Beijinho .......... R$ 4,00
    C - Bolo .............. R$ 10,00
    D - Brownie ........... R$ 8,00
================================
""")
valortotal = 0
while True:
    opcao = input("Digite a letra do produto que deseja:").lower()
    quantidade = int(input("Digite a quantidade desejada:"))

    if opcao == "a":
        valortotal = valortotal + (brigadeiro * quantidade)

    elif opcao == "b":
        valortotal = valortotal + (beijinho * quantidade)

    elif opcao == "c":
        valortotal = valortotal + (Bolo * quantidade)

    elif opcao == "d":
        valortotal = valortotal + (brownie * quantidade)

    else:
        print("Produto não encontrado")
        continue

    print("Total do produto: R$", valortotal)

    final = input("Finalizar pedido digite 1, continuar pedido digite 2:")

    if final == "1":
        print("Pedido finalizado")
        print("Valor total: R$", valortotal)
        break

    elif final == "2":
        print("COntinuando pedido...")