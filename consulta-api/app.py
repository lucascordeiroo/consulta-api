import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime
from PIL import Image, ImageTk
from io import BytesIO

api_key = "f40d03c874b82835fedce0d7ff1d9fe0"

# Função: Buscar endereço por CEP
def buscar_endereco():
    cep = entry_cep.get().strip()
    if len(cep) != 8 or not cep.isdigit():
        messagebox.showwarning("CEP inválido", "Digite um CEP válido com 8 números.")
        return

    try:
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        dados = resposta.json()

        if "erro" in dados:
            resultado_cep.config(text="CEP não encontrado.")
        else:
            endereco = f"{dados['logradouro']} - {dados['bairro']} - {dados['localidade']}/{dados['uf']}"
            resultado_cep.config(text=endereco)
    except:
        resultado_cep.config(text="Erro ao consultar o CEP.")

# Função: Buscar clima por cidade
def buscar_clima():
    cidade = entry_cidade.get().strip()
    if not cidade:
        messagebox.showwarning("Campo vazio", "Digite o nome de uma cidade.")
        return

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"
        resposta = requests.get(url)
        dados = resposta.json()

        if dados.get("cod") != 200:
            resultado_clima.config(text="Cidade não encontrada.")
            icone_clima.config(image="")  # remove o ícone anterior
            return

        temp = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"]
        umidade = dados["main"]["humidity"]
        data_hora = datetime.now().strftime('%d/%m/%Y %H:%M')

        resultado = f"{cidade.title()} | {temp}°C | {descricao} | Umidade: {umidade}% | {data_hora}"
        resultado_clima.config(text=resultado)

        # Ícone do clima
        codigo_icone = dados["weather"][0]["icon"]
        url_icone = f"http://openweathermap.org/img/wn/{codigo_icone}@2x.png"
        imagem = Image.open(BytesIO(requests.get(url_icone).content))
        imagem = imagem.resize((50, 50))
        imagem_tk = ImageTk.PhotoImage(imagem)
        icone_clima.image = imagem_tk
        icone_clima.config(image=imagem_tk)

    except:
        resultado_clima.config(text="Erro ao consultar o clima.")
        icone_clima.config(image="")

# Função: limpar campos
def limpar_campos():
    entry_cep.delete(0, tk.END)
    entry_cidade.delete(0, tk.END)
    resultado_cep.config(text="")
    resultado_clima.config(text="")
    icone_clima.config(image="")

# Interface
root = tk.Tk()
root.title("Consulta de Clima e Endereço")
root.geometry("500x550")
root.resizable(False, False)

# ---- Consulta CEP ----
frame_cep = tk.LabelFrame(root, text="Consulta de Endereço por CEP", padx=10, pady=10)
frame_cep.pack(fill="x", padx=20, pady=10)

tk.Label(frame_cep, text="CEP:").pack()
entry_cep = tk.Entry(frame_cep)
entry_cep.pack()
tk.Button(frame_cep, text="Buscar Endereço", command=buscar_endereco).pack(pady=5)
resultado_cep = tk.Label(frame_cep, text="", fg="blue")
resultado_cep.pack()

# ---- Consulta Clima ----
frame_clima = tk.LabelFrame(root, text="Consulta de Clima por Cidade", padx=10, pady=10)
frame_clima.pack(fill="x", padx=20, pady=10)

tk.Label(frame_clima, text="Cidade:").pack()
entry_cidade = tk.Entry(frame_clima)
entry_cidade.pack()
tk.Button(frame_clima, text="Buscar Clima", command=buscar_clima).pack(pady=5)
resultado_clima = tk.Label(frame_clima, text="", fg="green", wraplength=450)
resultado_clima.pack()
icone_clima = tk.Label(frame_clima)
icone_clima.pack(pady=5)

# ---- Ações ----
frame_acoes = tk.Frame(root)
frame_acoes.pack(pady=10)
tk.Button(frame_acoes, text="Limpar Campos", command=limpar_campos).pack()

# ---- Rodapé ----
footer = tk.Label(root, text="Desenvolvido por Lucas Cordeiro | 2025", font=("Arial", 8), fg="gray")
footer.pack(pady=10)

root.mainloop()
