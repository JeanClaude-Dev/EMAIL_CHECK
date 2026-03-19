import os
import json
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from pypdf import PdfReader
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# --- CONFIGURAÇÃO DA IA ---
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Debug: Lista os modelos disponíveis nos LOGS do Render para conferência
print("--- Verificando Modelos Disponíveis ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"Modelo Detectado: {m.name}")
except Exception as e:
    print(f"Não foi possível listar modelos: {e}")

# Definindo o modelo (Alterado para 1.5-pro para maior compatibilidade)
MODEL_NAME = 'gemini-1.5-pro'
model = genai.GenerativeModel(MODEL_NAME)

def extrair_texto_pdf(arquivo):
    try:
        leitor = PdfReader(arquivo)
        texto = ""
        for pagina in leitor.pages:
            content = pagina.extract_text()
            if content:
                texto += content
        return texto
    except Exception as e:
        return f"Erro ao ler PDF: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    texto_final = ""

    # 1. Captura de Arquivos
    if 'arquivo' in request.files:
        arquivo = request.files['arquivo']
        if arquivo.filename != '':
            if arquivo.filename.endswith('.pdf'):
                texto_final = extrair_texto_pdf(arquivo)
            elif arquivo.filename.endswith('.txt'):
                texto_final = arquivo.read().decode('utf-8')
    
    # 2. Captura de Texto Manual (se não houver arquivo)
    if not texto_final:
        texto_final = request.form.get('texto', '')

    if not texto_final:
        return jsonify({"error": "Nenhum conteúdo para analisar"}), 400

    try:
        # Prompt rigoroso para JSON
        prompt = (
            "Analise este e-mail corporativo. "
            "Responda APENAS um objeto JSON puro, sem markdown, com estas chaves: "
            "'categoria' (Produtivo/Improdutivo), 'justificativa', 'resposta_sugerida'. "
            f"Texto: {texto_final}"
        )

        response = model.generate_content(prompt)
        
        # Limpeza de possíveis blocos de código markdown
        raw_text = response.text
        clean_json = raw_text.replace('```json', '').replace('```', '').strip()
        
        return jsonify(json.loads(clean_json))

    except Exception as e:
        print(f"ERRO NA IA: {str(e)}")
        return jsonify({"error": f"Erro na API Gemini: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)