import os
import json
from flask import Flask, render_template, request, jsonify
from groq import Groq
from pypdf import PdfReader
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def extrair_texto_pdf(arquivo):
    try:
        leitor = PdfReader(arquivo)
        texto = ""
        for pagina in leitor.pages:
            content = pagina.extract_text()
            if content: texto += content
        return texto
    except Exception as e:
        return f"Erro no PDF: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    texto_final = ""

    if 'arquivo' in request.files:
        arquivo = request.files['arquivo']
        if arquivo.filename != '':
            if arquivo.filename.endswith('.pdf'):
                texto_final = extrair_texto_pdf(arquivo)
            elif arquivo.filename.endswith('.txt'):
                texto_final = arquivo.read().decode('utf-8')
    
    if not texto_final:
        texto_final = request.form.get('texto', '')

    if not texto_final:
        return jsonify({"error": "Conteúdo vazio"}), 400

    try:
        # Chamada ao modelo Llama 3.3 via Groq com Few-Shot Prompting
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system", 
                    "content": """Você é um especialista em triagem de e-mails corporativos.
                    Sua tarefa é classificar o conteúdo em:
                    - **Produtivo**: E-mails que solicitam ações, dúvidas, agendamentos ou documentos.
                    - **Improdutivo**: Spams, correntes, agradecimentos vazios ou propagandas.
                    Responda APENAS em JSON puro com as chaves: categoria, justificativa e resposta_sugerida."""
                },
                # Exemplos para "treinar"  
                {
                    "role": "user", 
                    "content": "Texto: 'Ganhe 50% de desconto em sapatos agora!'"
                },
                {
                    "role": "assistant", 
                    "content": '{"categoria": "Improdutivo", "justificativa": "Propaganda comercial não solicitada.", "resposta_sugerida": "Nenhum retorno necessário."}'
                },
                {
                    "role": "user", 
                    "content": "Texto: 'Segue em anexo o relatório financeiro de março para revisão.'"
                },
                {
                    "role": "assistant", 
                    "content": '{"categoria": "Produtivo", "justificativa": "Envio de documento de trabalho que exige análise.", "resposta_sugerida": "Recebido. Vou analisar e retorno em breve."}'
                },
                # Entrada usuário
                {
                    "role": "user", 
                    "content": f"Analise este conteúdo: {texto_final}"
                }
            ]
        )
        
        resultado = chat_completion.choices[0].message.content
        return jsonify(json.loads(resultado))

    except Exception as e:
        return jsonify({"error": f"Erro no Groq: {str(e)}"}), 500

if __name__ == '__main__':
    # Configuração para deploy (Render) ou rodar localmente
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)