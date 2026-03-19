# 📧 AI Email Classifier - Desafio Setor Financeiro

Esta aplicação utiliza Inteligência Artificial (Google Gemini API) para classificar automaticamente emails recebidos em **Produtivos** ou **Improdutivos**, sugerindo uma resposta imediata para otimizar o fluxo de trabalho.

## 🚀 Tecnologias Utilizadas
- **Backend:** Python & Flask
- **IA:** Google Generative AI (Gemini 1.5 Flash)
- **Frontend:** HTML5 & Tailwind CSS
- **Deploy:** Render / Vercel

## ⚙️ Como Executar Localmente
1. Clone o repositório: `git clone https://github.com/seu-usuario/seu-repositorio.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Crie um arquivo `.env` e adicione sua chave: `GEMINI_API_KEY=sua_chave_aqui`
4. Execute: `python app.py`
5. Acesse: `http://127.0.0.1:5000`

## 🧠 Lógica de IA
O sistema utiliza **Zero-Shot Prompting**. O texto do email é enviado ao modelo Gemini com instruções específicas de categorização baseadas no contexto financeiro. O modelo retorna um JSON estruturado com a classe e a sugestão de resposta, garantindo agilidade no processamento.

=====================================================================================

# 📧 AI Email Classifier & Triage 

Este é um projeto de inteligência artificial desenvolvido para realizar a triagem automática de e-mails corporativos. Utilizando o modelo **Gemini 1.5 Flash** do Google, o sistema classifica mensagens como "Produtivas" ou "Improdutivas", gera justificativas e sugere respostas automáticas.

---

## 🚀 Funcionalidades

* **Processamento Multimodal**: Aceita entrada de texto manual ou upload de arquivos (**PDF** e **TXT**).
* **Análise Inteligente**: Classificação baseada em contexto para separar spam/ruído de comunicações importantes.
* **Sugestão de Resposta**: Gera uma resposta educada e contextualizada para o e-mail analisado.
* **Interface Moderna**: UI responsiva construída com **Tailwind CSS** e funcionalidade **Drag & Drop**.
* **Deploy Pronto**: Configurado para rodar no **Render.com**.

---

## 🛠️ Tecnologias Utilizadas

* **Backend**: [Python 3.10+](https://www.python.org/)
* **Framework Web**: [Flask](https://flask.palletsprojects.com/)
* **IA Generativa**: [Google Gemini API](https://ai.google.dev/)
* **Processamento de PDF**: [pyPDF](https://pypdf.readthedocs.io/)
* **Frontend**: HTML5, JavaScript (ES6+), Tailwind CSS.
* **Servidor de Produção**: Gunicorn.

---

## 📦 Como Instalar e Rodar
1. git clone: [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
2. Instale as dependências: `pip install -r requirements.txt`
3. Crie um arquivo `.env` e adicione sua chave: `GEMINI_API_KEY=sua_chave_aqui`
4. Execute: `python app.py`
5. Acesse: `http://127.0.0.1:5000`
