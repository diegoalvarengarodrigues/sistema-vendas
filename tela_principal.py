import tkinter as tk
from tkinter import ttk
from tela_cadastro_cliente import TelaCadastroCliente
from tela_cadastro_vendedor import TelaCadastroVendedor
from tela_cadastro_produto import TelaCadastroProduto
from tela_venda import TelaVenda


class TelaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Vendas - Mercadinho")
        self.root.iconbitmap('market.ico')
        
        frame_principal = ttk.Frame(root)
        frame_principal.grid(row=0, column=0)
        
        imagem = tk.PhotoImage(file='D:\Vendas\logo.png')  # Substitua 'logo.png' pelo caminho da sua imagem
        label_imagem = ttk.Label(frame_principal, image=imagem)
        label_imagem.grid(row=0, column=0, columnspan=3, pady=20)

        self.cadastrar_cliente_button = ttk.Button(frame_principal, text="Cadastrar Cliente", command=self.abrir_cadastro_cliente, style="TButton")
        self.cadastrar_cliente_button.grid(row=1, column=0, padx=10, pady=10)

        self.cadastrar_vendedor_button = ttk.Button(frame_principal, text="Cadastrar Vendedor", command=self.abrir_cadastro_vendedor, style="TButton")
        self.cadastrar_vendedor_button.grid(row=1, column=1, padx=10, pady=10)

        self.cadastrar_produto_button = ttk.Button(frame_principal, text="Cadastrar Produto", command=self.abrir_cadastro_produto, style="TButton")
        self.cadastrar_produto_button.grid(row=1, column=2, padx=10, pady=10)

        self.realizar_venda_button = ttk.Button(frame_principal, text="Realizar Venda", command=self.abrir_realizar_venda, style="TButton")
        self.realizar_venda_button.grid(row=2, column=0, columnspan=3, pady=10)

        self.sair_button = ttk.Button(frame_principal, text="Sair", command=root.destroy, style="TButton")
        self.sair_button.grid(row=3, column=0, columnspan=3, pady=10)

        # Configurar estilo para os botões
        style = ttk.Style()
        style.configure("TButton", foreground="#0000CD", background="#87CEFA", font=('Arial', 14))

    def abrir_cadastro_cliente(self):
        cadastro_cliente_window = tk.Toplevel(self.root)
        cadastro_cliente = TelaCadastroCliente(cadastro_cliente_window)

    def abrir_cadastro_vendedor(self):
        cadastro_vendedor_window = tk.Toplevel(self.root)
        cadastro_vendedor = TelaCadastroVendedor(cadastro_vendedor_window)

    def abrir_cadastro_produto(self):
        cadastro_produto_window = tk.Toplevel(self.root)
        cadastro_produto = TelaCadastroProduto(cadastro_produto_window)

    def abrir_realizar_venda(self):
        realizar_venda_window = tk.Toplevel(self.root)
        realizar_venda = TelaVenda(realizar_venda_window)
