# 📧 Classificador Inteligente de E-mails com IA

Este projeto é uma aplicação web interativa que utiliza Inteligência Artificial para analisar conteúdos de e-mails ou documentos e classificá-los como **Produtivo** ou **Improdutivo**.

Além da classificação, o sistema fornece:

* 📌 Justificativa da decisão
* 💬 Sugestão de resposta automática baseada no contexto

---

## 🚀 Funcionalidades

* ✍️ **Entrada manual de texto**
* 📄 **Upload de arquivos (.pdf e .txt)**
* ⚡ **Análise em tempo real com IA**
* 🎯 **Classificação automática inteligente**
* 📊 **Resposta estruturada em JSON**
* 🎨 Interface simples e interativa com feedback visual

---

## 🧠 Tecnologias Utilizadas

* **Python**
* **Streamlit** (interface web)
* **Groq API** (LLM - Llama 3.3)
* **PyPDF** (leitura de PDFs)
* **python-dotenv** (variáveis de ambiente)

---

## 📂 Estrutura do Projeto

```id="a1x92p"
.
├── app.py
├── requirements.txt
└── README.md
```

---

## 📋 Pré-requisitos

Antes de começar, você precisa ter:

* Python **3.8 ou superior**
* Uma chave de API da Groq
  👉 https://console.groq.com/

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash id="b3k21f"
git clone https://github.com/JeanClaude-Dev/EMAIL_CHECK.git
cd EMAIL_CHECK
```

---

### 2. Instale as dependências

```bash id="c8m44z"
pip install -r requirements.txt
```

---

### 3. Configure a variável de ambiente

Crie um arquivo `.env` na raiz do projeto:

GROQ_API_KEY=sua_chave_aqui

---

## ▶️ Como Executar

```bash id="e9v11n"
streamlit run app.py
```

O aplicativo estará disponível em:

http://localhost:8501


---

## ☁️ Deploy no Streamlit Cloud

Para publicar sua aplicação:

1. Faça upload do projeto no GitHub
2. Acesse o Streamlit Cloud
3. Conecte seu repositório
4. Configure os **Secrets**:

GROQ_API_KEY = sua_chave_aqui

---

## 📌 Como Usar

1. Faça upload de um arquivo **PDF ou TXT**
   **ou**
2. Cole o conteúdo do e-mail no campo de texto
3. Clique em **Processar**
4. Visualize o resultado da análise

---

## 📊 Exemplo de Saída

{
  "categoria": "Produtivo",
  "justificativa": "Solicitação de análise de documento.",
  "resposta_sugerida": "Recebido. Vou verificar e retorno em breve."
}

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

## 👨‍💻 Autor

Desenvolvido por **Jean Claude** 🚀
