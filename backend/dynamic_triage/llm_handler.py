from flask import Flask, request, jsonify
import os
import vertexai
from vertexai.generative_models import GenerativeModel, Part

# Initialize Flask app
app = Flask(__name__)


# Define a route for generating content
@app.route('/generate_content', methods=['POST'])
def generate_content():
    # Get API key from the request headers
    api_key = request.headers.get('API-Key')

    if not api_key:
        return jsonify({"error": "API-Key header is missing"}), 400

    # Set the API key in the environment for Vertex AI (assuming API key support)
    os.environ["API_KEY"] = api_key

    # Proceed with Vertex AI initialization using the API key
    vertexai.init(project="your-project-id", location="your-location")

    # Parse input JSON data
    data = request.get_json()

    text2_1 = data.get('text2_1',
                       """i have been coughing for 4 days. it is a dry cough, I feel it mainly in the mornings, it wakes me up at night sometimes""")
    text3_1 = data.get('text3_1',
                       """the cough comes in waves its like 3 heavy coughs I lose breath then I recover, it happens about 3 times a day, it happens mainly inside the house. no runny nose, I don't feel hot, I do wheeze when I cough, I drink tea for the cough""")

    # Initialize model
    model = GenerativeModel(
        "gemini-1.5-flash-001",
        system_instruction=[system_prompt]
    )

    chat = model.start_chat()

    # Send messages to the model
    result = chat.send_message(
        [text2_1, text3_1],
        generation_config=generation_config
    )

    # Return result as JSON
    return jsonify({'response': str(result)})


# Start the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)




