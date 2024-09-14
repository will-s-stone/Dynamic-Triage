from transformers import pipeline
from flask import Flask, request, jsonify
import torch

app = Flask(__name__)

pipe = pipeline("summarization", model="Falconsai/medical_summarization", device=0)


if torch.backends
txt = ("Jane Doe, a 34-year-old female, has a medical history that includes asthma diagnosed at age 10, "
       "seasonal allergies, and recent hypertension. She reports experiencing a persistent dry cough for the past "
       "two weeks, accompanied by shortness of breath, particularly during physical activity, occasional wheezing, "
       "and mild chest discomfort mainly in the evening. Despite these symptoms, she has not experienced any fever "
       "but feels generally fatigued. Currently, Jane is taking Loratadine (10 mg daily) for her allergies and Lisinopril "
       "(20 mg daily) for hypertension. She occasionally uses an over-the-counter cough suppressant containing Dextromethorphan. "
       "Recent medical tests include a chest X-ray, which showed no significant abnormalities, and spirometry, which revealed "
       "a mild obstructive pattern. Her blood pressure is measured at 140/90 mmHg. Jane does not smoke, has not traveled recently, "
       "and works in a dusty environment. She engages in moderate exercise three times a week. Her family medical history includes "
       "type 2 diabetes in her mother, heart disease in her father, and asthma in a sibling.")

# Generate the summary
summary = pipe(txt)

# Print the summarized text
print("Summary:", summary[0]['summary_text'])
