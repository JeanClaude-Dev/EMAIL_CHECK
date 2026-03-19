import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure sua API KEY do Google Gemini aqui ou no arquivo .env
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def classificar_e_responder(texto_email):
    prompt = f"""
    Atue como um assistente de triagem de emails corporativos.
    Analise o email abaixo e responda EXATAMENTE no formato JSON:
    {{
        "categoria": "Produtivo" ou "Improdutivo",
        "justificativa": "breve explicação",
        "resposta_sugerida": "uma sugestão de resposta educada"
    }}

    Email: {texto_email}
    """
    response = model.generate_content(prompt)
    return response.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    data = request.json
    texto = data.get('texto', '')
    
    if not texto:
        return jsonify({"error": "Texto vazio"}), 400

    try:
        # Chamada para a IA
        resultado_bruto = classificar_e_responder(texto)
        # Limpeza simples caso a IA retorne markdown
        resultado_limpo = resultado_bruto.replace('```json', '').replace('```', '').strip()
        return resultado_limpo
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)