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