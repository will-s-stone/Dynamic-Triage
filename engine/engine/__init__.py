from transformers import pipeline
from flask import Flask, request, jsonify
import torch

app = Flask(__name__)

# Initialize the summarization pipeline
pipe = pipeline("summarization", model="Falconsai/medical_summarization")

# Move the model to CPU
device = "cpu"
pipe.model.to(device)

@app.route('/summarize', methods=['POST'])
def summarize_text():
    # Extract text from request body
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']

    try:
        # Run the summarizer on the input text
        output = pipe(text)
        return jsonify(output)
    except Exception as e:
        # Return error details for debugging
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)





