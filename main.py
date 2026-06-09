import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

aba_consulta = tk.Tk()
aba_consulta.title("Sistema de Estoque")
aba_consulta.geometry("1280x720")
#aba_consulta.state("zoomed")

aba_consulta.rowconfigure(0, weight=1)
aba_consulta .columnconfigure(0, weight=1)

abas = ttk.Notebook(aba_consulta)
abas.grid(row=0, column=0, sticky="nsew")

#ABAS
aba_consulta = tk.Frame(abas)
aba_estoque = tk.Frame(abas)
aba_cadastro = tk.Frame(abas)

#MENU DE ABAS SUPERIOR
abas.add(aba_consulta, text="Consulta")
abas.add(aba_estoque, text="Estoque")
abas.add(aba_cadastro, text="Cadastro")

#ITENS DA ABA CONSULTA ///ABA CONSULTA
tk.Label(aba_consulta, text="Bem-vindo ao Sistema de Estoque!", font=("Arial", 24)).grid(row=0, column=1, padx=10, pady=10, sticky="w")

#ITENS DA ABA ESTOQUE ///ABA ESTOQUE
tk.Label(aba_estoque, text="ESTOQUE", font=("Arial", 15)).grid(row=0, column=1, padx=10, pady=10, sticky="w")

label_excluir = tk.Label(aba_estoque, text="Id do Produto Para Exclusão:")
label_excluir.grid(row=5, column=0, padx=10, pady=10, sticky="w")

excluir = tk.Entry(aba_estoque)
excluir.grid(row=5, column=1, padx=10, pady=10)

tk.Button(aba_estoque, text="Excluir produto", command=lambda: [excluir_produto(), excluir.delete(0, tk.END)]).grid(row=5, column=2, padx=20, pady=10)

#DESCRIÇÃO DE CADA INPUT DA ABA CADASTRO ///ABA CADASTRO
label_nome = tk.Label(aba_cadastro, text="Nome do Produto:")
label_nome.grid(row=1, column=0, padx=10, pady=10, sticky="w")

label_quantidade = tk.Label(aba_cadastro, text="Quantidade:")
label_quantidade.grid(row=2, column=0, padx=10, pady=10, sticky="w")

label_preco = tk.Label(aba_cadastro, text="Preço:")
label_preco.grid(row=3, column=0, padx=10, pady=10, sticky="w")

#INPUTS DA ABA CADASTRO ///ABA CADASTRO

nome = tk.Entry(aba_cadastro)
nome.grid(row=1, column=1, padx=10, pady=10)

quantidade = tk.Entry(aba_cadastro)
quantidade.grid(row=2, column=1, padx=10, pady=10)

preco = tk.Entry(aba_cadastro)
preco.grid(row=3, column=1, padx=10, pady=10)

tk.Button(aba_cadastro, text="Adicionar produto", command=lambda: [adicionar_produto(), nome.delete(0, tk.END), quantidade.delete(0, tk.END), preco.delete(0, tk.END)]).grid(row=5, column=1, padx=20, pady=10)


def gerar_proximo_id():
    maior_id = -1

    try:
        with open(r"C:\Users\luizl\Documents\Estudos\Sistema de Estoque\estoque.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(",")

                if len(partes) >= 4:
                    id_produto = int(partes[0])

                    if id_produto > maior_id:
                        maior_id = id_produto

    except FileNotFoundError:
        maior_id = -1

    return maior_id + 1

def adicionar_produto():
    novo_id = gerar_proximo_id()
    if not nome.get() or not quantidade.get() or not preco.get():
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return
    with open(r"C:\Users\luizl\Documents\Estudos\Sistema de Estoque\estoque.txt", "a") as estoque:
        estoque.write(f"{novo_id},{nome.get()},{quantidade.get()},{preco.get()}\n")
    messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")

def excluir_produto():
            nome = excluir.get()
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
                messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
            else:
                messagebox.showerror("Erro", "Produto não encontrado.")
            

def buscar_produto():
    nome = input("\nDigite o nome do produto que deseja buscar: \n")
    with open(r"C:\Users\luizl\Documents\Estudos\Sistema de Estoque\estoque.txt", "r") as estoque:
        for linha in estoque:
            produto = linha.strip().split(",")
            if produto[0] == nome:
                print(f"Produto encontrado: {produto[0]}, Quantidade: {produto[1]}, Preço: {produto[2]}")
                return
    print("\nProduto não encontrado.\n")

frame_lista_estoque = tk.Frame(aba_estoque)
frame_lista_estoque.grid(row=5, column=6, padx=10, pady=10, sticky="w")

tabela_estoque = ttk.Treeview(
    aba_estoque,
    columns=("Id", "produto", "quantidade", "preco"),
    show="headings",
    height=20
)
tabela_estoque.heading("Id", text="Id")
tabela_estoque.heading("produto", text="Produto")
tabela_estoque.heading("quantidade", text="Quantidade")
tabela_estoque.heading("preco", text="Preço")

tabela_estoque.column("Id", width=120)
tabela_estoque.column("produto", width=250)
tabela_estoque.column("quantidade", width=200, minwidth=200, anchor="center")
tabela_estoque.column("preco", width=120)

tabela_estoque.grid(row=5, column=6, padx=20, pady=20, sticky="nsew")

def listar_produtos():
    tabela_estoque.delete(*tabela_estoque.get_children())

    with open(r"C:\Users\luizl\Documents\Estudos\Sistema de Estoque\estoque.txt", "r") as estoque:
        for linha in estoque:
            produto = linha.strip().split(",")

            if len(produto) >= 4:
                tabela_estoque.insert(
                    "",
                    "end",
                    values=(
                        produto[0],
                        produto[1],
                        produto[2],
                        produto[3]
                    )
                )

    tabela_estoque.after(1000, listar_produtos)

listar_produtos()
    
aba_consulta.mainloop()