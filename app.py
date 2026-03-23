import os
import json
from flask import Flask, render_template, request, jsonify
from groq import Groq
from pypdf import PdfReader
from dotenv import load_dotenv

# Carrega variáveis de ambiente (.env)
load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def extrair_texto_pdf(arquivo):
    """Extrai texto de um arquivo PDF enviado."""
    try:
        leitor = PdfReader(arquivo)
        texto = ""
        for pagina in leitor.pages:
            content = pagina.extract_text()
            if content:
                texto += content
        return texto
    except Exception as e:
        return f"Erro ao processar PDF: {str(e)}"

@app.route('/')
def index():
    """Rota principal que serve o seu index.html."""
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    """Rota que recebe os dados da interface e consulta a IA."""
    texto_final = ""
    
    # Verifica se há um arquivo ou texto manual
    if 'arquivo' in request.files:
        arquivo = request.files['arquivo']
        if arquivo.filename.endswith('.pdf'):
            texto_final = extrair_texto_pdf(arquivo)
        elif arquivo.filename.endswith('.txt'):
            texto_final = arquivo.read().decode('utf-8')
    else:
        texto_final = request.form.get('texto', '')

    if not texto_final:
        return jsonify({"error": "Conteúdo vazio ou inválido"}), 400

    try:
        # Chamada ao modelo Llama 
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

        resultado_ia = json.loads(chat_completion.choices[0].message.content)
        return jsonify(resultado_ia)

    except Exception as e:
        return jsonify({"error": f"Erro na IA: {str(e)}"}), 500

if __name__ == "__main__":
    # Porta padrão para o Render (usa a variável de ambiente PORT)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)