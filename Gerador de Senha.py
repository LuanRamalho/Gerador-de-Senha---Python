import tkinter as tk
import random
import string

def gerar_senha():
    tamanho = int(entry_tamanho.get())
    tipo_senha = var_tipo_senha.get()
    
    if tipo_senha == "letras":
        caracteres = string.ascii_letters
    elif tipo_senha == "numeros":
        caracteres = string.digits
    elif tipo_senha == "todos":
        caracteres = string.ascii_letters + string.digits + string.punctuation
    else:
        resultado.set("Selecione um tipo de senha.")
        return
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    resultado.set(senha)
    entry_senha.delete(0, tk.END)  # Limpa a caixa de texto antes de inserir a nova senha
    entry_senha.insert(0, senha)  # Insere a nova senha na caixa de texto

# Criação da janela principal
janela = tk.Tk()
janela.title("Gerador de Senha")
janela.geometry("400x300")  # Define o tamanho da janela
janela.config(bg="#f0f8ff")  # Cor de fundo suave

# Configuração da entrada para o tamanho da senha
label_tamanho = tk.Label(janela, text="Tamanho da senha:", font=("Arial", 12), bg="#f0f8ff", fg="#4b0082")
label_tamanho.pack(pady=10)

entry_tamanho = tk.Entry(janela, font=("Arial", 12), width=20, bd=2, relief="solid", justify="center")
entry_tamanho.pack(pady=5)

# Variável para tipo de senha
var_tipo_senha = tk.StringVar(value="letras")

# Opções para tipo de senha
radio_letras = tk.Radiobutton(janela, text="Somente letras", variable=var_tipo_senha, value="letras", font=("Arial", 12), bg="#f0f8ff", fg="#4b0082", selectcolor="#e0e0e0", activebackground="#e0e0e0")
radio_letras.pack()

radio_numeros = tk.Radiobutton(janela, text="Somente números", variable=var_tipo_senha, value="numeros", font=("Arial", 12), bg="#f0f8ff", fg="#4b0082", selectcolor="#e0e0e0", activebackground="#e0e0e0")
radio_numeros.pack()

radio_todos = tk.Radiobutton(janela, text="Letras, números e caracteres especiais", variable=var_tipo_senha, value="todos", font=("Arial", 12), bg="#f0f8ff", fg="#4b0082", selectcolor="#e0e0e0", activebackground="#e0e0e0")
radio_todos.pack()

# Botão para gerar a senha
botao_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_senha, font=("Arial", 12, "bold"), bg="#4b0082", fg="#ffffff", relief="raised", bd=4)
botao_gerar.pack(pady=15)

# Caixa de texto para mostrar a senha gerada
entry_senha = tk.Entry(janela, width=40, font=("Arial", 12), bd=2, relief="solid", justify="center")
entry_senha.pack(pady=5)

# Label para mostrar mensagens
resultado = tk.StringVar()

# Execução da interface
janela.mainloop()
