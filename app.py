from flask import Flask, request, jsonify
from langchain.document_loaders import PyPDFLoader
import preprocessPDF
import generateQuiz
from flask_cors import CORS, cross_origin 

app = Flask(__name__)
CORS(app)
def readPDF(pdfFilename):
    loader = PyPDFLoader(pdfFilename)
    data = loader.load()
    book = ""
    for x in data:
        book += x.page_content
    return book

@app.route("/api",methods=['GET'])
@cross_origin()
def index():
    return {
        "tutorial":"hello"
    } 

@app.route('/chunks', methods=['POST'])
def process_pdf():
    data = request.get_json()  # Get JSON body of request
    pdf_name = data.get('pdfName')  # Extract pdfName from JSON

    # Ensure that a PDF name was provided
    if not pdf_name:
        return jsonify({'error': 'No PDF name provided'}), 400

    text = readPDF(pdf_name)
    chunks = preprocessPDF.text_to_doc(text)
    

    return jsonify(chunks), 200  # Returns JSON response
@app.route('/quiz', methods=['POST'])
def chunkQuiz():
    data = request.get_json()  # Get JSON body of request
    chunk = data.get('chunk')  # Extract chunk from JSON

    # Ensure that a chunk was provided
    if not chunk:
        return jsonify({'error': 'No PDF name provided'}), 400

    questions = generateQuiz.generate(chunk)
    
    

    return jsonify(questions), 200  # Returns JSON response

if __name__ == "__main__":
    app.run()  # run the app on port 5000