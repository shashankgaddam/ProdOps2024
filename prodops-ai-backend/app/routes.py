from flask import Flask, request, jsonify
import spacy
import openai
import os

UPLOAD_FOLDER = 'uploaded_transcripts'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# Load OpenAI API key
openai.api_key = 'your_openai_api_key'

def categorize_text(extracted_text):
    categories = {
        'roadmap': [],
        'prd': [],
        'ux_design': [],
        'user_stories': []
    }
    
    # Define keywords or phrases for each category
    keywords = {
        'roadmap': ['roadmap', 'timeline', 'milestone'],
        'prd': ['product requirement', 'PRD', 'feature'],
        'ux_design': ['UX design', 'interface', 'wireframe', 'prototype'],
        'user_stories': ['user story', 'story', 'acceptance criteria', 'AC']
    }

    # Categorize based on keywords
    for key, value in keywords.items():
        for word in value:
            if word in extracted_text.lower():
                categories[key].append(extracted_text)
                break  # Avoid placing the same text in multiple categories

    return categories

@app.route('/process-transcript', methods=['POST'])
def process_transcript():
    file = request.files['transcript']
    transcript_text = file.read().decode('utf-8')

    # Using SpaCy to process text
    doc = nlp(transcript_text)
    extracted_text = ' '.join([sent.text for sent in doc.sents])

    # Using OpenAI for more complex extraction if needed
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Extract key points and categorize into roadmap, PRD, UX design, and user stories: {transcript_text}",
        max_tokens=150
    )

    extracted_info = response.choices[0].text.strip()

    # Categorize the extracted text
    categorized_info = categorize_text(extracted_info)

    return jsonify(categorized_info)

@app.route('/upload-and-process', methods=['POST'])
def upload_and_process():
    file = request.files['transcript']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    transcript_text = file.read().decode('utf-8')

    # Process the transcript to extract and categorize
    doc = nlp(transcript_text)
    extracted_text = ' '.join([sent.text for sent in doc.sents])

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Extract key points and categorize into roadmap, PRD, UX design, and user stories: {transcript_text}",
        max_tokens=150
    )

    extracted_info = response.choices[0].text.strip()
    categorized_info = categorize_text(extracted_info)

    return jsonify(categorized_info)

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
