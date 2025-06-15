from flask import Flask, request, jsonify
import PyPDF2

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    # Dummy quiz logic (just to test)
    question = "What is mentioned in the PDF?"
    return jsonify({"quiz": [{"question": question, "context": text[:200]}]})
  
