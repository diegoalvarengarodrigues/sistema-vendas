from tkinter import ttk, messagebox
from vendedor import Vendedor
from banco_dados import carregar_de_arquivo, salvar_em_arquivo


class TelaCadastroVendedor:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastrar Vendedor")

        self.nome_label = ttk.Label(root, text="Nome:")
        self.nome_label.grid(row=0, column=0, padx=10, pady=10)
        self.nome_entry = ttk.Entry(root)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)

        self.cpf_label = ttk.Label(root, text="CPF:")
        self.cpf_label.grid(row=1, column=0, padx=10, pady=10)
        self.cpf_entry = ttk.Entry(root)
        self.cpf_entry.grid(row=1, column=1, padx=10, pady=10)

        self.salario_label = ttk.Label(root, text="Salário:")
        self.salario_label.grid(row=2, column=0, padx=10, pady=10)
        self.salario_entry = ttk.Entry(root)
        self.salario_entry.grid(row=2, column=1, padx=10, pady=10)

        self.cadastrar_button = ttk.Button(root, text="Cadastrar", command=self.cadastrar_vendedor)
        self.cadastrar_button.grid(row=3, column=0, columnspan=2, pady=10)

    def cadastrar_vendedor(self):
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        salario = float(self.salario_entry.get())

        vendedores = carregar_de_arquivo('vendedores.json')
        vendedores.append(Vendedor(nome, cpf, salario).to_dict())
        salvar_em_arquivo(vendedores, 'vendedores.json')

        messagebox.showinfo("Cadastro", "Vendedor cadastrado com sucesso!")
        self.root.destroy()