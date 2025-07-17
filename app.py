from flask import Flask
from db import create_connection

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World"

if __name__ == '__main__':
    app.run(debug=True)