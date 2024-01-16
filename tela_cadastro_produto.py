import json
import tkinter as tk
from tkinter import ttk, messagebox
from produto import Produto
from banco_dados import salvar_em_arquivo, carregar_de_arquivo


class TelaCadastroProduto:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastrar Produto")

        self.codigo_label = ttk.Label(root, text="Código:")
        self.codigo_label.grid(row=0, column=0, padx=10, pady=10)
        self.codigo_entry = ttk.Entry(root)
        self.codigo_entry.grid(row=0, column=1, padx=10, pady=10)

        self.nome_label = ttk.Label(root, text="Nome:")
        self.nome_label.grid(row=1, column=0, padx=10, pady=10)
        self.nome_entry = ttk.Entry(root)
        self.nome_entry.grid(row=1, column=1, padx=10, pady=10)

        self.preco_label = ttk.Label(root, text="Preço:")
        self.preco_label.grid(row=2, column=0, padx=10, pady=10)
        self.preco_entry = ttk.Entry(root)
        self.preco_entry.grid(row=2, column=1, padx=10, pady=10)

        self.cadastrar_button = ttk.Button(root, text="Cadastrar", command=self.cadastrar_produto)
        self.cadastrar_button.grid(row=3, column=0, columnspan=2, pady=10)

    def cadastrar_produto(self):
        codigo = self.codigo_entry.get()
        nome = self.nome_entry.get()
        preco = float(self.preco_entry.get())

        produtos = carregar_de_arquivo('produtos.json')
        produtos.append(Produto(codigo, nome, preco).to_dict())
        salvar_em_arquivo(produtos, 'produtos.json')

        messagebox.showinfo("Cadastro", "Produto cadastrado com sucesso!")
        self.root.destroy()
        