import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

aba_estoque = tk.Tk()
aba_estoque.title("Sistema de Estoque")
aba_estoque.geometry("1280x720")
#aba_estoque.state("zoomed")

aba_estoque.rowconfigure(0, weight=1)
aba_estoque .columnconfigure(0, weight=1)

abas = ttk.Notebook(aba_estoque)
abas.grid(row=0, column=0, sticky="nsew")

#ABAS
aba_estoque = tk.Frame(abas)
aba_cadastro = tk.Frame(abas)

#MENU DE ABAS SUPERIOR
abas.add(aba_estoque, text="Estoque")
abas.add(aba_cadastro, text="Cadastro")

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
            

def listar_busca():
    tabela_estoque.delete(*tabela_estoque.get_children())

    nome = buscarNome.get()
    id_busca = buscarId.get()
    encontrado = False
    with open(r"C:\Users\luizl\Documents\Estudos\Sistema de Estoque\estoque.txt", "r") as estoque:
        for linha in estoque:
            produto = linha.strip().split(",")

            if len(produto) >= 4:
                if nome == produto[1] or id_busca == produto[0]:
                    encontrado = True

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

    if not encontrado:
        messagebox.showerror("Erro", "Produto não encontrado.")
        listar_produtos()

#TABELA E ITENS DO ESTOQUE
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

tabela_estoque.column("Id", width=120, anchor="center")
tabela_estoque.column("produto", width=250, anchor="center")
tabela_estoque.column("quantidade", width=200, minwidth=200, anchor="center")
tabela_estoque.column("preco", width=120, anchor="center")

tabela_estoque.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

#FRAME PRA DEIXAR INPU E LABEL NA MESMA COLUNA DA TABELA
frame_lado = tk.Frame(aba_estoque)
frame_lado.grid(row=2, column=1, padx=30, sticky="ns")
frame_cima = tk.Frame(aba_estoque)
frame_cima.grid(row=0, column=0, padx=5, sticky="w")

frame_controles = tk.Frame(frame_lado)
frame_controles.grid(row=4, column=0)

# Label um pouco acima do input
label_busca = tk.Label(frame_cima, text="Buscar produto:", font=("Arial", 12))
label_busca.grid(row=1, column=0, padx=10, pady=10, sticky="w")

#BOTAO E INPUT DE BUSCA ITEM
buscarNome = tk.Entry(frame_cima)
buscarNome.grid(row=1, column=1, padx=10, pady=0)
buscarId = tk.Entry(frame_cima)
buscarId.grid(row=1, column=2, padx=10, pady=0)
tk.Button(frame_cima, text="Buscar", command=lambda: [listar_busca(), buscarId.delete(0, tk.END), buscarNome.delete(0, tk.END)]).grid(row=1, column=3, padx=10, pady=0)
tk.Button(frame_cima, text="Mostrar Todos", command=lambda: [listar_produtos(), buscarId.delete(0, tk.END), buscarNome.delete(0, tk.END)]).grid(row=1, column=4, padx=10, pady=0)
tk.Label(frame_cima, text="ID", font=("Arial", 10)).grid(row=2, column=2, padx=(1,0), pady=0)
tk.Label(frame_cima, text="Nome", font=("Arial", 10)).grid(row=2, column=1, padx=(1,0), pady=0)

tk.Label(frame_cima, text="ESTOQUE", font=("Arial", 30, "bold")).grid(row=0, column=5, padx=(50,0), pady=10)

label_excluir = tk.Label(frame_lado, text="Id do Produto Para Exclusão:")
label_excluir.grid(row=2, column=2, padx=10, pady=10, sticky="w")

#BOTAO E INPUT PRA EXCLUIR ITEM
excluir = tk.Entry(frame_lado)
excluir.grid(row=3, column=2, padx=10, pady=10)
tk.Button(frame_lado, text="Excluir produto", command=lambda: [excluir_produto(), excluir.delete(0, tk.END)]).grid(row=4, column=2, padx=10, pady=10)

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
listar_produtos()

aba_estoque.mainloop()