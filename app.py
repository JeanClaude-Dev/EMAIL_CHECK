import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure sua API KEY no arquivo .env
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def classificar_e_responder(texto_email):
    prompt = f"""
    Atue como um assistente de triagem de emails corporativos.
    Analise o email abaixo e responda EXATAMENTE no formato JSON:
    {{
        "categoria": "Produtivo" ou "Improdutivo",
        "justificativa": "breve explicação",
        "resposta_sugerida": "Resposta sugerida"
    }}

    Email: {texto_email}
    """
    response = model.generate_content(prompt)
    return response.text

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)



import json 

@app.route('/processar', methods=['POST'])
def processar():
    data = request.json
    texto = data.get('texto', '')
    
    if not texto:
        return jsonify({"error": "Texto vazio"}), 400

    try:
        resultado_bruto = classificar_e_responder(texto)
        # Limpa os marcadores de Markdown
        resultado_limpo = resultado_bruto.replace('```json', '').replace('```', '').strip()
        
        # Converte a string Python real
        dados_json = json.loads(resultado_limpo)
        
        return jsonify(dados_json) # Retorna como JSON puro 
    except Exception as e:
        print(f"Erro no servidor: {e}") 
        return jsonify({"error": "Falha ao processar o email. Verifique a API Key."}), 500