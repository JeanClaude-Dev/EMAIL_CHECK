# 📧 Classificador de E-mails IA – Triagem Inteligente

Este projeto é um sistema de triagem inteligente que utiliza Inteligência Artificial para analisar o conteúdo de e-mails ou arquivos (PDF/TXT) e classificá-los como **Produtivo** ou **Improdutivo**. Ele fornece uma justificativa detalhada para a classificação e uma sugestão de resposta automática baseada no contexto analisado.

## 🚀 Tecnologias Utilizadas

* **Backend:** Python com o micro-framework **Flask**.
* **IA/LLM:** **Llama 3.3-70b-versatile** via API da **Groq**.
* **Frontend:** HTML5 e CSS3 moderno (interface responsiva e intuitiva).
* **Processamento de Arquivos:** Biblioteca pypdf para extração de texto de documentos PDF.

## 🛠️ Funcionalidades

* **Entrada de Texto:** Campo dedicado para colar o conteúdo do e-mail manualmente.
* **Upload de Documentos:** Suporte nativo para análise de arquivos nos formatos .pdf e .txt.
* **Análise em Tempo Real:** Classificação instantânea utilizando modelos de linguagem de larga escala (LLM).
* **Feedback Visual:** Interface que altera cores e estilos conforme o resultado (verde para produtivo, vermelho para improdutivo).

## 📋 Pré-requisitos

Para rodar este projeto localmente, você precisará de:
* **Python 3.8+** instalado.
* Uma chave de API da [Groq Cloud](https://console.groq.com/).

## 🔧 Instalação e Configuração

1.  **Clone o repositório:**
     clone:(https://github.com/JeanClaude-Dev/EMAIL_CHECK.git)
   

2.  **Instale as dependências necessárias:**
    pip install flask groq pypdf python-dotenv
    

3.  **Configure as variáveis de ambiente:**
    Crie um arquivo .env na raiz do projeto e insira sua chave da Groq:  GROQ_API_KEY=sua_chave_aqui
    

4.  **Inicie o servidor local:**
    python app.py
    

5.  **Acesse a aplicação:**
    Abra o navegador em `http://127.0.0.1:5000`

## 📁 Estrutura do Projeto

* app.py: Lógica do servidor Flask e integração com a API Llama 3.3.
* templates/index.html: Interface do usuário estilizada com CSS nativo.
* static/: Pasta para armazenar ativos estáticos (como o banner do projeto).

**Desenvolvido por Jean-Claude**
