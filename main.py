
def voltarMenu():
    while True:
        resposta = input("\nDeseja voltar ao menu principal? (s/n): \n")
        if resposta.lower() == "s":
            main()
            break
        elif resposta.lower() == "n":
            print("\nEncerrando o programa.\n")
            exit()
        else:
            print("\nResposta inválida. Por favor, digite 's' para sim ou 'n' para não.\n")

def adicionar_produto():
    nome = input("\nDigite o nome do produto: \n")
    quantidade = input("\nDigite a quantidade do produto: \n")
    preco = input("\nDigite o preço do produto: \n")
    with open(r"C:\Users\luizl\Documents\Estudos\Sistema de Estoque\estoque.txt", "a") as estoque:
        estoque.write(f"{nome},{quantidade},{preco}\n")
    print("\nProduto adicionado com sucesso!\n")
    voltarMenu()

def excluir_produto():
            nome = input("\nDigite o nome do produto que deseja excluir: \n")
            produtos = []
            encontrado = False
            with open(r"C:\Users\luizl\Documents\Estudos\Sistema de Estoque\estoque.txt", "r") as estoque:
                for linha in estoque:
                    produto = linha.strip().split(",")
                    if nome == produto[0]:
                        encontrado = True
                    else:
                        produtos.append(linha)
            if encontrado:
                with open(r"C:\Users\luizl\Documents\Estudos\Sistema de Estoque\estoque.txt", "w") as estoque:
                    estoque.writelines(produtos)
                print("\nProduto excluído com sucesso!\n")
            else:
                print("\nProduto não encontrado.\n")
            voltarMenu()

def buscar_produto():
    nome = input("\nDigite o nome do produto que deseja buscar: \n")
    with open(r"C:\Users\luizl\Documents\Estudos\Sistema de Estoque\estoque.txt", "r") as estoque:
        for linha in estoque:
            produto = linha.strip().split(",")
            if produto[0] == nome:
                print(f"Produto encontrado: {produto[0]}, Quantidade: {produto[1]}, Preço: {produto[2]}")
                return
            voltarMenu()
    print("\nProduto não encontrado.\n")
    voltarMenu()

def mostrarEstoque():
    with open(r"C:\Users\luizl\Documents\Estudos\Sistema de Estoque\estoque.txt", "r") as estoque:
        print("\nEstoque atual:\n")
        for linha in estoque:
            produto = linha.strip().split(",")
            print(f"Produto: {produto[0]}, Quantidade: {produto[1]}, Preço: {produto[2]}")
    voltarMenu()


def main():
    while True:
        selecao = input("\nDigite a opção desejada: \n1 - Adicionar produto\n2 - Excluir produto\n3 - Buscar produto\n4 - Mostrar estoque\n")
        if selecao == "1":
            adicionar_produto()
        elif selecao == "2":
            excluir_produto()
        elif selecao == "3":
            buscar_produto()
        elif selecao == "4":
            mostrarEstoque()
        else:
            print("\nOpção inválida.\n")
main() 
