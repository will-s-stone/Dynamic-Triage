from flask import Flask, request, jsonify
from database import save_patient_data, get_patient_data
from llm_service import query_llm

app = Flask(__name__)


@app.route('/triage', methods=['POST'])
def triage_patient():
    """
    Endpoint to handle patient triage.
    Expects a POST request with patient information in JSON format.
    """
    data = request.json

    if not data or "patient_info" not in data:
        return jsonify({"error": "Invalid input, 'patient_info' is required"}), 400

    patient_info = data['patient_info']

    # Send patient information to the LLM
    llm_response = query_llm(patient_info)

    # Save the conversation (patient input + LLM response) to MongoDB
    save_patient_data(patient_info, llm_response)

    # Return the LLM response to the user (e.g., the 'spoke' in your case)
    return jsonify({"llm_response": llm_response})


@app.route('/patient/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    """
    Endpoint to retrieve stored patient data by patient ID.
    """
    patient_data = get_patient_data(patient_id)

    if not patient_data:
        return jsonify({"error": "Patient not found"}), 404

    return jsonify(patient_data)


if __name__ == "__main__":
    app.run(debug=True)


