from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
import openai
import spacy

main = Blueprint('main', __name__)

# Directory to save uploaded files
# We can move towards databases once we get a working model in the local developement.
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize NLP model
nlp = spacy.load('en_core_web_sm')

# Setup OpenAI API key.
# Note: I just set this code up keeping openai in mind. We can have a consesus regarding what AI opensource models must be used.
openai.api_key = 'your_openai_api_key_here'

@main.route('/process-transcript', methods=['POST'])
def process_transcript():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)
    
    # Read the content of the uploaded file
    with open(file_path, 'r') as f:
        transcript = f.read()
    
    # Summarize the transcript
    summary = summarize_text(transcript)

    # Extract key points related to specific PM topics
    key_points = extract_key_points(transcript)

    return jsonify({
        'message': f'File {filename} processed successfully',
        'summary': summary,
        'key_points': key_points
    }), 200

def summarize_text(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following text:\n\n{text}\n\nSummary:",
        max_tokens=150,
        temperature=0.5
    )
    summary = response.choices[0].text.strip()
    return summary

def extract_key_points(text):
    doc = nlp(text)
    key_points = [sent.text for sent in doc.sents if 'roadmap' in sent.text.lower() or 'ux' in sent.text.lower() or 'prd' in sent.text.lower()]
    return key_points

@main.route('/process-transcript', methods=['POST'])
def process_transcript():
    data = request.json
    transcript = data.get('transcript')
    if not transcript:
        return jsonify({'error': 'No transcript provided'}), 400

    # Summarize the transcript
    summary = summarize_text(transcript)

    # Extract key points related to specific PM topics
    key_points = extract_key_points(transcript)

    return jsonify({
        'summary': summary,
        'key_points': key_points
    }), 200
