import os
import json
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from pypdf import PdfReader
from dotenv import load_dotenv



load_dotenv()
app = Flask(__name__)

# Configuração da IA
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#model = genai.GenerativeModel('gemini-1.5-flash')
#model = genai.GenerativeModel(model_name='gemini-1.5-flash')
#model = genai.GenerativeModel('gemini-1.0-pro')


try:
    model = genai.GenerativeModel('gemini-1.5-flash')
    # Teste rápido para validar o modelo
    print("Modelo Gemini 1.5 Flash carregado com sucesso.")
except:
    model = genai.GenerativeModel('gemini-1.0-pro')
    print("Usando Gemini 1.0 Pro como fallback.")







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

    if 'arquivo' in request.files:
        arquivo = request.files['arquivo']
        if arquivo.filename == '':
            return jsonify({"error": "Arquivo sem nome"}), 400
        
        if arquivo.filename.endswith('.pdf'):
            texto_final = extrair_texto_pdf(arquivo)
        elif arquivo.filename.endswith('.txt'):
            texto_final = arquivo.read().decode('utf-8')
    else:
        texto_final = request.form.get('texto', '')

    if not texto_final:
        return jsonify({"error": "Nenhum conteúdo encontrado"}), 400

    try:
        # Prompt otimizado para garantir JSON puro
        prompt = f"Analise o email/documento e responda EXATAMENTE no formato JSON: {texto_final}"
        response = model.generate_content(prompt)
        
        # Limpeza de markdown
        resultado_limpo = response.text.replace('```json', '').replace('```', '').strip()
        
        return jsonify(json.loads(resultado_limpo))
    except Exception as e:
        print(f"Erro detectado: {e}") # Isso ajuda a ver o erro nos logs do Render
        return jsonify({"error": str(e)}), 500

# --- ESTA PARTE É ESSENCIAL PARA O RENDER ---
if __name__ == '__main__':
    # O Render exige que o host seja 0.0.0.0 e a porta venha da variável de ambiente
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)