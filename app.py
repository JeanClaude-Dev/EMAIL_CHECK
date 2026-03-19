import os
import json
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from pypdf import PdfReader
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def extrair_texto_pdf(arquivo):
    leitor = PdfReader(arquivo)
    texto = ""
    for pagina in leitor.pages:
        texto += pagina.extract_text()
    return texto

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    texto_final = ""

    # Verifica se foi enviado um arquivo
    if 'arquivo' in request.files:
        arquivo = request.files['arquivo']
        if arquivo.filename == '':
            return jsonify({"error": "Arquivo sem nome"}), 400
        
        if arquivo.filename.endswith('.pdf'):
            texto_final = extrair_texto_pdf(arquivo)
        elif arquivo.filename.endswith('.txt'):
            texto_final = arquivo.read().decode('utf-8')
    
    # Se não for arquivo, tenta pegar o texto do formulário
    else:
        texto_final = request.form.get('texto', '')

    if not texto_final:
        return jsonify({"error": "Nenhum conteúdo encontrado"}), 400

    try:
        
        prompt = f"Analise o email/documento e responda em JSON: {texto_final}"
        response = model.generate_content(prompt)
        resultado_limpo = response.text.replace('```json', '').replace('```', '').strip()
        return jsonify(json.loads(resultado_limpo))
    except Exception as e:
        return jsonify({"error": str(e)}), 500