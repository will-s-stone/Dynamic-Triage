from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient('mongodb+srv://<your_username>:<your_password>@<your_cluster>.mongodb.net/<your_database>?retryWrites=true&w=majority')
db = client.your_database

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)