import json
import tkinter as tk
from tkinter import ttk, messagebox
from cliente import Cliente
from banco_dados import carregar_de_arquivo, salvar_em_arquivo

class TelaCadastroCliente:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastrar Cliente")

        self.nome_label = ttk.Label(root, text="Nome:")
        self.nome_label.grid(row=0, column=0, padx=10, pady=10)
        self.nome_entry = ttk.Entry(root)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)

        self.cpf_label = ttk.Label(root, text="CPF:")
        self.cpf_label.grid(row=1, column=0, padx=10, pady=10)
        self.cpf_entry = ttk.Entry(root)
        self.cpf_entry.grid(row=1, column=1, padx=10, pady=10)

        self.endereco_label = ttk.Label(root, text="Endereço:")
        self.endereco_label.grid(row=2, column=0, padx=10, pady=10)
        self.endereco_entry = ttk.Entry(root)
        self.endereco_entry.grid(row=2, column=1, padx=10, pady=10)

        self.cadastrar_button = ttk.Button(root, text="Cadastrar", command=self.cadastrar_cliente)
        self.cadastrar_button.grid(row=3, column=0, columnspan=2, pady=10)
        

    def cadastrar_cliente(self):
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        endereco = self.endereco_entry.get()

        clientes = carregar_de_arquivo('clientes.json')
        clientes.append(Cliente(nome, cpf, endereco).to_dict())
        salvar_em_arquivo(clientes, 'clientes.json')

        messagebox.showinfo("Cadastro", "Cliente cadastrado com sucesso!")
        self.root.destroy()