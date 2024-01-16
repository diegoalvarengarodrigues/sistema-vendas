import json
import tkinter as tk
from tkinter import ttk, messagebox
from venda import Venda
from cliente import Cliente
from produto import Produto
from vendedor import Vendedor
from banco_dados import carregar_de_arquivo, salvar_em_arquivo

class TelaVenda:
    def __init__(self, root):
        self.root = root
        self.root.title("Realizar Venda")

        self.clientes = carregar_de_arquivo('clientes.json')
        self.vendedores = carregar_de_arquivo('vendedores.json')
        self.produtos = carregar_de_arquivo('produtos.json')

        self.cliente_label = ttk.Label(root, text="Cliente:")
        self.cliente_label.grid(row=0, column=0, padx=10, pady=10)
        self.cliente_var = tk.StringVar(root)
        self.cliente_combobox = ttk.Combobox(root, textvariable=self.cliente_var, values=[cliente['nome'] for cliente in self.clientes])
        self.cliente_combobox.grid(row=0, column=1, padx=10, pady=10)

        self.vendedor_label = ttk.Label(root, text="Vendedor:")
        self.vendedor_label.grid(row=1, column=0, padx=10, pady=10)
        self.vendedor_var = tk.StringVar(root)
        self.vendedor_combobox = ttk.Combobox(root, textvariable=self.vendedor_var, values=[vendedor['nome'] for vendedor in self.vendedores])
        self.vendedor_combobox.grid(row=1, column=1, padx=10, pady=10)

        self.produtos_label = ttk.Label(root, text="Produtos:")
        self.produtos_label.grid(row=2, column=0, padx=10, pady=10)
        self.produtos_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=4)
        for produto in self.produtos:
            self.produtos_listbox.insert(tk.END, produto['nome'])
        self.produtos_listbox.grid(row=2, column=1, padx=10, pady=10)

        self.realizar_venda_button = ttk.Button(root, text="Realizar Venda", command=self.realizar_venda)
        self.realizar_venda_button.grid(row=3, column=0, columnspan=2, pady=10)

    def realizar_venda(self):
        try:
            cliente_index = self.cliente_combobox.current()
            vendedor_index = self.vendedor_combobox.current()
            selected_products_indices = self.produtos_listbox.curselection()

            if cliente_index == -1 or vendedor_index == -1 or not selected_products_indices:
                messagebox.showwarning("Aviso", "Por favor, selecione cliente, vendedor e pelo menos um produto.")
                return

            cliente = Cliente(**self.clientes[cliente_index])
            vendedor = Vendedor(**self.vendedores[vendedor_index])

            venda = Venda(cliente, vendedor)

            for index in selected_products_indices:
                produto = Produto(**self.produtos[index])
                venda.adicionar_produto(produto)

            vendas = carregar_de_arquivo('vendas.json')
            vendas.append({
                'cliente': cliente.to_dict(),
                'vendedor': vendedor.to_dict(),
                'produtos': [produto.to_dict() for produto in venda.produtos],
                'total': venda.calcular_total(),
                'forma_pagamento': "Dinheiro"
            })
            salvar_em_arquivo(vendas, 'vendas.json')

            cupom = venda.emitir_cupom_fiscal("Dinheiro")

            messagebox.showinfo("Cupom Fiscal", cupom)
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao finalizar a venda:\n{str(e)}")