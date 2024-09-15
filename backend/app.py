from flask import Flask, render_template

app = Flask(__name__, template_folder='../frontend/templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/patient')
def patient():
    return render_template('patient.html')

if __name__ == '__main__':
    app.run(debug=True)
