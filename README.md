# 🌤 Consulta de Clima e Endereço (CEP) - Python + Tkinter + APIs

Projeto desenvolvido em Python com interface gráfica usando Tkinter, que permite consultar o clima atual de qualquer cidade e o endereço completo de um CEP brasileiro, consumindo APIs públicas em tempo real.

---

## ✅ Funcionalidades

- 🔹 Consulta de endereço completo a partir do CEP (ViaCEP)
- 🔹 Consulta de clima atual por cidade (OpenWeatherMap)
- 🔹 Exibição de temperatura, clima, umidade e data/hora da consulta
- 🔹 Ícone do clima exibido junto da previsão
- 🔹 Interface gráfica simples e funcional com Tkinter
- 🔹 Botão para limpar campos
- 🔹 Tratamento de erros e validação de entrada

---

## 🛠 Tecnologias utilizadas

- Python 3
- Tkinter (GUI)
- `requests` (requisições HTTP)
- `Pillow` (exibição de ícones de clima)
- API ViaCEP (https://viacep.com.br)
- API OpenWeatherMap (https://openweathermap.org)

---

## ▶️ Como executar

### 1. Clone o repositório

git clone https://github.com/lucascordeiroo/consulta-api.git
cd consulta-api

2. Instale as dependências
pip install requests pillow

4. Obtenha uma chave da API OpenWeatherMap
Acesse: https://openweathermap.org/api
Crie uma conta gratuita
Copie sua chave da API
Cole no código (app.py) na linha onde está:

api_key = "SUA_CHAVE_AQUI"

4. Execute o aplicativo
python app.py
🧪 Exemplo de uso
CEP: 01001000 → mostra Praça da Sé - São Paulo/SP

Cidade: Belo Horizonte → mostra temperatura, clima, umidade e ícone

📂 Estrutura do projeto
consulta-api/
├── app.py         # Código principal
└── README.md      # Descrição do projeto

👨‍💻 Autor
Desenvolvido por Lucas Cordeiro
📧 lucascordeirooliveira50@gmail.com
🔗 https://github.com/lucascordeiroo

📄 Licença
Este projeto está sob a licença MIT — sinta-se livre para usar e modificar.
