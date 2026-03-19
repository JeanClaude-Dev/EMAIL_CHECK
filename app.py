import os
import json
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuração da API
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
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
        resultado_bruto = classificar_e_responder(texto)
        
        # Limpa blocos de código markdown se existirem
        resultado_limpo = resultado_bruto.replace('```json', '').replace('```', '').strip()
        
        # Converte para dicionário para garantir que o retorno seja JSON válido
        dados_json = json.loads(resultado_limpo)
        return jsonify(dados_json)
        
    except Exception as e:
        print(f"Erro no processamento: {e}") # Aparecerá nos logs do Render
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Configuração vital para o Render reconhecer a porta
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)