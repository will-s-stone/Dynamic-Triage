from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client['triage_db']  # Database name
patients_collection = db['patients']  # Collection to store patient information

def save_patient_data(patient_info, llm_response):
    """
    Save patient info and LLM response to MongoDB.
    """
    data = {
        "patient_info": patient_info,
        "llm_response": llm_response
    }
    patients_collection.insert_one(data)

def get_patient_data(patient_id):
    """
    Retrieve patient info by ID.
    """
    return patients_collection.find_one({"_id": patient_id})
